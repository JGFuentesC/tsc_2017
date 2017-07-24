def fact():
    i = 1
    f = 1
    n = 5
    if n < 0:
        print "Error"
    elif n == 0 or n == 1:
        print "1"
    elif n >= 2:
        while i <= n:
            f *= i
            i += 1
        print "%d" % f


if __name__ == "__main__":
    fact()
