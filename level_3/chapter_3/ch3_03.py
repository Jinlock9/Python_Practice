"""
Chapter 3 - Python Advanced (3) : Meta Class (3)
Keywords : Type inheritance, Custom metaclass
"""
# imports ==============================================================================================================
# ======================================================================================================================
"""  # =================================================================================================================
[ Meta Class ]
1. type class 상속
2. metaclass 속성 사용
3. custom metaclass 생성
    - intercepting class creation (intercept)
    - modifying class
    - improve class
    - return modified class
"""  # =================================================================================================================


# Ex 1 =================================================================================================================
# custom meta class 생성 예제 (type 상속 x)
def cus_mul(self, d):
    for i in range(len(self)):
        self[i] = self[i] * d


def cus_replace(self, old, new):
    while old in self:
        self[self.index(old)] = new


# list 를 상속 받음, 메소드 2개 추가
CustomList1 = type(
    'CustomList1',
    (list,),
    {
        'desc': 'Custom List 1',
        'cus_mul': cus_mul,
        'cus_replace': cus_replace
    }
)

c1 = CustomList1([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
c1.cus_mul(15)
c1.cus_replace(30, "oops")

print("Ex 1 > ", c1)
print("Ex 1 > ", c1.desc)
# print("Ex 1 > ", dir(c1))
print()
# ======================================================================================================================


# Ex 2 =================================================================================================================
# Creating Custom Meta Class Examples (with inheriting Type)
# new -> init -> call
class CustomListMeta(type):
    # 클래스 인스턴스 생성 (메모리 초기화)
    def __new__(mcs, name, bases, namespace):
        print("__new__ -> ", mcs, name, bases, namespace)
        namespace['desc'] = 'Custom List 2'
        namespace['cus_mul'] = cus_mul
        namespace['cus_replace'] = cus_replace
        return type.__new__(mcs, name, bases, namespace)

    # 생성 된 인스턴스 초기화
    def __init__(cls, object_or_name, bases, dicts):
        print("__init__ -> ", cls, object_or_name, bases, dicts)
        super().__init__(object_or_name, bases, dicts)

    # 인스턴스 실행
    def __call__(cls, *args, **kwargs):
        print("__call__ -> ", *args, **kwargs)
        return super().__call__(*args, **kwargs)


print("Ex 2 > ")
CustomList2 = CustomListMeta(
    'Custom List 2',
    (list, ),
    {}
)

c2 = CustomList2([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
c2.cus_mul(15)
c2.cus_replace(30, 'oops')

print("Ex 2 > ", c2)
print("Ex 2 > ", c2.desc)
# print("Ex 2 > ", dir(c2))

# 상속 확인
print("Ex 2 > ", CustomList2.__mro__)
print()
# ======================================================================================================================
