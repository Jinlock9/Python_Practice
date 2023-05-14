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
from concurrent import futures
# ======================================================================================================================

# 2가지 패턴 실습
# concurrent.futures map
# concurrent.futures wait, as_completed

# concurrent.futures map ===============================================================================================
WORK_LIST = [10000, 100000, 1000000, 10000000]


# 동시성 합계 계산 메인 함수
# 누적 합계 함수 (Generator)
def sum_generator(n):
    return sum(n for n in range(1, n + 1))


def main():
    # Worker Count
    worker = min(10, len(WORK_LIST))

    # starting time
    start_tm = time.time()

    # 결관 건수
    # ProcessPoolExecutor
    with futures.ThreadPoolExecutor() as executor:
        # map -> 작업 순서를 유지하고 즉시 실행
        result = executor.map(sum_generator, WORK_LIST)  # 4가지 작업을 동시에 실행

    # end time
    end_tm = time.time() - start_tm

    # output format
    msg = '\n Result -> {} Time : {:.2f}s'
    # print output
    print(msg.format(list(result), end_tm))


# 실행
if __name__ == '__main__':
    main()

# ======================================================================================================================
