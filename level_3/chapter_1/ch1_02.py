"""
Chapter 1 - Python Advanced (1) : Lambda, Reduce, Map, Filter Functions
Keywords : lambda, map, filter, reduce
"""
# imports ==============================================================================================================
from functools import reduce
# ======================================================================================================================
"""  # =================================================================================================================
advantage of Lambda : 익명, 힙 영역 사용, 사용 후 즉시 소멸, python garbage collection (Count = 0)
normal function : saved in memory for reusing
Usually use Reduce, Map, Filter for Sequence-like Preprocessing
"""  # =================================================================================================================

# lambda ===============================================================================================================
# Ex 1 -----------------------------------------------------------------------------------------------------------------
cul = lambda a, b, c: a * b + c
print("Ex 1 > ", cul(10, 15, 20))
print()
# ======================================================================================================================

# map ==================================================================================================================
# Ex 2 -----------------------------------------------------------------------------------------------------------------
digits1 = [x * 10 for x in range(1, 11)]
print("Ex 2 > ", digits1)

# map(func, iter)
result = list(map(lambda i: i ** 2, digits1))
print("Ex 2 > ", result)


# module
def also_square(nums):
    def double(x):
        return x ** 2
    return map(double, nums)


print("Ex 2 > ", list(also_square(digits1)))
print()
# ======================================================================================================================

# filter ===============================================================================================================
# Ex 3 -----------------------------------------------------------------------------------------------------------------
digits2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = list(filter(lambda x: x % 2 == 0, digits2))

print("Ex 3 > ", result)


# module
def also_evens(nums):
    def is_even(x):
        return x % 2 == 0
    return filter(is_even, nums)


print("Ex 3 > ", list(also_evens(digits2)))
print()
# ======================================================================================================================

# reduce ===============================================================================================================
# Ex 4 -----------------------------------------------------------------------------------------------------------------
# from functools import reduce
digits3 = [x for x in range(1, 101)]
result = reduce(lambda x, y: x + y, digits3)
print("Ex 4 > ", result)


def also_add(nums):
    def add(x, y):
        return x + y
    return reduce(add, nums)


print("Ex 4 > ", also_add(digits3))
# ======================================================================================================================
