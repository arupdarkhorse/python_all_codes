def minimum_bribe(arr):
    len_arr= len(arr)
    idx, bribe_count = 0, 0
    expected_num = 1
    process_cnt = 0 
    temp_idx = 0
    while idx<len_arr:
        if arr[idx]==expected_num-process_cnt:
            idx += 1
            expected_num += 1
        else:
            if arr[idx+1]==expected_num:
                temp_idx += 1
                temp = arr[idx-1]-arr[idx]
                bribe_count += temp
                idx += 2
                expected_num +=2
                if temp_idx >=1:
                    process_cnt +=1
            else:
                print('order not possible')
                return

    return bribe_count

#print(minimum_bribe([2, 1, 8, 3, 4, 6, 5, 7]))
# print(minimum_bribe([2, 1, 8, 3, 6, 4, 5, 7]))
# print(minimum_bribe([2, 1, 8, 3, 5, 4, 6, 7]))
# print(minimum_bribe([2, 1, 8, 3, 6, 4, 7, 5]))



