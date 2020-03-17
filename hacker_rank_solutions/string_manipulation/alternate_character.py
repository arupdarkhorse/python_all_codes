def alternate_char(arr):
    """ This function will return repeting charcters between alternate characters """
    CNT = 0
    if len(arr)==1:
        return 0
        
    for i in range(len(arr)-1):
        if arr[i]==arr[i+1]:
            CNT +=1

    return CNT

alternate_char("AAABBABBAAB")