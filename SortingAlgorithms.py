

def bucketSort(arr : list):

    if (len(arr) <= 1):
        return arr

    min_val = min(arr)
    max_val = max(arr)

    bucket_count = 10
    bucket_range = (max_val - min_val + 1) / bucket_count
    buckets = [[] for i in range(bucket_count)] 

    for value in arr:
        if bucket_range > 0:
            bucket_index = int((value - min_val) / bucket_range)

            if bucket_index >= bucket_count:
                bucket_index = bucket_count - 1
        else:
            bucket_index = 0 
        
        buckets[bucket_index].append(value)
    
    result = []

    for bucket in buckets:
        sorted_bucket = insertionSort(bucket)
        result.extend(sorted_bucket)
    
    return result


def insertionSort(arr : list):
    n = len(arr)

    if (n <= 1):
        return arr
    
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while(j >= 0 and key < arr[j]):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    
    return arr



def mergeSort(arr : list, left : int, right: int):
    if (left < right):
        mid = int(left + (right - left) // 2)

        mergeSort(arr, left, mid)
        mergeSort(arr, mid + 1, right)
        merge(arr, left, mid, right)

        return arr


def merge(arr : list, left : int, mid : int, right : int):

    n1 : int = mid - left + 1
    n2 : int = right - mid

    leftArr = [0] * n1
    rightArr = [0] * n2

    for i in range(0, n1):
        leftArr[i] = arr[left + i]
    
    for i in range(0, n2):
        rightArr[i] = arr[mid + 1 + i]

    i : int = 0
    j : int = 0

    k = left

    while i < n1 and j < n2:
        if leftArr[i] <= rightArr[j]:
            arr[k] = leftArr[i]
            i += 1
        else:
            arr[k] = rightArr[j]
            j += 1
        k += 1
    
    while i < n1:
        arr[k] = leftArr[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = rightArr[j]
        j += 1
        k += 1


    
    

    

    



