# Chapter 04-04 ========================================================================================================
# Sequence Type ========================================================================================================
# Hash Table: 적은 리소스로 많은 데이터를 효율적으로 관리
# Dict -> Key 중복 허용 x, Set -> 중복 허용 x
# ======================================================================================================================

from types import MappingProxyType
from dis import dis
from unicodedata import name

# Dict Advanced ========================================================================================================
# Immutable Dict -------------------------------------------------------------------------------------------------------
# from types import MappingProxyType
d = {'key1': 'value1'}

# Read Only
d_frozen = MappingProxyType(d)  # cannot modify

print(d, id(d))
# print(hash(d))
print(d_frozen, id(d_frozen))
# print(hash(d_frozen))

# immutable
try:
    d_frozen['key2'] = 'value2'
except TypeError:
    print('cannot modify')

# mutable
d['key2'] = 'value2'
print(d)
# ======================================================================================================================

print()
print()

# Set ==================================================================================================================
s1 = {'Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'}  # set
s2 = set(['Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'])
s3 = {3}
s4 = set()  # Not {}
s5 = frozenset({'Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'})

s1.add('Melon')
print(s1)
print()

# cannot add
# s5.add('Melon')  <- Read Only

print(s1, type(s1))
print(s2, type(s2))
print(s3, type(s3))
print(s4, type(s4))
print(s5, type(s5))

print()

# 선언 최적화 ------------------------------------------------------------------------------------------------------------
# Byte Code -> Execute byte code by Python Interpreter
# from dis import dis
print('-------------------------------------------')
print(dis('{10}'))
print('-------------------------------------------')
print(dis('set([10])'))  # more steps

print()

# 지능형 집합 (Comprehending Set) ----------------------------------------------------------------------------------------
print('-------------------------------------------')
# from unicodedata import name
print({name(chr(i), '') for i in range(0, 256)})
# ======================================================================================================================
