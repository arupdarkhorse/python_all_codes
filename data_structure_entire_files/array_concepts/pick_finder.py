# using naive approach

def peak_finder(arr):
    """ peak finder will find peak value and return. This will work for any problem """
    result = []
    arr_len = len(arr)
    
    if arr_len==0:
        print("Peak finding not possible it is empty")
        return
    elif arr_len==1:
        return arr[0]
    elif arr_len==2:
        if arr[0]>arr[1]:
            return arr[0]
        else:
            return arr[1]
    for i in range(len(arr)-2):
        if arr[i+1]>= arr[i] and arr[i+1]>arr[i+2]:
            result.append(arr[i+1])
    
    return result

print(peak_finder([]))

# using iteration

def peak_finder(arr):
    """ using divide conquer iterative approach"""
    low, high = 0, len(arr)-1
    cnt = 0
    while low < high:
        mid = (high + low)//2
        if arr[mid] > arr[mid+1]:
            high = mid 
            cnt+=1
        else:
            low = mid + 1
            cnt+=1
    
    return low, cnt

# using recursion divide conquer
def peak_finder(arr):
    """ using recursion. This will only work for sorted array, Code will fail for
        arr = [90, 2, 20, 30, 70, 60 ]   """

    def recur(arr, low, high):
        if low==high:
            return low 
        mid = (low + high)//2
        if arr[mid] < arr[mid+1]:
            return recur(arr, mid+1, high)
        return recur(arr, low, mid)

    return recur(arr, 0, len(arr)-1)

arr = [90, 2, 20, 30, 70, 60 ] 

print("Index of a peak point is", peak_finder(arr)) 

# two dimensional pick finder to do

