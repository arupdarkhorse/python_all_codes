# binary search using recursion
def binary_search_recu(arr, item):
    """ binary search using recursion"""
    def binary_search(arr, first, last, item):
        """ wrapper function """
        if first<=last:
            mid = (first + last)//2
            if arr[mid]==item:
                return item
            else:
                if arr[mid]<item:
                    return binary_search(arr, mid+1, last, item)
                else:
                    return binary_search(arr, first, mid-1, item)
        
        return False
    
    first, last = 0, len(arr)-1
    return binary_search(arr, 0, last, item)

array1 = [2,3,4,5,5]
#print(binary_search_recu(array1, 5))
 
# binary search using iteration
def binary_search_iter(arr, item):
    """ Binary search using iterative method """
    first, last = 0, len(arr)-1
    while first<=last:
        mid = (first + last)//2
        if arr[mid] == item:
            return arr[mid]
        else:
            if arr[mid]<item:
                first = mid + 1
            else:
                last = mid - 1
    return False
array = []
#print(binary_search_iter(array, 3))