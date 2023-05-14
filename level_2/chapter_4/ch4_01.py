# Chapter 04-01 ========================================================================================================
# Sequence Type ========================================================================================================
# - Container: 서로 다른 자료형 - list, tuple, collections.deque, etc
# - Flat: 단일 자료형 - str, bytes, bytearray, array.array, memoryview
# ----------------------------------------------------------------------------------------------------------------------
# - Mutable: list, bytearray, array.array, memoryview, deque
# - Immutable: tuple, str, bytes
# ======================================================================================================================

import array

# Advanced List and Tuple ==============================================================================================
# Comprehending List (지능형 리스트) -------------------------------------------------------------------------------------
chars = '+_)(*&^%$#@!'
code_list1 = []

# unicode lists
for s in chars:
    code_list1.append(ord(s))

print(code_list1)

# comprehending list (little faster)
code_list2 = [ord(s) for s in chars]
print(code_list2)

# Comprehending Lists + Map, Filter ------------------------------------------------------------------------------------
code_list3 = [ord(s) for s in chars if ord(s) > 40]
print(code_list3)
code_list4 = list(filter(lambda x: x > 40, map(ord, chars)))
print(code_list4)

# print all
print(code_list1)
print(code_list2)
print(code_list3)
print(code_list4)
print([chr(s) for s in code_list1])
print([chr(s) for s in code_list2])
print([chr(s) for s in code_list3])
print([chr(s) for s in code_list4])
# ======================================================================================================================

print()
print()

# Generator ============================================================================================================
# Kind of powerful iterator
# import array

# Generator : 한 번에 한 개의 항목을 생성 (메모리 유지 X) --------------------------------------------------------------------
tuple_generator = (ord(s) for s in chars)
print(tuple_generator)
print(type(tuple_generator))
print(next(tuple_generator))
print(next(tuple_generator))
print(next(tuple_generator))
print(next(tuple_generator))
print(next(tuple_generator))
print(next(tuple_generator))
print(next(tuple_generator))
print(next(tuple_generator))
print(next(tuple_generator))
print(next(tuple_generator))
print(next(tuple_generator))
print(next(tuple_generator))

print()

# array with generator -------------------------------------------------------------------------------------------------
array_generator = array.array('I', (ord(s) for s in chars))
print(array_generator)
print(type(array_generator))
print(array_generator.tolist())

print()

# generator example ----------------------------------------------------------------------------------------------------
print(('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1, 21)))

for s in ('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1, 21)):
    print(s)
# ======================================================================================================================

print()

# Things to beware of list =============================================================================================
marks1 = [['~'] * 3 for _ in range(4)]  # _ : 반복은 할건데 후에 사용 안할 때
print(marks1)
marks2 = [['~'] * 3] * 4
print(marks2)

marks1[0][1] = 'X'
marks2[0][1] = 'X'
print(marks1)
print(marks2)

# proof
print([id(i) for i in marks1])  # 4 different list
print([id(i) for i in marks2])  # 4 same list
