"""
Chapter 2 - Python Advanced (2) : Property (2) - Getter & Setter
Keywords : @Property
"""
# imports ==============================================================================================================
# ======================================================================================================================
"""  # =================================================================================================================
- Advantage of Property
    1. Pythonic Code
    2. 변수 제약 설정
    3. Getter, Setter 효과 동등 (코드 일관성)
        - 캡슐화 - 유효성 검사 기능 추가 용이
        - 대체 표현 (속성 노출, 내부의 표현 은닉 가능)
        - 속성의 수명 및 메모리 관리 용이
        - 디버깅 용이
        - Getter, Setter 작동에 대해 설계된 여러 library (open source) 상호 운용성 증가
"""  # =================================================================================================================


# Ex 1 =================================================================================================================
# Property 활용, Getter & Setter 작성
class SampleA:
    def __init__(self):
        self.x = 0
        self.__y = 0  # private

    # STANDARD *************************************
    @property
    def y(self):
        print("Get method called")
        return self.__y

    @y.setter
    def y(self, value):
        print("Set method called")
        self.__y = value

    @y.deleter
    def y(self):
        print("Delete method called")
        del self.__y
    # **********************************************


a = SampleA()
a.x = 1
a.y = 2

print("Ex 1 > x : {}".format(a.x))
print("Ex 1 > y : {}".format(a.y))

# deleter
# del a.y  # deletes _SampleA__y
print("Ex 1 > ", dir(a))
print()
# ======================================================================================================================


# Ex 2 =================================================================================================================
# Property 활용 제약 조건 추가
class SampleB:
    def __init__(self):
        self.x = 0
        self.__y = 0  # private

    @property
    def y(self):
        # print("Get method called")
        return self.__y

    @y.setter
    def y(self, value):
        # print("Set method called")
        if value < 0:
            raise ValueError('input integer larger than 0')
        self.__y = value

    @y.deleter
    def y(self):
        # print("Delete method called")
        del self.__y


b = SampleB()
b.x = 1
b.y = 10

# b.y = -5  # ValueError

print("Ex 2 > x : {}".format(b.x))
print("Ex 2 > y : {}".format(b.y))
# ======================================================================================================================
