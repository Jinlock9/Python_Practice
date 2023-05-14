# chapter 2 - 02
# 객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지, 유지보수 용이, 대형 프로젝트
# 규모가 큰 프로젝트(프로그램) -> 함수 중심 -> 데이터가 방대해짐 -> 복잡
# 클래스 중심 -> 데이터 중심 -> 객체로 관리

class Car:
    """
    Car class
    Author: Choi
    Date:2023.01.09
    """
    # Class Variable (referred by all instances)
    car_count = 0

    def __init__(self, company, details):
        self._company = company
        self.car_count = 10
        self._details = details
        Car.car_count += 1

    def __str__(self):  # user
        return 'str : {} - {}'.format(self._company, self._details)

    def __repr__(self):  # engineer
        return 'repr : {} - {}'.format(self._company, self._details)

    def __del__(self):
        print('Instance Deleted')
        Car.car_count -= 1

    def detail_info(self):
        print('Current ID : {}'.format(id(self)))
        print('Car Detail Info: {} ${}'.format(self._company, self._details.get('price')))


# meaning of self
car1 = Car('Ferrari', {'color': 'White', 'horsepower': 400, 'price': 8000})
car2 = Car('BMW', {'color': 'Black', 'horsepower': 270, 'price': 5000})
car3 = Car('Audi', {'color': 'Silver', 'horsepower': 300, 'price': 6000})

# check ID
print(id(car1))
print(id(car2))
print(id(car3))

print(car1._company == car2._company)
print(car1 is car2)

# dir & __dict__
print(dir(car1))
print(dir(car2))

print()
print()

print(car1.car_count)
print(car2.car_count)
print(car1.__dict__)
print(car2.__dict__)

# Doctring
print(Car.__doc__)
print()

# execute
car1.detail_info()
Car.detail_info(car1)
car2.detail_info()
Car.detail_info(car2)

# compare
print(car1.__class__, car2.__class__)
print(id(car1.__class__) == id(car2.__class__) == id(car3.__class__))

# Error
# Car.detail_info()

# share
print(car1.car_count)
print(car2.car_count)
print(car1.__dict__)
print(car2.__dict__)
print(dir(car1))

# access
print(car1.car_count)
print(Car.car_count)

print()

del car2
# check deletion
print(Car.car_count)
print(car1.car_count)

# Instance Name Space에 없으면 상위에서 검색
# 즉, 동일한 이름으로 변수 생성 가능(인스턴스 검색 후 -> 상위(클래스 변수, 부모 클래스 변수)

print("---------------------------------")
