# OEIS A011541: correction to the seventh-bound remark (not yet submitted)

<!-- oeis-status:begin -->
**OEIS status: not submitted** (lab registry, 15 Nov 2026).

- [A011541](https://oeis.org/A011541), remark on Pavlov's conjecture vs the bound 101^3*a(6): **candidate** (2026-11-13: repository built (core c6)). Certificate: complete.

Rules and the full registry: [athanor-oeis](https://github.com/iwasborninbali/athanor-oeis/blob/main/REGISTRY.md).
<!-- oeis-status:end -->

## Definition

For n≥1, a(n) is the least positive integer with at least n representations as a sum of two positive integer cubes, unordered, counting equal summands once. The offset is 1.

## Terms / result

No term or bound is changed. The live [A011541](https://oeis.org/A011541), read 2026-11-13, gives the bound `a(7) <= 24885189317885898975235988544`, attributed to Robert G. Wilson v, Nov 18 2012. Sergey Pavlov's Mar 01 2017 conjecture includes the exact parenthesis `(this is not true if a(7) is equal to the upper bound given above)`. Equality to that displayed bound would instead give 11 distinct prime factors, compared with 10 for the listed a(6), and 11≤14. Thus the asserted failure does not occur at the sixth-to-seventh transition.

## How it was obtained

The bound is exactly 101³ times the sixth term, and 101 is a new prime factor. [proof.md](proof.md) gives the complete factorization and argument.

## Verification

An independent trial-division script checks the factorization and equality using exact integers. It does not establish the minimum a(6), the bound's cube representations, or the conjecture for all n. See [CERTIFICATE.md](CERTIFICATE.md).

## Prior art and credit

The bound is attributed in OEIS to Wilson and the conjecture to Pavlov. The lab's ChatGPT answer noticed the arithmetic issue, independently checked by Claude Code. See [PRIOR-ART.md](PRIOR-ART.md).

## Reproduce

Run `python3 verification/check.py` (under one second). Expected output:

```text
factorization of a(6): [(2, 6), (3, 3), (7, 4), (13, 1), (19, 1), (43, 1), (73, 1), (79, 3), (97, 1), (157, 1)]
bound equals 101^3 times a(6): True
distinct prime counts at a(6), bound: 10 11
11 <= 2*7: True
```

## Provenance

Source: `projects/science/athanor-oeis`, commit `11b7ea9cc6f4c0057731d8e36c023f8b36e7c27f`, `tasks/2026-11-12-A011541-taxicab-prime-factors/answers/2026-11-12-chatgpt.md`. The checker was separately written for this repository.

## Author, licence

Aleksei Kudriashov (ORCID 0009-0006-8885-5338), Athanor lab, with AI assistance (OpenAI Codex cores; Claude Code as the lab's guide). Code: MIT; data and text: CC BY 4.0 (see LICENSE.md).
