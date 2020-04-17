def find_missing_number_using_sum(arr):
    """ find missing number from a consecutive integer array. Problem: chance of overflow """
    arr_len = len(arr)
    arr_sum = (arr_len + 1)(arr_len + 2) // 2
    return arr_sum - sum(arr)

def find_missing_number_using_loop(arr):
    total, arr_len = 0, len(arr)
    for i in range(2, arr_len + 2):
        total += i
        total -= arr[i-2]

    return total

print(find_missing_number_using_loop([5, 6, 2, 1, 4]))

def find_missing_number_using_xor(arr):
    