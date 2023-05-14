# Chapter 03-02
# Special Method (Magic Method)
# 파이썬의 핵심 -> 시퀀스 (Sequence), 반복 (Iterator), 함수 (Functions), Class (클래스)

# 클래스 안에 정의할 수 있는 특별한 (Built-in) 메소드

# Class example 2
# Vector(x, y)
# (5, 2) + (4, 3) = (9, 5)
# (10, 3) * 5 = (50, 15)
# Max(5, 10) = 10

class Vector(object):
    def __init__(self, *args):
        """
        Create a vector, example : v = Vector(5, 10)
        :param args:
        """
        if len(args) == 0:
            self._x, self._y = 0, 0
        else:
            self._x, self._y = args

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def __repr__(self):
        """
        Return the vector information.
        """
        return 'Vector(%r, %r)' % (self._x, self._y)

    def __add__(self, other):
        """
        Return the Vector addition of self and other
        """
        return Vector(self._x + other.get_x(), self._y + other.get_y())

    def __mul__(self, other):
        return Vector(self._x * other, self._y * other)

    def __bool__(self):
        """
        Find whether Vector is on an origin or not
        """
        return not bool(max(self._x, self._y))


# create Vector Instance
v1 = Vector(5, 7)
v2 = Vector(23, 35)
v3 = Vector()

# print Vectors
print(Vector.__init__.__doc__)
print(Vector.__repr__.__doc__)
print(Vector.__add__.__doc__)

print(v1, v2, v3)

print(v1 + v2)
print(v1 * 3)
print(bool(v1), bool(v2), bool(v3))
