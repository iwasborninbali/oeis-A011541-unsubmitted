#!/usr/bin/env python3
"""Independent exact audit of OEIS A011541 arithmetic and cube witnesses.

Uses a sieve followed by complete division, not the repository's
incrementing trial-divisor routine. Unordered positive cube pairs are
enumerated through divisors of N and the discriminant identity
4N = s(s*s + 3*t*t), with s=x+y and t=y-x.
"""

from math import isqrt
from time import perf_counter

TERMS = (
    2,
    1729,
    87539319,
    6963472309248,
    48988659276962496,
    24153319581254312065344,
)
BOUND7 = 24885189317885898975235988544


def small_primes(limit):
    allowed = bytearray(b"\x01") * (limit + 1)
    allowed[0:2] = b"\x00\x00"
    for p in range(2, isqrt(limit) + 1):
        if allowed[p]:
            allowed[p*p:limit+1:p] = b"\x00" * ((limit-p*p)//p+1)
    return [n for n in range(2, limit+1) if allowed[n]]


def complete_factorization(value, primes):
    remaining = value
    out = []
    for p in primes:
        if remaining == 1:
            break
        if remaining % p:
            continue
        power = 0
        while remaining % p == 0:
            power += 1
            remaining //= p
        out.append((p, power))
    if remaining != 1:
        raise AssertionError(f"Unfactored cofactor {remaining} of {value}")
    product = 1
    for p, exponent in out:
        product *= p ** exponent
    assert product == value
    return out


def positive_cube_pairs(value, factors):
    divisors = [1]
    for prime, exponent in factors:
        original_divisors = tuple(divisors)
        prime_power = 1
        for _ in range(exponent):
            prime_power *= prime
            divisors.extend(d * prime_power for d in original_divisors)
    pairs = []
    for sum_xy in divisors:
        # From N = (x+y)(x*x-x*y+y*y) and
        # 4*N/(x+y) = (x+y)^2 + 3*(y-x)^2.
        candidate = 4 * (value // sum_xy) - sum_xy * sum_xy
        if candidate < 0 or candidate % 3:
            continue
        difference_squared = candidate // 3
        difference = isqrt(difference_squared)
        if difference * difference != difference_squared:
            continue
        if difference >= sum_xy or (sum_xy - difference) % 2:
            continue
        x, y = (sum_xy - difference) // 2, (sum_xy + difference) // 2
        assert 1 <= x <= y and x**3 + y**3 == value
        pairs.append((x, y))
    assert len(pairs) == len(set(pairs))
    return sorted(pairs)


def main():
    start = perf_counter()
    primes = small_primes(1000)
    values = TERMS + (BOUND7,)
    factors = [complete_factorization(v, primes) for v in values]
    assert BOUND7 == TERMS[5] * (101 ** 3)
    assert 101 not in [p for p, _ in factors[5]]
    assert [p for p, _ in factors[6]] == sorted([p for p, _ in factors[5]] + [101])
    expected = [1, 2, 3, 4, 5, 6, 7]
    counts = []
    for i, (value, fac) in enumerate(zip(values, factors)):
        pairs = positive_cube_pairs(value, fac)
        counts.append(len(pairs))
        label = f"a({i+1})" if i < 6 else "B7 (upper bound, not proved minimal)"
        print(f"{label}: N={value}")
        print(f"  factorization={fac}")
        print(f"  omega={len(fac)}; exact positive unordered cube representations={len(pairs)}")
        if i == 6:
            for x, y in pairs:
                print(f"  witness=({x},{y})")
    assert counts == expected, (counts, expected)
    print("cube representation counts for a(1..6) and B7:", counts)
    print("distinct prime counts for a(1..6) and B7:", [len(f) for f in factors])
    print("B7 == 101^3 * a(6):", BOUND7 == 101**3 * TERMS[5])
    print("conditional omega(B7)>omega(a6):", len(factors[6]) > len(factors[5]))
    print("conditional omega(B7)<=2*7:", len(factors[6]) <= 14)
    print("No minimality test has been performed for any a(n).")
    print(f"elapsed_seconds={perf_counter()-start:.6f}")


if __name__ == "__main__":
    main()
