"""Synthetic accounting tests only; no provider or client data."""
import copy
import json
from pathlib import Path
import subprocess
import sys
import unittest

from summarize_observations import summarize, ValidationError, host_matches, alias_matches


def observation(**updates):
    row = dict(schema_version=2, observation_id="synthetic-o1", run_id="synthetic-run",
        panel_id="synthetic-panel", panel_version="1", prompt_id="p1", prompt_version="1",
        prompt_text="Synthetic: which product?", repeat_id="1", engine="synthetic-engine",
        model="synthetic-model", surface="synthetic-ui", source_type="simulated",
        search_mode="auto", search_used=True, locale="en-US", response_locale="en-US", market="US", intent="commercial",
        brand_scope="unbranded", observed_at="2026-09-24T10:00:00Z", status="ok", error=None,
        raw_answer="SYNTHETIC: Example Brand is recommended.", evidence_ref="synthetic:fixture",
        mention=True, mention_quote="Example Brand", recommendation=True,
        recommendation_quote="Example Brand is recommended.", citations=[], exclusion_reason=None,
        synthetic=True)
    row.update(updates)
    return row


def citation(**updates):
    c = dict(url="https://example.com/a", claim_quote="Example Brand is recommended.",
        source_quote="SYNTHETIC source support", fidelity="supported", evidence_ref="synthetic:source")
    c.update(updates)
    return c


def run(rows):
    return summarize([json.dumps(r) for r in rows], ["example.com"], ["Example Brand"], allow_synthetic=True)


class AccountingTests(unittest.TestCase):
    def test_rates_and_exact_duplicate(self):
        a = observation(citations=[citation(), citation()])
        b = observation(observation_id="o2", repeat_id="2", mention=False, mention_quote=None,
                        recommendation=None, recommendation_quote=None, citations=[])
        c = observation(observation_id="o3", repeat_id="3", mention=None, mention_quote=None,
                        recommendation=False, recommendation_quote=None, citations=None)
        report = run([a, copy.deepcopy(a), b, c])
        self.assertEqual((report["input_rows"], report["unique_observations"], report["exact_duplicates"]), (4,3,1))
        g = report["groups"][0]
        self.assertEqual(g["mention"], dict(numerator=1, denominator=2, unknown=1, rate=0.5))
        self.assertEqual(g["citation"], dict(numerator=1, denominator=2, unknown=1, rate=0.5))
        self.assertEqual(g["recommendation"], dict(numerator=1, denominator=2, unknown=1, rate=0.5))
        self.assertEqual(g["fidelity"]["denominator"], 1)
        self.assertEqual(g["duplicate_citations_removed"], 1)

    def test_error_unknown_no_search_and_exclusion(self):
        rows = [observation(search_used=False), observation(observation_id="o2", repeat_id="2", search_used=None),
                observation(observation_id="o3", repeat_id="3", exclusion_reason="predefined locale mismatch")]
        for i, status in enumerate(["error", "unknown"], 4):
            rows.append(observation(observation_id=f"o{i}", repeat_id=str(i), status=status,
                error="synthetic timeout or uncertain capture", raw_answer=None, mention=None, mention_quote=None,
                recommendation=None, recommendation_quote=None, citations=None, response_locale=None))
        r = run(rows)
        self.assertEqual(sum(g["eligible_answers"] for g in r["groups"]), 2)
        self.assertEqual({g["search_state"] for g in r["groups"]}, {"search", "no_search", "unknown"})
        g = next(g for g in r["groups"] if g["search_state"] == "search")
        self.assertEqual((g["errors"],g["unknown_status"],g["excluded"]), (1,1,1))
        self.assertIsNone(g["mention"]["rate"])
        self.assertEqual(g["mention"]["denominator"], 0)

    def test_fidelity_numerator_denominator_and_coverage(self):
        cs = [citation(url=f"https://example.com/{i}", fidelity=f) for i,f in enumerate(
            ["supported","partial","unsupported","unverifiable","not_reviewed"])]
        cs += [citation(url="https://evil-example.test/fake")]
        g = run([observation(citations=cs)])["groups"][0]
        self.assertEqual(g["fidelity"]["numerator"],1)
        self.assertEqual(g["fidelity"]["denominator"],3)
        self.assertEqual(g["fidelity"]["unknown"],2)
        self.assertEqual(g["fidelity_review_coverage"]["numerator"],3)
        self.assertEqual(g["fidelity_review_coverage"]["denominator"],5)

    def test_domain_boundaries_and_aliases(self):
        for u in ["https://evil-example.test", "https://example.com.evil.test", "https://evil.test/example.com"]:
            self.assertFalse(host_matches(u, ["example.com"], True))
        self.assertFalse(host_matches("https://sub.example.com", ["example.com"], False))
        self.assertTrue(host_matches("https://sub.example.com", ["example.com"], True))
        self.assertTrue(host_matches("https://EXAMPLE.com./x", ["example.com"], False))
        self.assertFalse(alias_matches("NotExample Brandish", ["Example Brand"]))
        self.assertTrue(alias_matches("Use EXAMPLE BRAND!", ["Example Brand"]))

    def test_domain_normalization_is_lossless_and_fail_closed(self):
        self.assertFalse(host_matches('https://xn--fa-hia.example/a', ['fass.example']))
        self.assertTrue(host_matches('https://xn--fa-hia.example/a', ['xn--fa-hia.example']))
        for url in ('https://faß.example/a', 'https://example.com.../a', 'https://example.com../a'):
            with self.subTest(url=url), self.assertRaises(ValidationError):
                host_matches(url, ['fass.example', 'example.com'])
        with self.assertRaises(ValidationError):
            run([observation(citations=[citation(url='https://example.com.../a')])])

    def test_mention_quote_boundaries_use_answer_context(self):
        for answer in ('NotExample Brandish', 'Example Brandish', 'NotExample Brand',
                       'Example Brand exists. NotExample Brandish only.'):
            quote = 'Example Brandish' if answer.endswith('only.') else 'Example Brand'
            with self.subTest(answer=answer), self.assertRaises(ValidationError):
                run([observation(raw_answer=answer, mention_quote=quote,
                                 recommendation=False, recommendation_quote=None)])
        answer = 'NotExample Brandish; Example Brand is real.'
        self.assertEqual(run([observation(raw_answer=answer, recommendation=False,
            recommendation_quote=None)])["groups"][0]["mention"]["numerator"], 1)

    def test_response_language_is_observed_not_frozen(self):
        rows = [observation(schema_version=2, response_locale=lang,
            observation_id=f'o{i}', repeat_id=str(i))
            for i, lang in enumerate(('en-US', 'es', 'mul', None), 1)]
        report = run(rows)
        self.assertEqual(report['schema_version'], 2)
        self.assertEqual(len(report['groups']), 1)
        self.assertEqual(report['groups'][0]['eligible_response_locales'],
                         {'en-US': 1, 'es': 1, 'mul': 1, 'unknown': 1})
        changed = copy.deepcopy(rows[0]); changed['observation_id'] = 'different'
        changed['response_locale'] = 'es'
        with self.assertRaisesRegex(ValidationError, 'duplicate measurement cell'):
            run([rows[0], changed])
        changed['repeat_id'] = '5'; changed['locale'] = 'es'
        with self.assertRaisesRegex(ValidationError, 'prompt definition drift'):
            run([rows[0], changed])

    def test_unicode_surrogate_cli_is_controlled_error(self):
        script = str(Path(__file__).with_name('summarize_observations.py'))
        args = [sys.executable, script, '-', '--domain', 'example.com',
                '--alias', 'Example Brand', '--allow-synthetic']
        for row in (observation(engine='\ud800'), observation(raw_answer='\ud800'),
                    observation(**{'\ud800': 'bad key'})):
            p = subprocess.run(args, input=json.dumps(row), text=True, capture_output=True)
            self.assertEqual(p.returncode, 2, p.stderr)
            self.assertEqual(p.stdout, '')
            self.assertIn('error', json.loads(p.stderr))
            self.assertNotIn('Traceback', p.stderr)

    def test_invalid_records_fail(self):
        variants = [dict(status="success"), dict(search_used="false"), dict(schema_version=True),
            dict(schema_version=1), dict(response_locale=7), dict(response_locale='unknown!'),
            dict(observed_at="2026-09-24"), dict(observed_at="2026-02-30T10:00:00Z"),
            dict(observed_at="2026-09-24T10:00:00+00:99"),
            dict(mention="false"), dict(unknown_field=1), dict(mention_quote="Brand"),
            dict(citations=[citation(url="javascript:bad")]), dict(citations=[citation(fidelity="correct")]),
            dict(status="error"), dict(recommendation_quote="not in answer"), dict(raw_answer=""),
            dict(locale=" "), dict(search_mode="off", search_used=True)]
        for update in variants:
            with self.subTest(update=update), self.assertRaises(ValidationError): run([observation(**update)])
        r = observation(); del r["engine"]
        with self.assertRaises(ValidationError): run([r])

    def test_conflicts_fail_not_silently_deduped(self):
        with self.assertRaises(ValidationError): run([observation(), observation(mention=False, mention_quote=None)])
        with self.assertRaises(ValidationError): run([observation(), observation(observation_id="new-id")])
        with self.assertRaises(ValidationError): run([observation(citations=[citation(),citation(fidelity="partial")])])

    def test_json_unknown_and_empty(self):
        for lines in [['{broken'], ['{"status":"ok","status":"error"}'], ['NaN'], ['[]'], ['']]:
            with self.assertRaises(ValidationError): summarize(lines,["example.com"],["Example Brand"])
        self.assertEqual(summarize([], ["example.com"],["Example Brand"])["groups"], [])

    def test_split_panels_engines_locales_dates_sources(self):
        rows = [observation()]
        for i, update in enumerate([dict(panel_version="2"), dict(engine="other"), dict(locale="es-ES"),
             dict(observed_at="2026-09-25T00:00:00Z"), dict(source_type="api"),dict(brand_scope="branded")], 2):
            rows.append(observation(observation_id=f"o{i}", prompt_id=f"p{i}", run_id=f"run{i}", **update))
        self.assertEqual(len(run(rows)["groups"]),7)

    def test_panel_definition_drift_rejected(self):
        with self.assertRaises(ValidationError):
            run([observation(), observation(observation_id="o2", repeat_id="2", prompt_text="changed wording")])

    def test_unknown_metrics_not_absence(self):
        g = run([observation(mention=None, mention_quote=None, recommendation=None,
                             recommendation_quote=None, citations=None)])["groups"][0]
        for metric in ("mention", "citation", "recommendation"):
            self.assertEqual(g[metric], dict(numerator=0,denominator=0,unknown=1,rate=None))

    def test_synthetic_guard(self):
        with self.assertRaises(ValidationError):
            summarize([json.dumps(observation())],["example.com"],["Example Brand"])
        self.assertEqual(run([observation()])["evidence_kind"],"synthetic_only")

    def test_cli_real_process(self):
        script = str(Path(__file__).with_name("summarize_observations.py"))
        args = [sys.executable,script,"-","--domain","example.com","--alias","Example Brand"]
        p = subprocess.run(args+["--allow-synthetic"],input=json.dumps(observation())+"\n",text=True,capture_output=True)
        self.assertEqual(p.returncode,0,p.stderr)
        self.assertEqual(json.loads(p.stdout)["unique_observations"],1)
        for data in ["{invalid\n",json.dumps(observation(status="bogus")),json.dumps(observation())]:
            p = subprocess.run(args,input=data,text=True,capture_output=True)
            self.assertEqual(p.returncode,2)
            self.assertEqual(p.stdout,"")
            self.assertIn("error",p.stderr)


if __name__ == "__main__":
    unittest.main()
