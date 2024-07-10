

def find_smallest(arr):
    smallest = arr[0]   # 存储最小的值
    smallest_index = 0  # 存储最小的元素索引
    for i in range(1,len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selection_sort(arr):
    new_arr = []
    for item in arr:
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr



if __name__ == '__main__':
    arr = [2,7,4,5,0,72,3,8,94,10]
    print(find_smallest(arr))