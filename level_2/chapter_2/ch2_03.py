# chapter 2 - 03
# 객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지, 유지보수 용이, 대형 프로젝트
# 규모가 큰 프로젝트(프로그램) -> 함수 중심 -> 데이터가 방대해짐 -> 복잡
# 클래스 중심 -> 데이터 중심 -> 객체로 관리

class Car:
    """
    Car class
    Author: Choi
    Date:2023.01.09
    Description: Class, Static, Instance Method
    """
    # Class Variable (referred by all instances)
    price_per_raise = 1.0

    def __init__(self, company, details):
        self._company = company
        # self.car_count = 10
        self._details = details

    def __str__(self):  # user
        return 'str : {} - {}'.format(self._company, self._details)

    def __repr__(self):  # engineer
        return 'repr : {} - {}'.format(self._company, self._details)

    # Instance Method
    # Self: 객체의 고유한 속성 값을 사용
    def detail_info(self):
        print('Current ID : {}'.format(id(self)))
        print('Car Detail Info: {} ${}'.format(self._company, self._details.get('price')))

    # Instance Method
    def get_price_before(self):
        return 'Before Car Price: company - {}, price -${}'.format(self._company, self._details.get('price'))

    # Instance Method
    def get_price_after(self):
        return 'After Car Price: company - {}, price -${}'.format(self._company,
                                                                  self._details.get('price') * Car.price_per_raise)

    # Class Method
    @classmethod
    def raise_price(cls, per):  # cls = ex. Car class
        if per <= 1:
            print('Please Enter 1 or More')
            return
        cls.price_per_raise = per
        print('Succeed!')

    # Static Method
    @staticmethod
    def is_bmw(inst):
        if inst._company == "BMW":
            return "OK! This car is {}.".format(inst._company)
        return "Sorry! This car is not BMW. It's {}.".format(inst._company)


# meaning of self
car1 = Car('Ferrari', {'color': 'White', 'horsepower': 400, 'price': 8000})
car2 = Car('BMW', {'color': 'Black', 'horsepower': 270, 'price': 5000})
car3 = Car('Audi', {'color': 'Silver', 'horsepower': 300, 'price': 6000})

# whole info
car1.detail_info()
car2.detail_info()
print()

# price info (direct access)
print(car1._details.get('price'))  # not a good way
print(car2._details.get('price'))
print()

# price info (before)
print(car1.get_price_before())
print(car2.get_price_before())
print()

# raise price (class method not used)
Car.price_per_raise = 1.4
print(car1.get_price_after())
print(car2.get_price_after())
print()

# raise price (class method used)
Car.raise_price(1)
Car.raise_price(1.6)
print(car1.get_price_after())
print(car2.get_price_after())
print()

# called by instance (Static)
print(car1.is_bmw(car1))
print(car2.is_bmw(car2))
print(car2.is_bmw(car3))
print()

# called by Class (Static)
print(Car.is_bmw(car1))
print(Car.is_bmw(car2))
print(Car.is_bmw(car3))

print("--------------------------------------------------")
