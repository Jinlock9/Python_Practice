# Chapter 03-02
# Special Method (Magic Method)
# 파이썬의 핵심 -> 시퀀스 (Sequence), 반복 (Iterator), 함수 (Functions), Class (클래스)

# 클래스 안에 정의할 수 있는 특별한 (Built-in) 메소드

# 객체 -> 파이썬의 데이터 추상화
# 모든 객체 -> id, type -> value

from math import sqrt
from collections import namedtuple

# general tuple ========================================================================================================
pt1 = (1.0, 5.0)
pt2 = (2.5, 1.5)

l_length1 = sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2)

print(l_length1)

# Named Tuple: tuple that has the attribute of dictionary ==============================================================
# declare named tuple
Point = namedtuple('Point', 'x y')

pt3 = Point(1.0, 5.0)
pt4 = Point(2.5, 1.5)

print(pt3, pt3[0], pt3[1])
print(pt4, pt4.x, pt4.y)

l_length2 = sqrt((pt3.x - pt4.x) ** 2 + (pt3.y - pt4.y) ** 2)
print(l_length2)

# method to declare Named Tuple ========================================================================================
Point1 = namedtuple('Point', ['x', 'y'])
Point2 = namedtuple('Point', 'x, y')
Point3 = namedtuple('Point', 'x y')
Point4 = namedtuple('Point', 'x y x class', rename=True)  # Default = False, 디폴트 상태는 예약어나 중복되는 단어가 들어가면 안됨

print(Point1, Point2, Point3, Point4)

# Dict to Unpacking
temp_dict = {'x': 75, 'y': 55}

# Tuple to Unpacking
temp_tuple = (10, 20)

# Create Object
p1 = Point1(x=10, y=35)
p2 = Point2(20, 40)
p3 = Point3(45, y=20)
p4 = Point4(10, 20, 30, 40)
p5 = Point1(**temp_dict)  # ** -> unpacking dictionary
p6 = Point1(*temp_tuple)  # * -> unpacking tuple

print()
print(p1)
print(p2)
print(p3)
print(p4)  # 중복어와 예약어는 자동으로 리네임됨, rename=False면 에러가 남
print(p5)
print(p6)

print(p1[0] + p2[1])
print(p1.x + p2.y)

x, y = p3  # unpacking
print(x, y)

# named tuple method ===================================================================================================
temp = [52, 38]

# _make() : create new object based on list
p4 = Point1._make(temp)
print(p4)

# _fields: check field name
print(p1._fields, p2._fields, p3._fields)

# _asdict() : return OrderedDict
print(p1._asdict())

# Application ==========================================================================================================
# 4 classes (A, B, C, D) with 20 students each (1 ~ 20)

Classes = namedtuple('Classes', ['rank', 'number'])

# declare group list
numbers = [str(n) for n in range(1, 21)]
ranks = 'A B C D'.split(' ')

print(numbers)
print(ranks)

# List Comprehension
students = [Classes(rank, number) for rank in ranks for number in numbers]
print(len(students))
print(students)

students2 = [Classes(rank, number)
             for rank in 'A B C D'.split()
             for number in [str(n)
                            for n in range(1, 21)]]

for s in students2:
    print(s)
