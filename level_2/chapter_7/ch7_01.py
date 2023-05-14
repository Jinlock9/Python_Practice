# Chapter 07-01 ========================================================================================================
# AsyncIO --------------------------------------------------------------------------------------------------------------
# 비동기 I/O Coroutine 작업
# Generator -> 반복적인 객체 return 사용
# Non-blocking 비동기 처리
# DB 작업이나 web service 작업을 동시 처리할 때 사용할 수 있는 고순위 package
# ----------------------------------------------------------------------------------------------------------------------
# Blocking I/O : 호출된 함수가 자신의 작업이 완료 될 때까지 제어권을 가지고 있음. 타 함수는 대기.
# NonBlocking I/O : 호출된 함수가 (subroutine) return 후 호출한 함수 (main routine)에 제어권 전달 -> 타 함수는 일 지속
# ----------------------------------------------------------------------------------------------------------------------
# Thread Disadvantage : 디버깅 어려움, 자원 접근 시 Race Condition (경쟁 상태), Dead Lock -> 고려 후 코딩
# Coroutine Advantage : 하나의 루틴만 실행 -> 락 관리 필요 x -> 제어권으로 실행
# Coroutine Disadvantage : 사용 함수가 비동기로 구현이 되어 있어야 하거나, 또는 직접 비동기로 구현해야 한다.
# ----------------------------------------------------------------------------------------------------------------------
# imports --------------------------------------------------------------------------------------------------------------
import asyncio
import timeit
from urllib.request import urlopen
from concurrent.futures import ThreadPoolExecutor
import threading
# ----------------------------------------------------------------------------------------------------------------------

# Starting time
start = timeit.default_timer()

# 서비스 방향이 비슷한 사이트로 실습 권장 (ex. 게시판성 커뮤니티)
urls = ['https://www.daum.net/', 'https://www.naver.com/', 'https://mlbpark.donga.com/mp/', 'https://www.tistory.com/']


async def fetch(url, executor):
    # print thread name
    print("Thread Name : ", threading.current_thread().name, 'Start', url)
    # execute
    response = await loop.run_in_executor(executor, urlopen, url)  # <OLD>
    # response = urlopen(url)  # <NEW>
    print("Thread Name : ", threading.current_thread().name, 'Done', url)

    # return results
    return response.read()[0:5]


async def main():
    # Create Thread Pool
    executor = ThreadPoolExecutor(max_workers=10)

    # collect future objects, then process in 'gather'
    futures = [
        asyncio.ensure_future(fetch(url, executor)) for url in urls
    ]

    # collect results
    result = await asyncio.gather(*futures)  # gather 가 결과값을 끝까지 기다림

    print()
    print('Result : ', result)


if __name__ == '__main__':
    # initialize loop
    loop = asyncio.get_event_loop()
    # wait until work completes
    loop.run_until_complete(main())
    # asyncio.run(main())  # <NEW>
    # measure processing time
    duration = timeit.default_timer() - start
    # total time
    print("Total Running Time : ", duration)
# ======================================================================================================================
