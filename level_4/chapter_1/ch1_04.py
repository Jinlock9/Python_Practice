"""
[ Section 1 ] Thread (2) - Daemon, Join
Keywords : Daemon Thread, Join
"""
# imports ==============================================================================================================
import logging
import threading
# ======================================================================================================================
"""  # =================================================================================================================
[ Daemon Thread ] ------------------------------------------------------------------------------------------------------
    (1) Background 에서 실행
    (2) * Main Thread 종료 시 즉시 종료 *
    (3) 주로 Background 무한 대기 이벤트 발생 실행하는 부분 담당 -> JVM (Garbage Collection), Auto Save
    (4) 일반 Thread 는 작업 종료시 까지 실행 
------------------------------------------------------------------------------------------------------------------------
"""  # =================================================================================================================


def thread_func(name, d):
    logging.info("- Sub-Thread %s: STARTING", name)
    for i in d:
        print(i)
    logging.info("- Sub-Thread %s: ENDING", name)


# main area
if __name__ == "__main__":
    # set logging format
    fmt = "%(asctime)s: %(message)s"
    logging.basicConfig(format=fmt, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info("Main-Thread: Before creating thread")

    # check function factor
    x = threading.Thread(target=thread_func, args=('First', range(20000)), daemon=True)  # Daemon: main thread 종료와 함께 종료
    y = threading.Thread(target=thread_func, args=('Second', range(10000)), daemon=True)

    logging.info("Main-Thread: Before running thread")

    # start sub-thread
    x.start()
    y.start()

    # Check whether it is Daemon
    # print(x.daemon)

    # 주석 전후 결과 확인
    # x.join()  # Main thread wait for sub thread to finish completely
    # y.join()
    # Daemon 을 사용했음에도 join 을 쓰면 결국 main 은 sub 를 끝까지 기다림

    logging.info("Main-Thread: Waiting for the thread to finish")

    logging.info("Main-Thread: Process all done")
