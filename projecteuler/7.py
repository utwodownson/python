#!/usr/bin/python



def gen_primes():
    D = {}
    q = 2
    while True:
        if q not in D: 
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1

def nth_prime(n):
  return (j for i,j in enumerate(gen_primes()) if i == n-1).next()

print nth_prime(10001)
