import random
import time
from common.log import log_config
logger = log_config.logger

def check_elapsed_time(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        ret_val = func(*args, **kwargs)
        t2 = time.time()
        logger.info(f"该段代码{func}运行时间为：{round(t2 - t1, 2)}")
        return ret_val
    return wrapper

def find_smallest(arr):
    smallest = arr[0]  # 存储最小的值
    smallest_index = 0  # 存储最小的元素索引
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


@check_elapsed_time
def selection_sort(arr):
    new_arr = []
    for item in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr


if __name__ == '__main__':
    unique_random_list = list(random.sample(range(1, 100000), 10000))

    print(len(unique_random_list))
    sorted_list = selection_sort(unique_random_list)
    print(sorted_list[:10])
