def hourglassSum(arr):
    final_result = []
    max_val = 0
    for i in range(4):
        for j in range(4):
            temp = sum(arr[i][j:j+3]) + arr[i+1][j+1] + sum(arr[i+2][j:j+3])
            if temp > max_val:
                max_val = temp
    
    return max_val

array = [[1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 9, 2, -4, -4, 0],
    [0, 0, 0, -2, 0, 0],
    [0, 0, -1, -2, -4, 0]]

print(hourglassSum(array))