'''python searches'''
import math

def linear_search(list, value):
    search = 0
    found = False
    
    while search < len(list) and found == False:
        if list[search] == value:
            found = True
        else:
            search = search + 1
    return found
    
def interpolation_search(list, value):
    search = 0
    length = (len(list) - 1)
    
    while search <= length and value >= list[search] and value <= list[length]:
        mid = search + int(((float(length - search)/(list[length] - list[search])) * ( value - list[search])))
        
        if list[mid] == value:
            return True
        if list[mid]  < value:
            search = mid + 1
    
    return False
    
def binary_search(list, value):
    search = 0
    length = len(list)-1
    found = False
    
    while (search <= length) and (found == False):
        mid = (search + length) // 2
        if list[mid] == value:
            found = True
        else:
            if value < list[mid]:
                search = mid - 1
            else:
                search = mid + 1
    return found

def JumpSearch (list, value):
    length = len(list)
    jump = int(math.sqrt(length))
    left, right = 0, 0
    while left < length and list[left] <= value:
        right = min(length - 1, left + jump)
        if list[left] <= value and list[right] >= value:
            break
        left += jump;
    if left >= length or list[left] > value:
        return False
    right = min(length - 1, right)
    i = left
    while i <= right and list[i] <= value:
        if list[i] == value:
            return True
        i += 1
    return False
    
def binary_search_recursive(list, low, high, value):
    if high >= low:
        mid = (high+low)// 2
        
        if list[mid] == value:
            return True
        
        elif list[mid] > value:
            return binary_search_recursive(list, low, mid-1, value)
        else:
            return binary_search_recursive(list, mid+1, high, value)
    else:
        return False 
        
if "__main__" == __name__:
     list = [0,1,2,3,4,5,6,7,8,9,10]
     result = linear_search(list, 10)
     print(result)
     result = interpolation_search(list, 10)
     print(result)
     result = binary_search(list, 10)
     print(result)
     result = JumpSearch(list, 10)
     print(result)
     result = binary_search_recursive(list, 0, len(list) -1,  10)
     print(result)