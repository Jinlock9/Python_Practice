# Chapter 06-03 ========================================================================================================
# 병행성 (Concurrency) : one computer performs multitasks at once -> 단일 프로그램 안에서 여러 일을 쉽게 해결
# 병렬성 (Parallelism) : multi computers perform a single task together at once -> speed
# Coroutine : single thread, stack 을 기반으로 동작하는 비동기 작업 ----------------------------------------------------------
# Thread : os 에서 관리, cpu core 에서 실시간 (또는 시분할) 비동기 작업 -> multi thread
# yield, send : main <--> sub
# 코루틴 제어, 상태, 양방향 전송
# sub routine : call main routine -> perform at sub routine (control flow)
# coroutine : stop while running routine -> 동시성 프로그래밍
# coroutine : thread 에 비해 오버헤드 감소
# thread : single thread -> multi thread -> complicate because of shared resource -> possibility of dead-lock
#        : context switching cost occurs, possibility of consuming resource increase
# def -> async, yield -> await
# ======================================================================================================================

from inspect import getgeneratorstate


# Coroutine Ex1 ========================================================================================================
def coroutine1():
    print('>>> coroutine started')  # subroutine 1
    i = yield
    print('>>> coroutine received : {}'.format(i))  # subroutine 2


# main routine
# declare as generator
cr1 = coroutine1()

print(cr1, type(cr1))
try:
    # yield 지점까지 subroutine 수행
    next(cr1)
    # next(cr1)  # 기본 전달값 None
    # 값 전송
    cr1.send(100)  # send 에게 next 의 기능도 있음
except StopIteration:
    pass
# ======================================================================================================================

print()
print("=" * 118)
print()


# Coroutine Ex2 ========================================================================================================
# GEN_CREATED : 처음 대기 상태
# GEN_RUNNING : 실행 상태
# GEN_SUSPENDED : yield 대기 상태
# GEN_CLOSED : 실행 완료 상태
def coroutine2(x):
    print('>>> coroutine started : {}'.format(x))
    y = yield x
    print('>>> coroutine received : {}'.format(y))
    z = yield x + y
    print('>>> coroutine received : {}'.format(z))


# [main to sub] = yield [sub to main]
# [sub to main] 은 print 문으로 확인

# from inspect import getgeneratorstate

cr2 = coroutine2(10)

print(getgeneratorstate(cr2))
try:
    print(next(cr2))
    print(getgeneratorstate(cr2))
    print(cr2.send(100))
    print(getgeneratorstate(cr2))
    cr2.send(100)
except StopIteration:
    pass
print(getgeneratorstate(cr2))
# ======================================================================================================================

print()
print("=" * 118)
print()


# Coroutine Ex3 ========================================================================================================
# StopIteration 자동 처리 (3.5 이상 -> await)
# 중첩 coroutine 처리
# ----------------------------------------------------------------------------------------------------------------------
def generator1():
    for x in 'AB':
        yield x
    for y in range(1, 4):
        yield y


t1 = generator1()

try:
    print(next(t1))
    print(next(t1))
    print(next(t1))
    print(next(t1))
    print(next(t1))
    # print(next(t1))
except StopIteration:
    pass

print()

# ----------------------------------------------------------------------------------------------------------------------
t2 = generator1()
print(list(t2))

print()


# ----------------------------------------------------------------------------------------------------------------------
def generator2():
    yield from 'AB'
    yield from range(1, 4)


t3 = generator2()
try:
    print(next(t3))
    print(next(t3))
    print(next(t3))
    print(next(t3))
    print(next(t3))
    # print(next(t1))
except StopIteration:
    pass
# ======================================================================================================================
