# Chapter 05-01 ========================================================================================================
# First Class Function 일급 함수 (일급 객체) ==============================================================================
# 파이썬 함수 특징 --------------------------------------------------------------------------------------------------------
# 1. 런타임 초기화
# 2. 변수 할당 가능
# 3. 함수 인수 전달 가능
# 4. 함수 결과 반환 가능 (return)
# ======================================================================================================================

from functools import reduce, partial
from operator import add, mul


# === Function Object ==================================================================================================
def factorial(n):
    """Factorial Function -> n : int"""
    if n == 1:  # n < 2
        return 1
    return n * factorial(n - 1)


class A:
    pass


print(factorial(5))
print(factorial.__doc__)
print(type(factorial), type(A))
print(dir(factorial))  # function, but considered as an object
print(set(sorted(dir(factorial))) - set(sorted(dir(A))))  # function's original attributes
print(factorial.__name__)
print(factorial.__code__)
# ======================================================================================================================

print()
print()

# === 변수 할당 ==========================================================================================================
var_func = factorial  # assign function to variable

print(var_func)
print(var_func(10))
print(list(map(var_func, range(1, 11))))
# ======================================================================================================================

print()
print()

# === 함수 인수 전달 및 함수로 결과 반환 -> 고위 함수 (Higher-order Function) =================================================
# --- map, filter ------------------------------------------------------------------------------------------------------
print(list(map(var_func, filter(lambda _: _ % 2, range(1, 6)))))
print([var_func(i) for i in range(1, 6) if i % 2])  # 5 % 2 = 1 = True
print()

# --- reduce -----------------------------------------------------------------------------------------------------------
# from functools import reduce
# from operator import add

print(reduce(add, range(1, 11)))
print(sum(range(1, 11)))  # faster, in this case
print()

# --- Lambda (익명 함수) -------------------------------------------------------------------------------------------------
# 가급적 주석 작성
# 가급적 함수 작성
# 일반 함수 형태로 Refactoring 권장
print(reduce(lambda x, t: x + t, range(1, 11)))
# ======================================================================================================================

print()
print()

# === Callable : 호출 연산자 -> check whether it can be called in the form of method =====================================
# 호출 가능 확인
print(callable(str), callable(A), callable(list), callable(var_func), callable(factorial), callable(3.14))
# ======================================================================================================================

print()
print()

# === Partial 사용법 : 인수 고정 -> 콜백 함수 사용 ==========================================================================
# from operator import mul
# from functools import partial

print(mul(10, 10))

# --- 인수 고정 ----------------------------------------------------------------------------------------------------------
five = partial(mul, 5)  # 5 * ?
print(five(10))

# 고정 추가
six = partial(five, 6)
print(six())
print([five(i) for i in range(1, 11)])
print(list(map(five, range(1, 11))))
# ======================================================================================================================
