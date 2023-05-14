# chapter 2 - 01
# 객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지, 유지보수 용이, 대형 프로젝트
# 규모가 큰 프로젝트(프로그램) -> 함수 중심 -> 데이터가 방대해짐 -> 복잡
# 클래스 중심 -> 데이터 중심 -> 객체로 관리

# general coding
# car1
car_company_1 = 'Ferrari'
car_detail_1 = [
    {'color': 'White'},
    {'horsepower': 400},
    {'price': 8000}
]

# car2
car_company_2 = 'BMW'
car_detail_2 = [
    {'color': 'Black'},
    {'horsepower': 270},
    {'price': 5000}
]

# car3
car_company_3 = 'Audi'
car_detail_3 = [
    {'color': 'Silver'},
    {'horsepower': 300},
    {'price': 6000}
]

# list
# inconvenient to manage, delete
# possible to make mistake when accessing to data with index
car_company_list = ['Ferrari', 'BMW', 'Audi']
car_detail_list = [
    {'color': 'White', 'horsepower': 400, 'price': 8000},
    {'color': 'Black', 'horsepower': 270, 'price': 5000},
    {'color': 'Silver', 'horsepower': 300, 'price': 6000}
]

del car_company_list[1]
del car_detail_list[1]

print(car_company_list)
print(car_detail_list)

print()
print()

# dictionary
# 코드 반복 지속, duplication problem (key), 키 조회 예외 처리 등
car_dicts = [
    {'car_company': 'Ferrari', 'car_detail': {'color': 'White', 'horsepower': 400, 'price': 8000}},
    {'car_company': 'BMW', 'car_detail': {'color': 'Black', 'horsepower': 270, 'price': 5000}},
    {'car_company': 'Audi', 'car_detail': {'color': 'Silver', 'horsepower': 300, 'price': 6000}}
]

del car_dicts[1]
print(car_dicts)

print()
print()


# Class
# 구조 설계 후 재사용성 증가, 코드 반복 최소화, 메소드 활용
class Car:
    def __init__(self, company, details):
        self._company = company
        self._details = details

    def __str__(self):  # user
        return 'str : {} - {}'.format(self._company, self._details)

    def __repr__(self):  # engineer
        return 'repr : {} - {}'.format(self._company, self._details)


car1 = Car('Ferrari', {'color': 'White', 'horsepower': 400, 'price': 8000})
car2 = Car('BMW', {'color': 'Black', 'horsepower': 270, 'price': 5000})
car3 = Car('Audi', {'color': 'Silver', 'horsepower': 300, 'price': 6000})
print(car1)
print(car2)
print(car3)

print(car1.__dict__)
print(car2.__dict__)
print(car3.__dict__)

# print(dir(car1))

print()
print()

# list (__repr__)
car_list = [car1, car2, car3]
print(car_list)

print()
print()

# 반복(__str__)
for x in car_list:
    print(x)
    print(repr(x))
