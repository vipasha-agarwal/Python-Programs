import threading 
import time
from concurrent.futures import ThreadPoolExecutor
# Indicates some task being done
def func(seconds):
    print(f"sleeping for {seconds} seconds")
    time.sleep(seconds)

def main():
    time1 = time.perf_counter()
    # func(4)
    # func(7)
    # func(2)
    # func(1)

    t1 = threading.Thread(target = func, args = [4])
    t2 = threading.Thread(target = func, args = [6])
    t3 = threading.Thread(target = func, args = [3])
    t4 = threading.Thread(target = func, args = [2])

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join() # it is used to wait till the 1 thread end
    t2.join()
    t3.join()
    t4.join()
    # Calculating Time 
    time2 = time.perf_counter()
    print(time2 - time1)

def PoolingDemo():
    with ThreadPoolExecutor(max_workers = 1) as executor:
        # future1 = executor.submit(func, 3)       
        # future2 = executor.submit(func, 2)
        # future3 = executor.submit(func, 4)
        # print(future1.result())
        # print(future2.result())
        # print(future3.result())

        l = [3, 5, 1, 2]
        results = executor.map(func, l)
        for result in results:
            print(result)

PoolingDemo()