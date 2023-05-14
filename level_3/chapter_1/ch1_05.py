"""
Chapter 1 - Python Advanced (1) : Context Manager (2)
Keywords : Contextlib, __enter__, __exit__
"""
# imports ==============================================================================================================
import time
# ======================================================================================================================
"""  # =================================================================================================================
Contextlib - Measure execution time (timer)
"""  # =================================================================================================================

# Contextlib ===========================================================================================================
# Ex 1 -----------------------------------------------------------------------------------------------------------------
# use Class
# import time


class ExecuteTimer:
    def __init__(self, msg):
        self._msg = msg

    def __enter__(self):
        self._start = time.monotonic()
        return self._start

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print("Logging exception : {}".format((exc_type, exc_val, exc_tb)))
        else:
            print("{} : {} s".format(self._msg, time.monotonic() - self._start))
        return True


with ExecuteTimer("Now Process.") as v:
    print("Received start monotonic1: {}".format(v))  # v <- self._start
    # Execute Job
    for i in range(10000000):
        pass

with ExecuteTimer("Now Process.") as v:
    print("Received start monotonic1: {}".format(v))  # v <- self._start
    # Raise Exception
    raise Exception("Raise Exception for testing")


