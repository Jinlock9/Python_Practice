# Chapter 06-01 ========================================================================================================
# 병행성 (Concurrency) ==================================================================================================
# Iterator, Generator --------------------------------------------------------------------------------------------------
# ======================================================================================================================

from collections import abc

# Python Iterable Types ================================================================================================
# - Collections, test file, List, Dict, Set, Tuple, unpacking, *args... : iterable

# 반복 가능한 이유? -> iter(x) 함수 호출 -----------------------------------------------------------------------------------
t = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(dir(t))  # __iter__
for c in t:
    print(c)

print()

# while ----------------------------------------------------------------------------------------------------------------
w = iter(t)
print(dir(w))  # __next__
"""
print(next(w))
print(next(w))
print(next(w))
"""

while True:
    try:
        print(next(w))
    except StopIteration:
        break
print()

# 반복형 확인 ------------------------------------------------------------------------------------------------------------
# from collections import abc
# print(dir(t))
print(hasattr(t, '__iter__'))
print(isinstance(t, abc.Iterable))
# ======================================================================================================================

print()
print("=" * 118)
print()


# Class ================================================================================================================
# next -----------------------------------------------------------------------------------------------------------------
class WordSplitter:
    def __init__(self, text):
        self._idx = 0
        self._text = text.split(' ')

    def __next__(self):
        # print('Called __next__')
        try:
            word = self._text[self._idx]
        except IndexError:
            # raise StopIteration('Stopped Iteration.')
            word = 'ERROR: Stop Iteration.'
        self._idx += 1
        return word

    def __repr__(self):
        return 'WordSplitter(%s)' % self._text


wi = WordSplitter('Do today what you could do tomorrow')
print(wi)
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print()


# generator ------------------------------------------------------------------------------------------------------------
# 1. 지능형 리스트, 딕셔너리, 집합 -> 데이터 양 증가 후 메모리 사용량 증가 -> generator 사용 권장
# 2. 단위 실행 가능한 Coroutine 구현과 연동
# 3. 작은 메모리 조각 사용
class WordSplitGenerator:
    def __init__(self, text):
        self._text = text.split(' ')

    def __iter__(self):
        for word in self._text:
            yield word  # Generator
        return

    def __repr__(self):
        return 'WordSplitGenerator(%s)' % self._text


wg = WordSplitGenerator('Do today what you could do tomorrow')
wt = iter(wg)
print(wt, wg)

print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
# print(next(wt))  # Stop Iteration
# ======================================================================================================================

print()
print("=" * 118)
print()
