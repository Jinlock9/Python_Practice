# Chapter 04-02 ========================================================================================================
# Sequence Type ========================================================================================================
# - Container: 서로 다른 자료형 - list, tuple, collections.deque, etc
# - Flat: 단일 자료형 - str, bytes, bytearray, array.array, memoryview
# ----------------------------------------------------------------------------------------------------------------------
# - Mutable: list, bytearray, array.array, memoryview, deque
# - Immutable: tuple, str, bytes
# ======================================================================================================================

# Tuple Advanced =======================================================================================================
# Unpacking ------------------------------------------------------------------------------------------------------------

# a, b = b, a
print(divmod(100, 9))
print(divmod(*(100, 9)))
print(*(divmod(100, 9)))

print()

x, y, *rest = range(10)
print(x, y, rest)
x, y, *rest = range(2)
print(x, y, rest)
x, y, *rest = 1, 2, 3, 4, 5
print(x, y, rest)
# ======================================================================================================================

print()
print()

# Mutable (가변) vs. Immutable (불변) ====================================================================================
l = (15, 20, 25)
m = [15, 20, 25]
print(l, id(l))
print(m, id(m))

l = l * 2
m = m * 2
print(l, id(l))
print(m, id(m))

l *= 2
m *= 2
print(l, id(l))  # id of immutable tuple keep changing
print(m, id(m))  # same id -> since list is mutable

# ======================================================================================================================

print()
print()

# Sort vs. Sorted ======================================================================================================
# reverse, key = len, key=str.Lower, key=func...

# sorted : 정렬 후 새로운 객체로 반환 (원본 수정 x) --------------------------------------------------------------------------
f_list = ['orange', ' apple', 'mango', 'papaya', 'lemon', 'strawberry', 'coconut']
print('sorted - ', sorted(f_list))
print('sorted - ', sorted(f_list, reverse=True))
print('sorted - ', sorted(f_list, key=len))  # according to length of word
print('sorted - ', sorted(f_list, key=lambda _: _[-1]))
print('sorted - ', sorted(f_list, key=lambda _: _[-1], reverse=True))
print('original - ', f_list)

print()

# sort: 정렬 후 객체를 직접 변경 (원본 수정 o) -------------------------------------------------------------------------------
# 반환 값 확인 (None)
print('sort - ', f_list.sort(), f_list)
print('sort - ', f_list.sort(reverse=True), f_list)
print('sort - ', f_list.sort(key=len), f_list)
print('sort - ', f_list.sort(key=lambda _: _[-1]), f_list)
print('sort - ', f_list.sort(key=lambda _: _[-1], reverse=True), f_list)
# ======================================================================================================================

# List vs Array ========================================================================================================
# 리스트 기반: 융통성, 다양한 자료형, 범용적 사용 - list
# 숫자 기반: 배열(리스트와 거의 호한) - array
# ======================================================================================================================
