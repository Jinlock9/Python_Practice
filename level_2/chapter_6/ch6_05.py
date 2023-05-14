# Chapter 06-04 ========================================================================================================
# Futures 동시성 --------------------------------------------------------------------------------------------------------
# 비동기 작업 실행
# 지연 시간 (Block) CPU 및 리소스 낭비 방지 -> (File) Network I/O 관련 작업 -> 동시성 활용 권장
# 동기 작업 : A 가 끝내면 B 시작
# 비동기 작업 : A 와 B 동시 수행 가능
# 비동기 작업과 적합한 Program 경우 압도적 성능 향상
# ----------------------------------------------------------------------------------------------------------------------
# futures : 비동기 실행을 위한 API를 고수준으로 작성 -> 사용하기 쉽도록 개선
# concurrent.Futures
# 1. Multithreading / Multiprocessing API 통일 -> 매우 사용하기 쉬움
# 2. 실행 중인 작업 취소, 완료 여부 체크, 타임 아웃 옵션, 콜백 추가, 동기화 코드 매우 쉽게 작성 -> promise 개념
# ----------------------------------------------------------------------------------------------------------------------
# GIL ------------------------------------------------------------------------------------------------------------------
# GIL : 두 개 이상의 Thread 가 동시에 실행 될 때, 하나의 자원을 access 하는 경우 -> 이슈를 방지하기 위해 -> GIL 이 실행 됨
#       -> 즉 리소스 적체에 락이 걸림 -> Context switch (문맥 교환)
# GIL - Global Interface Lock
# GIL 우회하기 : Multiprocessing 사용, Cpython 사용
# imports --------------------------------------------------------------------------------------------------------------
import os
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, wait, as_completed
# ======================================================================================================================

# 2가지 패턴 실습
# concurrent.futures map
# concurrent.futures wait, as_completed

# concurrent.futures wait, as_completed ================================================================================

WORK_LIST = [10000000, 10000, 100000, 1000000]


# 동시성 합계 계산 메인 함수
# 누적 합계 함수 (Generator)
def sum_generator(n):
    return sum(n for n in range(1, n + 1))


# wait
# as_completed
def main():
    # Worker Count
    worker = min(10, len(WORK_LIST))

    # starting time
    start_tm = time.time()
    # Futures
    futures_list = []

    # 결관 건수
    # ProcessPoolExecutor
    with ThreadPoolExecutor() as executor:
        for work in WORK_LIST:
            # future_ 만 반환
            future_ = executor.submit(sum_generator, work)
            # scheduling
            futures_list.append(future_)
            # check scheduling
            print('Schedule for {} : {}'.format(work, future_))
        """ [1] WAIT ---------------------------------------------------------------------------------------------------
        # wait 결과 출력
        result = wait(futures_list, timeout=1)
        # success works
        print('Completed Tasks : ' + str(result.done))
        # failed works
        print("Pending ones after waiting for 1 seconds : " + str(result.not_done))
        # print output
        print([f.result() for f in result.done])
        """  # ---------------------------------------------------------------------------------------------------------
        # [2] AS_COMPLETED ---------------------------------------------------------------------------------------------
        # as_completed 결과 출력
        for f in as_completed(futures_list):
            result = f.result()
            done = f.done()
            cancelled = f.cancelled()
            # future 결과 확인
            print("Future Result : {}, Done : {}".format(result, done))
            print("Future Cancelled : {}".format(cancelled))
        # --------------------------------------------------------------------------------------------------------------
    # end time
    end_tm = time.time() - start_tm

    # output format
    msg = '\n Time : {:.2f}s'
    # print output
    print(msg.format(end_tm))


# 실행
if __name__ == '__main__':
    main()

# ======================================================================================================================
