# Independent verification of A011541 certificate (2026-11-15)

Source: uploaded archive of ``iwasborninbali/oeis-A011541-unsubmitted`` at commit ``f605ec31d584172540812c43122f2eb94a98f5e3``. Referee is independent of the authors of ``proof.md``, ``CERTIFICATE.md``, and ``verification/check.py``. The archive contains no ``programs/`` directory; its only program is ``verification/check.py``.

## Claim

**Exact ``CERTIFICATE.md`` claim (one line):** If a(7) equals the bound displayed in A011541, then ω(a(7))=11>10=ω(a(6)) and 11≤14, assuming the displayed a(6).

This is a *conditional arithmetic assertion*. It neither says that ``a(7)`` equals the upper bound nor establishes minimality of any taxicab term.

## Proof check

**Proof verdict: correct** for the exact conditional claim. No incorrect mathematical step, fatal gap, hidden use of Pavlov's conjecture, or circular argument was found. The complete line-by-line audit is:

- **Line 1:** Heading only; no mathematical assertion.
- **Line 2:** Blank.
- **Line 3:** ``A=24153319581254312065344`` and ``B=24885189317885898975235988544`` agree with the public A011541 sequence and bound. **Expository omission, fixable:** cite the current OEIS entry in ``proof.md``, rather than relying on a separate README. The identification ``A=a(6)`` is **conditional on the listed sixth term**, an assumption stated in both ``proof.md`` and ``CERTIFICATE.md``, not a hidden hypothesis or an error.
- **Line 4:** Blank.
- **Line 5:** ``A=2^6*3^3*7^4*13*19*43*73*79^3*97*157`` and ``B=101^3*A`` are **correct exact integer identities**. **Expository omission, fixable:** the proof gives no multiplication worksheet or machine output inline; either expand the multiplication or cite a reproducible factorization certificate. The separate independent program here verifies both equalities.
- **Line 6:** Blank.
- **Line 7, primality sentence:** Every listed factor is prime, pairwise distinct, and not 101, and 101 is prime. Direct tests up to each factor's integer square root suffice; no unproved primality conjecture is needed. **Expository omission, fixable:** the script or a small prime/divisibility table can be cited to display the actual checks. The independent sieve-and-exact-quotient computation here establishes all factors and leaves no cofactor.
- **Line 7, omega sentence:** Counting the ten distinct primes of ``A`` and the newly introduced prime 101 gives ``ω(A)=10`` and ``ω(B)=11``, hence ``11>10`` and ``11<=2*7=14``. **Correct**, once the previous exact identities are checked.
- **Line 7, final sentence:** Correct **only under ``a(7)=B`` and the listed ``a(6)``**. The proof explicitly says it does not prove later conjectural behavior and takes the displayed sixth term as given. The phrase 'both stated conditions' must not be read as unconditional confirmation of Pavlov's conjecture.

**Not proved (and not required by this certificate):** the leastness of ``a(6)`` or ``a(7)``; whether ``a(7)=B``; the strict-increase or ``2n`` conjecture for other unknown terms. These are scope exclusions, **not fatal defects in the conditional proof**. With the additional calculation below we also verify that ``B`` has seven cube decompositions (so it is a genuine *upper-bound witness*), but not that it is minimal.

## Independent computation

I wrote ``independent_check.py`` from scratch without reading/importing any of the repository's executable code into it. Inputs are the six publicly listed integers ``a(1)..a(6)`` and the seventh **upper bound** ``B``, not a presumed seventh term. Methods differ from the repository's ascending-integer trial division:

1. Build a sieve of Eratosthenes through 1000. Divide every input by all sieve primes, accumulate exponents, and require the remaining cofactor to equal exactly 1. Multiply the factors back to the original integer. Thus the factorization is **complete**, even though large input integers are used; sieve primality is exact in this range.
2. Enumerate all divisors ``s`` of each completely factored integer ``N``. For positive unordered integer cubes ``N=x^3+y^3``, ``1<=x<=y``, put ``s=x+y``, ``t=y-x``. Then ``s|N``, ``4N=s(s^2+3t^2)``, and ``t^2=(4N/s-s^2)/3``. Test all divisors for nonnegative integral square ``t^2``, parity, positivity and the original cube identity. Therefore this enumeration is **exhaustive** for each fixed ``N``; it is not a search truncated at a cube-root bound.
3. Compare ``B`` directly to ``101^3*a(6)`` and check ``101`` is a new prime factor. This independently tests the exact certificate while also extending the repository's check to ``a(1)..a(5)`` and to *complete* representations of every listed integer and of ``B``.

**Range:** seven exact integers: OEIS-listed ``a(1)`` through ``a(6)``, and ``B=24885189317885898975235988544``. No range of unknown ``a(n)`` is asserted.

| Number | ω | Exact positive unordered cube representations |
|---|---:|---:|
| listed ``a(1)=2`` | 1 | 1 |
| listed ``a(2)=1729`` | 3 | 2 |
| listed ``a(3)=87539319`` | 5 | 3 |
| listed ``a(4)=6963472309248`` | 8 | 4 |
| listed ``a(5)=48988659276962496`` | 9 | 5 |
| listed ``a(6)=24153319581254312065344`` | **10** | 6 |
| seventh bound ``B=24885189317885898975235988544`` | **11** | **7** |

The complete independent factorization of ``B`` is:

``2^6 * 3^3 * 7^4 * 13 * 19 * 43 * 73 * 79^3 * 97 * 101^3 * 157``.

``B=101^3*a(6)`` is **true** and the conditions ``11>10`` and ``11<=14`` are **true**. Seven verified cube pairs of ``B`` (each pair ``(x,y)`` means ``x^3+y^3=B``) are:

```
(58798362,2919526806)
(309481473,2918375103)
(459531128,2915734948)
(860447381,2894406187)
(1638024868,2736414008)
(1766742096,2685635652)
(1847282122,2648660966)
```

**Runtime:** ``elapsed_seconds=0.064779`` as recorded by ``time.perf_counter()`` for this run in the supplied CPU container (including factoring and enumeration; subsequent runs will differ). Requires Python 3 standard library only; run ``python3 independent_check.py`` from this directory. Its recorded output is ``independent_check.log``.

**SHA-256 of program:** ``b89d2d8e9f8b80d2362f70ff775967731d34b98f77bb55e93158ae6e628b1a40``  
**SHA-256 of output log:** ``7f2cc9c0c7e0bd17f7ad6dfbbfc7b10a82a9d96b9500e67bac35f4720c87914b``

## Prior art

Checked publicly available sources on **2026-11-15**. Distinguish prior publication of the arithmetic identity from prior publication of an explicit correction to Pavlov's particular sentence:

1. **OEIS A011541:** <https://oeis.org/A011541/internal> (comments ``%C``). It lists ``a(6)``, the bound ``B`` attributed to Robert G. Wilson v (Nov 18 2012), and Sergey Pavlov's Mar 01 2017 conjecture with the parenthetical saying monotonicity would fail if ``a(7)`` equaled ``B``. The parenthetical remains present. The internal-format page's revision marker is ``#194 Sep 15 2026``. **This is the error under review, not prior correction.** <https://oeis.org/A011541/list> independently lists all six known displayed terms.
2. **Direct OEIS cross references:** <https://oeis.org/A001235> (alternative taxi-cab sequence), <https://oeis.org/A003826> (primitive representations in at least four ways), <https://oeis.org/A023050> (coprime cube sums), <https://oeis.org/A047696> (Cabtaxi, including a separate 2017 prime-factor comment by Pavlov), and <https://oeis.org/A080642> (cubefree taxicab). They offer related context, **not this specific correction**. Crucially also checked <https://oeis.org/A273594/internal> (Altug Alkan, May 26 2016), which **already states explicitly** ``A011541(7) <= 101^3*A011541(6)``. That identity pre-dates Pavlov's 2017 sentence and the Athanor repository.
3. **arXiv:** Pavel Emelyanov, *On Hunting for Taxicab Numbers*, arXiv:0802.1147v1 (submitted Feb 8, 2008), <https://arxiv.org/html/0802.1147v1>, Appendix A **explicitly gives** ``T_7=101^3 R_6=24885189317885898975235988544`` with the **same seven positive cube pairs**. This is unambiguous prior art for the main numerical identity and witness. No mention of Pavlov's later parenthetical can occur in this 2008 paper.
4. **Journals:** Christian Boyer, *New Upper Bounds for Taxicab and Cabtaxi Numbers*, *Journal of Integer Sequences* **11** (2008), 08.1.6, <https://cs.uwaterloo.ca/journals/JIS/VOL11/Boyer/boyer.html>, says it presents bounds for Taxicab(7..19) and decompositions through Taxicab(12). David W. Wilson, *The Fifth Taxicab Number is 48988659276962496*, *JIS* **2** (1999), 99.1.9, <https://cs.uwaterloo.ca/journals/JIS/wilson10.html>, concerns the earlier term. Calude, Calude and Dinneen (2003), *What is the Value of Taxicab(6)?*, cited by <https://oeis.org/A011541/internal>, concerns probabilistic evidence for the sixth term. Po-Chi Su, *More Upper Bounds on Taxicab and Cabtaxi Numbers*, *JIS* **19** (2016), 16.4.3, <https://cs.uwaterloo.ca/journals/JIS/VOL19/Su/su3.html>, concerns higher bounds. A later Springer article, <https://link.springer.com/article/10.1007/s11139-024-00968-6>, describes the six known taxicab numbers and says later ones remain unknown. **None of the inspected journal abstracts/pages supplied the exact post-2017 prime-factor correction.**
5. **MathOverflow / Mathematics Stack Exchange:** searched ``site:mathoverflow.net`` and ``site:math.stackexchange.com`` for ``A011541``, ``Pavlov``, ``taxicab``, ``prime factors``, and ``distinct prime factors``, including exact correction phrases. Found discussions of the taxicab problem, e.g. <https://math.stackexchange.com/questions/2815/find-taxicab-numbers-in-on-time/2847>, which discusses a bound around ``2.5*10^28``, **but no indexed direct correction of Pavlov's specific parenthetical**. This is a negative search result, not proof that no post exists.
6. **zbMATH Open:** searched web-indexed ``site:zbmath.org`` records for ``taxicab Boyer``, ``On Hunting for Taxicab Numbers``, ``What is the value of Taxicab(6)``, and ``Pavlov taxicab``; **no relevant accessible entry supplying the proposed correction was located**. This does not substitute for a complete zbMATH bibliographic search.
7. **OEIS edit history:** attempted <https://oeis.org/history?seq=A011541> and <https://oeis.org/A011541/history> but these history endpoints were **not accessible through the browsing interface**. Dated comments and the ``#194`` current internal-format revision were inspected. A full historical revision-by-revision search is **not established**.

**Novelty assessment:** The 101-cubed identity and all seven cube witnesses are demonstrably **not new** (2008, and recorded in OEIS A273594 in 2016). The elementary deduction of ``ω(B)=11`` is independently correct. An earlier **explicit, post-2017 published correction of Pavlov's wording** was not found in the examined sources, but cannot be ruled out; priority/novelty of that correction is **not established**. The lab's ``PRIOR-ART.md`` does not make a priority claim.

## Verdict

**COMPLETE for the exact certificate claim:** the conditional implication is true, its short proof is correct, and every arithmetic/computational component was re-verified independently using a separate algorithm, over the six published terms plus the seventh bound. The bound even has exactly seven positive unordered cube representations.

**Separately: novelty of the proposed correction is NOT ESTABLISHED.** Its key identity is established prior art and the OEIS history endpoint could not be fully reviewed. No unconditional statement about ``a(7)`` or the global prime-factor conjecture follows. A correction to the OEIS parenthetical can be justified by the arithmetic, but it should not be presented as a new result about taxicab minimality or as priority over earlier published calculations.
