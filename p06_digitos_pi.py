from mpmath import *

def sum_digit_pi(n):
    mp.dps = n+1
    return sum([int(c) for c in str(mp.pi)[2:]])

if __name__== '__main__':
    print sum_digit_pi(144)