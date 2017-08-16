from __future__ import division
from math import sqrt as sq


def fibo(n):
    if n <= 2:
        return 1
    elif n >= 3:
        return fibo(n - 1) + fibo(n - 2)


def main():
    fi = (1 + sq(5)) / 2
    k = 2
    while abs(fi - fibo(k) / fibo(k - 1)) > 0.00000000001:
        print k
        k += 1
    print "lo logre despues de %d vueltas" % k
    print "la aproximacion de %.7f es %.7f" %(fi,fibo(k) / fibo(k - 1))

if __name__ == '__main__':
    main()