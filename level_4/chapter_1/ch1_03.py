"""
[ Section 1 ] Thread (1) - Basic
Keywords : Threading Basic
"""
# imports ==============================================================================================================
import logging
import threading
import time
# ======================================================================================================================


def thread_func(name):
    logging.info("- Sub-Thread %s: STARTING", name)
    time.sleep(3)
    logging.info("- Sub-Thread %s: ENDING", name)


# main area
if __name__ == "__main__":
    # set logging format
    fmt = "%(asctime)s: %(message)s"
    logging.basicConfig(format=fmt, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info("Main-Thread: Before creating thread")

    # check function factor
    x = threading.Thread(target=thread_func, args=('First',))

    logging.info("Main-Thread: Before running thread")

    # start sub-thread
    x.start()

    # 주석 전후 결과 확인
    x.join()  # Main thread wait for sub thread to finish completely

    logging.info("Main-Thread: Waiting for the thread to finish")

    logging.info("Main-Thread: Process all done")


