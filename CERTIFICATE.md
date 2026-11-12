# Verification certificate

## Claim

If a(7) equals the bound displayed in A011541, then ω(a(7))=11>10=ω(a(6)) and 11≤14, assuming the displayed a(6).

## Evidence

| What | Path | Author and date | Coverage | Result |
|---|---|---|---|---|
| Derivation | [proof.md](proof.md) | OpenAI Codex, 2026-11-13, based on reviewed source | Listed a(6) and bound | Parenthetical fails at n=7 |
| Independent check | [verification/check.py](verification/check.py) | OpenAI Codex, 2026-11-13 | Exact factorization and equality | 10 and 11 prime factors |

The checker shares the displayed numbers but no code with the source answer; trial division checks primality and factorization.

## Replayed for this repository

2026-11-13, macOS local workstation: `python3 verification/check.py`; full output is [verification/logs/check.txt](verification/logs/check.txt) and is reproduced in README.

## Not covered

Minimality of a(6), the validity or optimality of the seventh bound, and the conjecture beyond this arithmetic consequence were not checked. The hypothesis a(7) equals the displayed bound is not asserted to be true.

## Guide's independent check

pending

## Verdict

complete — the independent arithmetic check was replayed in full.
