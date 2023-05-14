# Chapter 06-02 ========================================================================================================
# 병행성 (Concurrency) : one computer performs multitasks at once -> 단일 프로그램 안에서 여러 일을 쉽게 해결
# 병렬성 (Parallelism) : multi computers perform a single task together at once -> speed
# ======================================================================================================================

import itertools


# Generator Ex1 ========================================================================================================
def generator_ex1():
    print('Start')
    yield 'A Point'  # 다음 일을 기억한 채 stop!
    print('Continue')
    yield 'B Point'  # return 의 역할도 함
    print('End')


temp = iter(generator_ex1())

print(temp)
print(next(temp))
print(next(temp))
# print(next(temp))

print()

for v in generator_ex1():
    print(v)
# ======================================================================================================================

print()
print("=" * 118)
print()

# Generator Ex2 ========================================================================================================
temp2 = [x * 3 for x in generator_ex1()]
temp3 = (x * 3 for x in generator_ex1())  # generator

print(temp2)
print()

print(temp3)
print()

for i in temp3:
    print(i)
# ======================================================================================================================

print()
print("=" * 118)
print()

# Generator Ex3 (Important Functions) ==================================================================================
# count, takewhile, filterfalse, accumulate, chain, product, groupby...

# import itertools
# count ----------------------------------------------------------------------------------------------------------------
gen1 = itertools.count(1, 2.5)
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
# ... infinite

print()

# takewhile ------------------------------------------------------------------------------------------------------------
gen2 = itertools.takewhile(lambda n: n < 10, itertools.count(1, 2.5))
for v in gen2:
    print(v)

print()

# filterfalse ----------------------------------------------------------------------------------------------------------
gen3 = itertools.filterfalse(lambda n: n < 3, [1, 2, 3, 4, 5])
for v in gen3:
    print(v)

print()

# accumulate -----------------------------------------------------------------------------------------------------------
gen4 = itertools.accumulate([x for x in range(1, 11)])
for v in gen4:
    print(v)

print()

# chain 1 --------------------------------------------------------------------------------------------------------------
gen5 = itertools.chain('ABCDE', range(1, 11, 2))
print(list(gen5))

print()

# chain 2 --------------------------------------------------------------------------------------------------------------
gen6 = itertools.chain(enumerate('ABCDE'))
print(list(gen6))

print()

# product 1 ------------------------------------------------------------------------------------------------------------
gen7 = itertools.product('ABCDE')
print(list(gen7))

print()

# product 2 ------------------------------------------------------------------------------------------------------------
gen8 = itertools.product('ABCDE', repeat=2)
print(list(gen8))

print()

# groupby --------------------------------------------------------------------------------------------------------------
gen9 = itertools.groupby('AAABBBCCCCDDDDEEEEE')
# gen9 = itertools.groupby('ABCADDBDBAACBEBDBCACEEEBACBAEBBCAE')
for c, group in gen9:
    print(c, ' : ', list(group))
# ======================================================================================================================
