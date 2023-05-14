"""
[ Section 1 ] Thread (3) - ThreadPoolExecutor
Keywords : Many Threads, concurrent.futures, (xxx)PoolExecutor
"""
# imports ==============================================================================================================
import logging
from concurrent.futures import ThreadPoolExecutor
import time
# ======================================================================================================================
"""  # =================================================================================================================
[ Group Thread ] -------------------------------------------------------------------------------------------------------
    (1) Python 3.2 이상 표준 라이브러리 사용
    (2) concurrent.futures
    (3) with 사용으로 thread 생성, 소멸 라이프 사이클 관리 용이
    (4) hard to debug
    (5) 대기 중인 작업 -> Queue -> 완료 상태를 조사 -> 결과 또는 예외 반환 -> 단일화 (캡슐화)
------------------------------------------------------------------------------------------------------------------------
"""  # =================================================================================================================


# task area ============================================================================================================
def task(name):
    logging.info("Sub-Thread %s: STARTING", name)

    result = 0
    for i in range(10001):
        result += i

    logging.info("Sub-Thread %s: RESULT - %d", name, result)

    return result
# ======================================================================================================================


# main area ============================================================================================================
def main():
    # set logging format
    fmt = "%(asctime)s: %(message)s"
    logging.basicConfig(format=fmt, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info("Main-Thread: Before creating and running thread")

    # Option 1 ---------------------------------------------------------------------------------------------------------
    """"
    # max_worker: 작업의 개수가 넘어가면 직접 설정이 유리
    executor = ThreadPoolExecutor(max_workers=3)
    task1 = executor.submit(task, ("First",))
    task2 = executor.submit(task, ("Second",))
    
    # if there are return values
    # print(task1.result())
    # print(task2.result())
    """
    # Option 2 ---------------------------------------------------------------------------------------------------------
    with ThreadPoolExecutor(max_workers=3) as executor:
        tasks = executor.map(task, ['First', 'Second', 'Third'])

        # check result
        print("RETURN VALUES : {}".format(list(tasks)))


if __name__ == "__main__":
    main()
# ======================================================================================================================
