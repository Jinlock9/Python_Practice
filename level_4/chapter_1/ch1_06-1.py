"""
[ Section 1 ] Thread (4) - Lock, DeadLock
Keywords : Lock, DeadLock, Race Condition, Thread synchronization
"""
# imports ==============================================================================================================
import logging
from concurrent.futures import ThreadPoolExecutor
import time
import threading
# ======================================================================================================================
"""  # =================================================================================================================
[ Terminology ] -------------------------------------------------------------------------------------------------------
    (1) Semaphore: 프로세스간 공유된 자원에 접근 시 문제 발생 가능성이 있어서
        -> 한 개의 프로세스만 접근 처리를 고안한 것 (경쟁 상태 예방)
    (2) Mutex: 공유된 자원의 데이터를 여러 thread 가 접근하는 것을 막는 것 -> 경쟁 상태 예방
    (3) Lock: 상호 배제를 위한 잠금 (lock) 처리 -> 데이터 경쟁
    (4) Deadlock: 프로세스가 자원을 획득하지 못해 다음 처리를 못하는 무한 대기 상황 (교착 상태)
    (5) Thread Synchronization (Thread 동기화): Thread 동기화를 통해서 안정적으로 동작하게 처리 (동기화 메소드, 동기화 블럭)
------------------------------------------------------------------------------------------------------------------------
[ Difference between Semaphore and Mutex ] -----------------------------------------------------------------------------
    Semaphore 와 Mutex 객체는 모두 병렬 프로그래밍 환경에서 상호배제를 위해 사용
    Mutex -> 단일 스레드가 리소스 또는 중요 섹션을 소비 허용
    Semaphore -> 리소스에 대한 제한된 수의 동시 엑세스 허용
------------------------------------------------------------------------------------------------------------------------
"""  # =================================================================================================================


class FakeDataStore:
    # shared variable
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()

    # update variable
    def update(self, v):
        logging.info("Thread [%s] starting update", v)

        # mutex & Lock 등 동기화 (Thread synchronization 필요)

        # Acquiring Lock (1)
        """
        self._lock.acquire()
        logging.info("Thread [%s] acquire lock", v)
        local_copy = self.value
        local_copy += 1
        time.sleep(0.1)
        self.value = local_copy

        logging.info("Thread [%s] about to release lock", v)
        self._lock.release()
        """

        # Acquiring Lock (2)
        with self._lock:
            logging.info("Thread [%s] acquire lock", v)
            local_copy = self.value
            local_copy += 1
            time.sleep(0.1)
            self.value = local_copy
            logging.info("Thread [%s] about to release lock", v)

        logging.info("Thread [%s] finishing update", v)


# main area
if __name__ == "__main__":
    # set logging format
    fmt = "%(asctime)s: %(message)s"
    logging.basicConfig(format=fmt, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info("Main-Thread: Before creating and running thread")

    # class instance
    store = FakeDataStore()

    logging.info("Testing update: Starting value is %d", store.value)

    # With Context
    with ThreadPoolExecutor(max_workers=3) as executor:
        for n in ['First', 'Second', 'Third']:
            executor.submit(store.update, n)

    logging.info("Testing update: Ending value is %d", store.value)



