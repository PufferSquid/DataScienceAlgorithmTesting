

# these return the indexes of the target

def linearSearch(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    
    return -1

def binarySearch(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        midValue = arr[mid]
        
        if target == midValue:
            return mid
        elif target < midValue:
            high = mid - 1
        else:
            low = mid + 1
    
    return -1