import math


class Vector:
    _v = None
    _n = 0
    """Constructor de la clase"""

    def __init__(self, x):
        self._v = [float(v) for v in x.split(",")]
        self._n = len(self._v)

    def n_euclid(self):
        return math.sqrt(sum([x ** 2 for x in self._v]))

    def n_sup(self):
        return max(self._v)

    @property
    def v(self):
        return self._v

    @property
    def n(self):
        return self._n


def main():
    v = Vector("1,2,2,12,5,10")
    print "vector [%s]" % (", ".join([str(x) for x in v.v]))
    print "norma euclidea %4.2f" % v.n_euclid()
    print "norma del supremo %4.2f" % v.n_sup()


if __name__ == "__main__":
    main()
