def bubble_sort(l):
    n = len(l)
    while not is_sorted(l):
        for i in range(n - 1):
            if l[i + 1] < l[i]:
                l[i + 1], l[i] = l[i], l[i+1]
    return l


def is_sorted(l):
    n = len(l)
    issorted = True
    for i in range(n - 1):
        if l[i + 1] < l[i]:
            issorted = False
            break
    return issorted


def main():
    l = [5,4,3,2,1]
    print l
    print bubble_sort(l)

if __name__ == '__main__':
    main()
