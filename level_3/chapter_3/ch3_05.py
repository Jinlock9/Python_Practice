"""
Chapter 3 - Python Advanced (3) : Descriptor (2)
Keywords : descriptor vs property, low level (descriptor) vs high level (property)
"""
# imports ==============================================================================================================
import os
import logging
# ======================================================================================================================
"""  # =================================================================================================================
[ Descriptor ]
1. 상황에 맞는 메소드 구현을 통한 객체 지향 프로그래밍 구현
2. property 와 달리 reuse (재사용) 가능
3. ORM Framework 사용
"""  # =================================================================================================================


# Ex 1 =================================================================================================================
# Descriptor Example 1
# import os
class DirectoryFileCount:
    def __get__(self, instance, owner=None):  # instance = DirectoryPath.self
        print(os.listdir(instance.dirname))
        return len(os.listdir(instance.dirname))


class DirectoryPath:
    # Descriptor Instance
    size = DirectoryFileCount()

    def __init__(self, dirname):
        self.dirname = dirname


s = DirectoryPath("./")
g = DirectoryPath("../")

print("Ex 1 > ", dir(DirectoryPath))
print("Ex 1 > ", DirectoryPath.__dict__)
print("Ex 1 > ", dir(s))
print("Ex 1 > ", s.__dict__)

print("Ex 1 > ", s.size)
print("Ex 1 > ", g.size)
print()
# ======================================================================================================================

# Ex 2 =================================================================================================================
# Descriptor Example 2
# import logging
logging.basicConfig(
    format='%(asctime)s %(message)s',
    level=logging.INFO,
    datefmt='%y-%m-%d %H:%M:%S',
)


class LoggedScoreAccess:
    def __init__(self, value=50):
        self.value = value

    def __get__(self, instance, owner=None):
        logging.info('%r accessing %r giving %r', instance.name, 'score', self.value)
        return self.value

    def __set__(self, instance, value):
        logging.info('%r updating %r giving %r', instance.name, 'score', self.value)
        self.value = value


class Student:
    # Descriptor Instance
    score = LoggedScoreAccess()

    def __init__(self, name):
        # Regular instance attribute
        self.name = name


s1 = Student("Kim")
s2 = Student("Lee")

# Check score
print("Ex 2 > ", s1.score)
s1.score += 20
print("Ex 2 > ", s1.score)

print("Ex 2 > ", s2.score)
s2.score += 30
print("Ex 2 > ", s2.score)

# check __dict__
print("Ex 2 > ", vars(s1))
print("Ex 2 > ", vars(s2))
print("Ex 2 > ", s1.__dict__)
print("Ex 2 > ", s2.__dict__)
# ======================================================================================================================
