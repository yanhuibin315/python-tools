"""
通过multiprocessing模块使用python多进程
"""
from multiprocessing import Pool
import time
import random
def add_two_num(num1, num2):
    time.sleep(random.randint(1, 3))
    return num1+num2


def create_pool(pool_num=10, func_name=add_two_num):
    resultList = []
    with Pool(pool_num) as pool:
        for num1 in range (0, 10):
            # idx += 1
            # if idx > 100: break
            result = pool.apply_async(func_name, (num1, num1*2))
            resultList.append(result)
        pool.close()
        pool.join()
    
    return resultList

if __name__ == '__main__':
    results = create_pool(4, add_two_num)
    for result in results:
        sum = result.get()
        print(sum)