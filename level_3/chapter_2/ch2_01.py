"""
Chapter 2 - Python Advanced (2) : Context Manager Annotation
Keywords : @contextlib.contextmanager, __enter__, __exit__
"""
# imports ==============================================================================================================
import contextlib
import time
# ======================================================================================================================
"""  # =================================================================================================================
- understanding most typical WITH structure
- using Contextlib decorator
- 직관적 코드, 용이한 예외 처리
"""  # =================================================================================================================


# Ex 1 =================================================================================================================
# Use decorator
@contextlib.contextmanager
def my_file_writer(filename, method):
    file = open(filename, method)
    yield file  # __enter__
    file.close()  # __exit__


with my_file_writer("test4.txt", "w") as f:
    f.write("Context Manager \nContextlib Test4.")
# ======================================================================================================================


# Ex 2 =================================================================================================================
# Use decorator
@contextlib.contextmanager
def ExecuteTimerDc(msg):
    start = time.monotonic()
    try:  # __enter__
        yield start
    except BaseException as e:
        print("Logging Exception : {} : {}".format(msg, e))
        # raise
    else:  # __exit__
        print("{} : {}s".format(msg, time.monotonic() - start))


with ExecuteTimerDc("Now Process.") as v:
    print("Received start monotonic2 : {}".format(v))
    # Execute
    for i in range(1000000):
        pass
print()

with ExecuteTimerDc("Now Process.") as v:  # raise error
    print("Received start monotonic2 : {}".format(v))
    raise ValueError("Error occurred.")
# ======================================================================================================================
