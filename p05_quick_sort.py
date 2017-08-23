def quicksort(l):
    if len(l) > 0:
        if len(l) >= 2:
            piv = len(l) // 2
        else:
            piv = 0
        p = l.pop(piv)
        return quicksort(filter(lambda x: x < p, l)) + [p]+ quicksort(filter(lambda x: x >= p, l))
    else:
        return []


def main():
    print quicksort([6, 7, 5, 4, 3, 7, 2, 2, 1])


if __name__ == '__main__':
    main()
