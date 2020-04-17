# selection sort time complexity O(n**2)
def selection_sort(arr):
    """ This program is for sorting an array using selection sort """
    arr_len = len(arr)
    for i in range(arr_len):
        min_pos = i
        for j in range(i+1,arr_len):
            if arr[j]<arr[min_pos]:
                min_pos = j
        arr[i], arr[min_pos] = arr[min_pos], arr[i]

    return arr

print(selection_sort([1, 23, 4, 4, 67, 7]))

# stable selection sort, means the postion of same keys will not change after sorting

# sorting string to do

