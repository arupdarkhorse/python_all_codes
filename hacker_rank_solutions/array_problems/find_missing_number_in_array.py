def finding_missing_num(arr):
    """ finding a single missing number in array """
    len_arr = len(arr)
    for i in range(len_arr-1):
        if arr[i+1]-arr[i]!=1:
            return arr[i] + 1
    
array = list(range(1000000000))
array.remove(99996000)
print(finding_missing_num(array))