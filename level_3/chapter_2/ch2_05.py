"""
Chapter 2 - Python Advanced (2) : Method Overriding
Keywords : overloading, OOP, multiple dispatch
"""
# imports ==============================================================================================================
from multipledispatch import dispatch
# ======================================================================================================================
"""  # =================================================================================================================
[ Effect of Method OverLoading ]
1. 동일 메소드 재정의
2. 네이밍 기능 예측
3. 코드 절약, 가독성 향상
4. 메소드 파라미터 기반 호출 방식
"""  # =================================================================================================================


# Ex 1 =================================================================================================================
# 동일 이름 메소드 사용 예제
# 동적 타입 검사 -> 런타임에 실행 (타입 에러가 실행 시에 발견)
class SampleA:
    def add(self, x, y):
        return x + y

    def add(self, x, y, z):
        return x + y + z

    # !! able to resolve by using packing (integer)
    # def add(self, *args):
    #     return sum(args)


a = SampleA()
# print("Ex 1 > ", a.add(2, 3)) -> TypeError: SampleA.add() missing 1 required positional argument: 'z'
print("Ex 1 > ", dir(a))
print()
# ======================================================================================================================


# Ex 2 =================================================================================================================
# 동일 이름 메소드 사용 예제
# 자료형에 따른 분기 처리
class SampleB:
    def add(self, datatype, *args):
        if datatype == 'int':
            return sum(args)
        if datatype == 'str':
            return ' '.join([x for x in args])


b = SampleB()
# integer
print("Ex 2 > ", b.add('int', 5, 6))
# string
print("Ex 2 > ", b.add('str', 'Hi', 'Python'))
print()
# ======================================================================================================================


# Ex 3 =================================================================================================================
# Method Overloading using multipledispatch package
# from multipledispatch import dispatch
class SampleC:
    @staticmethod
    @dispatch(int, int)
    def product(x, y):
        return x * y

    @staticmethod
    @dispatch(int, int, int)
    def product(x, y, z):
        return x * y * z

    @staticmethod
    @dispatch(float, float, float)
    def product(x, y, z):
        return x * y * z


c = SampleC()
print("Ex 3 > ", c.product(5, 6))
print("Ex 3 > ", c.product(5, 6, 7))
print("Ex 3 > ", c.product(5.5, 6.5, 7.5))
