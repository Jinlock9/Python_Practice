"""
Chapter 2 - Python Advanced (2) : Method Overriding
Keywords : Overriding, OOP, Polymorphism
"""
# imports ==============================================================================================================
import datetime
# ======================================================================================================================
"""  # =================================================================================================================
[ Effect of Method Overriding ]
1. Able to call super class from sub class
2. Able to use function after redefine it
3. 부모 클래스의 메소드를 추상화한 후 사용가능 (구조적 접근)
4. 확장 가능, Polymorphism (다양한 방식으로 동작)
5. 가독성 증가, 오류 가능성 감소, 메소드 이름 절약, 유지 보수성 증가 등
"""  # =================================================================================================================


# Ex 1 =================================================================================================================
# Basic Overriding Example
class ParentEx1:
    def __init__(self):
        self.value = 5

    def get_value(self):
        return self.value


class ChildEx1(ParentEx1):
    pass


c1 = ChildEx1()
p1 = ParentEx1()

# Call Super class method
print("Ex 1 > ", c1.get_value())

# Attributes of c1
print("EX 1 > ", dir(c1))

print("Ex 1 > ", dir(ParentEx1))
print("Ex 1 > ", dir(ChildEx1))

print("Ex 1 > ", ParentEx1.__dict__)
print("Ex 1 > ", ChildEx1.__dict__)
print()
# ======================================================================================================================


# Ex 2 =================================================================================================================
# 기본 Overriding 메소드 재정의
class ParentEx2:
    def __init__(self):
        self.value = 5

    def get_value(self):
        return self.value


class ChildEx2(ParentEx2):
    def get_value(self):
        return self.value * 10


c2 = ChildEx2()

# Call subclass after redefine
print("Ex 2 > ", c2.get_value())
print()
# ======================================================================================================================


# Ex 3 =================================================================================================================
# Overriding Polymorphism Example
# import datetime
class Logger:
    def log(self, msg):
        print(msg)


class TimeStampLogger(Logger):
    def log(self, msg):
        message = "{ts} {msg}".format(ts=datetime.datetime.now(), msg=msg)
        super(TimeStampLogger, self).log(message)  # option 1
        # super().log(message)  # option 2


class DateLogger(Logger):
    def log(self, msg):
        message = "{ts} {msg}".format(ts=datetime.datetime.now().strftime("%Y-%m-%d"), msg=msg)
        super(DateLogger, self).log(message)


logger = Logger()
time_logger = TimeStampLogger()
date_logger = DateLogger()

print("Ex 3 > ")
logger.log(": Logger Called")
print("Ex 3 > ")
time_logger.log(": Time Stamp Logger Called")
print("Ex 3 > ")
date_logger.log(": Date Logger Called")
# ======================================================================================================================
