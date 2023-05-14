"""
Chapter 3 - Python Advanced (3) : Descriptor (1)
Keywords : descriptor, set, get, del, property
"""
# imports ==============================================================================================================
# ======================================================================================================================
"""  # =================================================================================================================
[ Descriptor ]
1. 객체에서 서로 다른 객체를 속성 값으로 가지는 것
2. Read, Write, Delete 등을 미리 정의 가능
3. data descriptor (set, del), non-data descriptor (get)
4. 읽기 전용 객체 생성 장점, 클래스를 의도하는 방향으로 생성 가능
"""  # =================================================================================================================


# Ex 1 =================================================================================================================
# Basic Descriptor Example
class DescriptorEx1:
    def __init__(self, name='Default'):
        self.name = name

    def __get__(self, instance, owner):
        return "Get method Called. -> self : {}, instance : {}, instance type : {}, name : {}".format(self, instance,
                                                                                                       owner, self.name)

    def __set__(self, instance, value):
        print("Set method called.")
        if isinstance(value, str):
            self.name = value
        else:
            raise TypeError("Name should be string")

    def __delete__(self, instance):
        print("Delete method called.")
        self.name = None


class Sample1:
    name = DescriptorEx1()


s1 = Sample1()

# Call __set__ method
s1.name = 'Descriptor Test 1'
# s1.name = 10  # TypeError!

# check attr
# Call __get__ method
print("Ex 1 > ", s1.name)

# Call __delete__ method
del s1.name
print("Ex 1 > ", s1.name)  # check
print()
# ======================================================================================================================


# Ex 2 =================================================================================================================
# Property 클래스 사용하여 Descriptor 직접 구현
# class property(fget=None, fset=None, fdel=None, doc=None)
class DescriptorEx2:
    def __init__(self, value="default"):
        self._name = value

    def getVal(self):
        return "Get method called. -> self : {}, name : {}".format(self, self._name)

    def setVal(self, value):
        print("Set method called.")
        if isinstance(value, str):
            self._name = value
        else:
            raise TypeError("Name should be string.")

    def delVal(self):
        print("Delete method called.")
        self._name = None

    name = property(getVal, setVal, delVal, "Property Method Example")


s2 = DescriptorEx2("Descriptor Test 2")

# check initial value
print("Ex 2 > ", s2.name)

# call setVal
s2.name = "Descriptor Test 2 Method."

# raise exception
# s2.name = 10  # TypeError!

# call getVal
print("Ex 2 > ", s2.name)

# call delVal
del s2.name
print("Ex 2 > ", s2.name)  # check

# check Doc
print("Ex 2 > ", DescriptorEx2.name.__doc__)
# ======================================================================================================================
