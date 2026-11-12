from math import isqrt
A = 24153319581254312065344
B = 24885189317885898975235988544

def factor(n):
    result = []
    d = 2
    while d*d <= n:
        if n % d == 0:
            e = 0
            while n % d == 0:
                n //= d
                e += 1
            result.append((d, e))
        d += 1
    if n > 1:
        result.append((n, 1))
    return result

f = factor(A)
assert all(p >= 2 and all(p % x for x in range(2, isqrt(p)+1)) for p,e in f)
assert B == 101**3*A and A % 101 != 0
print('factorization of a(6):', f)
print('bound equals 101^3 times a(6):', True)
print('distinct prime counts at a(6), bound:', len(f), len(f)+1)
print('11 <= 2*7:', 11 <= 2*7)
