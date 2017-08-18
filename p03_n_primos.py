from __future__ import division
from math import sqrt as sq


def isprime(n):
    prime = True
    ls = int(sq(n))
    for i in range(2, ls + 1):
        if n % i == 0:
            prime = False
            break
    return prime


def main():
    tot = 100
    lst_prime = []
    n = 2
    while len(lst_prime) < tot:
        if isprime(n):
            lst_prime.append(n)
        n += 1
    print lst_prime

if __name__ == '__main__':
    main()