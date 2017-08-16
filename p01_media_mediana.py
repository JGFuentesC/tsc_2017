from __future__ import division


def main():
    num = raw_input()
    num = num.split(" ")
    num = [int(x) for x in num]
    print "la media es %.1f" % media(num)
    print "la mediana es %.1f" % mediana(num)


def media(num):
    suma = 0
    n = len(num)
    for i in range(n):
        suma += num[i]
    return suma / n


def mediana(num):
    num = sorted(num)
    n = len(num)
    if n % 2 == 0:
        return (num[n // 2-1] + num[n // 2])/2
    else:
        return num[n // 2]


if __name__ == '__main__':
    main()
