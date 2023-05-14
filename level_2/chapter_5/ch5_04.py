# Chapter 05-02 ========================================================================================================
# First Class Function 일급 함수 (일급 객체) ==============================================================================
# Closure Basic --------------------------------------------------------------------------------------------------------
# Decorator
# Advantages:
# 1. remove duplicates, clean code, 공통 함수 작성
# 2. 로깅, 프레임워크, 유효성 체크 -> 공통 기능
# 3. 조합해서 사용 용이
# Disadvantages:
# 1. 가독성 감소
# 2. 특정 기능에 한정된 함수는 -> 단일 함수로 작성하는 것이 유리
# 3. 디버깅 불편
# ======================================================================================================================

import time


# Decorator Practice ===================================================================================================
# import time

def perf_clock(func):
    def perf_clocked(*args):
        # 함수 시작 시간
        st = time.perf_counter()
        # 함수 실행
        result = func(*args)
        # 함수 종료 시간
        et = time.perf_counter() - st
        # 실행 함수명
        name = func.__name__
        # 함수 매개변수
        arg_str = ','.join(repr(arg) for arg in args)
        # 결과 출력
        print('[%0.5fs] %s(%s) -> %r' % (et, name, arg_str, result))
        return result

    return perf_clocked


def time_func1(seconds):
    time.sleep(seconds)


def sum_func1(*numbers):
    return sum(numbers)


# not use as decorator -------------------------------------------------------------------------------------------------
none_deco1 = perf_clock(time_func1)
none_deco2 = perf_clock(sum_func1)

print(none_deco1, none_deco1.__code__.co_freevars)
print(none_deco2, none_deco2.__code__.co_freevars)

print()

print('-' * 10, 'Called None Decorator -> time_func1')
none_deco1(1.5)
print('-' * 10, 'Called None Decorator -> sum_func1')
none_deco2(10, 20, 30, 40, 50)

print()
print()


# use as Decorator -----------------------------------------------------------------------------------------------------
@perf_clock
def time_func2(seconds):
    time.sleep(seconds)


@perf_clock
def sum_func2(*numbers):
    return sum(numbers)


print('-' * 10, 'Called Decorator -> time_func2')
time_func2(1.5)
print('-' * 10, 'Called Decorator -> sum_func2')
sum_func2(10, 20, 30, 40, 50)
