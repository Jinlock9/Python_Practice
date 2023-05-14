"""
[ Section 1 ] Thread (5) - Prod vs Cons Using Queue
Keywords : Producer / Consumer Pattern
"""
# imports ==============================================================================================================
import logging
from concurrent.futures import ThreadPoolExecutor
import queue
import random
import threading
import time
# ======================================================================================================================
"""  # =================================================================================================================
[ Producer-Consumer Pattern ] ------------------------------------------------------------------------------------------
    (1) Multithread Design Pattern 의 정석
    (2) 서버 측 프로그래밍의 핵심
    (3) 주로 허리 역할, 중요함
------------------------------------------------------------------------------------------------------------------------
[ Python Event Object ] ------------------------------------------------------------------------------------------------
    (1) Flag initial value ( 0 )
    (2) Set() -> 1, Clear() -> 0, Wait(1 -> return, 0 -> wait), isSet() -> current flag status
------------------------------------------------------------------------------------------------------------------------
"""  # =================================================================================================================


# producer
def producer(q, ev):
    """
    네트워크 대기 상태라 가정 (서버)
    :return:
    """
    while not ev.is_set():
        message = random.randint(1, 11)
        logging.info("Producer got message: %s", message)
        q.put(message)
    logging.info("Producer send event. Exiting...")


# consumer
def consumer(q, ev):
    """
    응답 받고 소비하는 것으로 가정 or DB 저장
    :return:
    """
    while not ev.is_set() or not q.empty():
        message = q.get()
        logging.info("Consumer storing message: %s (size=%d)", message, q.qsize())
    logging.info("Consumer received event. Exiting...")


# main area
if __name__ == "__main__":
    # set logging format
    fmt = "%(asctime)s: %(message)s"
    logging.basicConfig(format=fmt, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info("Main-Thread: Before creating and running thread")

    # size important
    pipeline = queue.Queue(maxsize=10)

    # event flag initial value 0
    event = threading.Event()

    # With Context
    with ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline, event)
        executor.submit(consumer, pipeline, event)

        # 실행 시간 조정
        time.sleep(0.001)

        logging.info("Main: about to set event")

        # 프로그램 종료
        event.set()
