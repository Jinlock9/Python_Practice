"""
Chapter 1 - Python Advanced (1) : Context Manager (1)
Keywords : Contextlib, __enter__, __exit__, exception
"""
# imports ==============================================================================================================
# ======================================================================================================================
"""  # =================================================================================================================
Context Manager : 원하는 타이밍에 정확하게 리소스를 할당 및 제공, 반환하는 역할
-> Typical : with
"""  # =================================================================================================================

# with =================================================================================================================
# Ex 1 -----------------------------------------------------------------------------------------------------------------
file = open('./test1.txt', 'w')
try:
    file.write("Context Manager \nContextlib Test1.")
finally:
    file.close()

# Ex 2 -----------------------------------------------------------------------------------------------------------------
with open("test2.txt", 'w') as f:
    f.write("Context Manager \nContextlib Test2.")


# Ex 3 -----------------------------------------------------------------------------------------------------------------
# Use Classes -> Context Manager with exception handling.
class MyFileWriter:
    def __init__(self, filename, method):
        print("MyFileWriter started : __init__")
        self.file_obj = open(filename, method)

    def __enter__(self):
        print("MyFileWriter started : __enter__")
        return self.file_obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("MyFileWriter started : __exit__")
        if exc_type:
            print("Logging exception : {}".format((exc_type, exc_val, exc_tb)))
        self.file_obj.close()


with MyFileWriter("test3.txt", 'w') as f:
    f.write("Context Manager \nContextlib Test3.")
