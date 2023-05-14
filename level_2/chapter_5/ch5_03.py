# Chapter 05-02 ========================================================================================================
# First Class Function 일급 함수 (일급 객체) ==============================================================================
# Closure Basic --------------------------------------------------------------------------------------------------------
# 외부에서 호출된 함수의 변수값, 상태 (reference) 복사 후 저장 -> 후에 접근 (access) 가능
# ======================================================================================================================

# Using Closure ========================================================================================================
def closure_ex1():
    # Free variable : declare outside the function one is going to use
    # Closure area
    series = []

    def averager(v):
        series.append(v)
        print('inner >>> {} / {}'.format(series, len(series)))
        return sum(series) / len(series)

    return averager


avg_closure1 = closure_ex1()
print(avg_closure1)
print(avg_closure1(10))
print(avg_closure1(20))
print(avg_closure1(30))
# ======================================================================================================================

print()
print("================================================================================================================"
      "======")
print()

# function inspection ==================================================================================================
print(dir(avg_closure1))
print()
print(dir(avg_closure1.__code__))
print()
print(avg_closure1.__code__.co_freevars)
print(avg_closure1.__closure__[0].cell_contents)
# ======================================================================================================================

print()
print("================================================================================================================"
      "======")
print()


# Wrong Usage of Closure ===============================================================================================
def closure_ex2():
    # Free variables
    cnt = 0
    total = 0

    def averager(v):
        cnt += 1
        total += v
        return total / cnt

    return averager


avg_closure2 = closure_ex2()
# print(avg_closure2(10))  # ERROR!!!!!


# Fixation -------------------------------------------------------------------------------------------------------------
def closure_ex3():
    # Free variables
    cnt = 0
    total = 0

    def averager(v):
        nonlocal cnt, total
        cnt += 1
        total += v
        return total / cnt

    return averager


avg_closure3 = closure_ex3()
print(avg_closure3(15))
print(avg_closure3(35))
print(avg_closure3(55))
# ======================================================================================================================
