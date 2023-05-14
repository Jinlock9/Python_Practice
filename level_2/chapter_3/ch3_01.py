# Chapter 03-01
# Special Method (Magic Method)
# 파이썬의 핵심 -> 시퀀스 (Sequence), 반복 (Iterator), 함수 (Functions), Class (클래스)

# 클래스 안에 정의할 수 있는 특별한 (Built-in) 메소드

# 기본형
print(int)
print(float)

# 모든 속성 및 메소드 출력
print(dir(int))
print(dir(float))

n = 10

print(n + 100)
print(n.__add__(100))
# print(n.__doc__)
print(n.__bool__(), bool(n))
print(n * 100, n.__mul__(100))

print()
print()


# Class example 1
class Fruit:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    def get_name(self):
        return self._name

    def get_price(self):
        return self._price

    def __str__(self):
        return 'Fruit Class Info: {} ${}'.format(self._name, self._price)

    def __add__(self, other):
        print("Call >> __add__")
        return self._price + other.get_price()

    def __sub__(self, other):
        print("Call >> __sub__")
        return self._price - other.get_price()

    def __le__(self, other):
        print("Call >> __le__")
        if self._price <= other.get_price():
            return True
        else:
            return False

    def __ge__(self, other):
        print("Call >> __ge__")
        if self._price >= other.get_price():
            return True
        else:
            return False


# create Instance
s1 = Fruit('Orange', 7500)
s2 = Fruit('Banana', 3000)

# print(s1._price + s2._price)
print(s1 + s2)
print(s1 - s2)
print(s2 - s1)

print(s1 >= s2)
print(s1 <= s2)

print(s1)
print(s2)
