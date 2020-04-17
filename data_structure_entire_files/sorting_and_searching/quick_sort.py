# quick sort
def quick_sort_from_end(arr):
    """ sorting arr pivot point is the last index """
    pivot = arr[-1]
    lag_index = 0
    for i in range(len(arr)):
        if arr[i]<pivot:
            if i>lag_index:
                arr[i], arr[lag_index]= arr[lag_index], arr[i]
            lag_index += 1
    arr[lag_index+1], arr[-1] = arr[-1], arr[lag_index+1]

def partition(arr, low, high):
    pivot = arr[high]
    lag_index = low
    for i in range(low, high):
        if arr[i]<pivot:
            arr[i], arr[lag_index]= arr[lag_index], arr[i]
            lag_index += 1
    arr[lag_index+1], arr[high] = arr[high], arr[lag_index+1]
    
    return arr

print(partition([2,10,4,8,7], 0, 4))


