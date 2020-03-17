def find_second_highest(arr):
    if len(arr) in (0,1):
        return "There is no second highest"
    else:
        maximum, second_max = 0, 0
        for i in arr:
            if i>maximum:
                second_max = maximum
                maximum = i
            elif i>second_max and i!=maximum:
                second_max = i 

        return second_max

print(find_second_highest([1, 2, 3, 5, 8, 10, 9, 10, 8]))