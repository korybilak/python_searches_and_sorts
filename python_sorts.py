'''python sorting/searching program'''

def bubblesort(list):
    for num in range(len(list)-1,0,-1):
        for id in range(num):
            if list[id]>list[id+1]:
                temp = list[id]
                list[id] = list[id+1]
                list[id+1] = temp
    return list
    
def merge_sort(list):
    if len(list) <=1:
        return list
        
    middle = len(list) // 2
    first_half = list[:middle]
    second_half = list[middle:]
    
    first_half = merge_sort(first_half)
    second_half = merge_sort(second_half)
    list = merge(first_half, second_half)
    
    return list
    
def merge(first_half, second_half):
    list = []
    while len(first_half) != 0 and len(second_half) != 0:
        if first_half[0] < second_half[0]:
            list.append(first_half[0])
            first_half.remove(first_half[0])
        else:
            list.append(second_half[0])
            second_half.remove(second_half[0])
            
    if len(first_half) == 0:
        list = list + second_half
    else:
        list = list + first_half
        
    return list
    
def insertion_sort(list):
    for i in range(1, len(list)):
        j = i-1
        value = list[i]
    
    while(list[j] > value) and (j >= 0):
        list[j+1] = value[j]
        j = j-1
    
    list[j+1] = value
    
    return list
                
 
def shell_sort(list):
    value = len(list) // 2
    while value > 0:
        for i in range(value, len(list)):
            temp = list[i]
            j = i
        
            while j >= value and list[j - value] > temp:
                list[j] = list[j - value]
                j = j - value
            
            list[j] = temp
            
        value = value // 2
    
    return list
    
def selection_sort(list):
    for value in range(len(list)):
        min_value = value
        for j in range(value + 1, len(list)):
            if list[min_value] > list[j]:
                min_value = j
    
    list[value], list[min_value] = list[min_value], list[value]
    
    return list
    
def partition(list, low, high):
    i = (low - 1)
    pivot = list[high]
    
    for j in range(low, high):
        if list[j] <= pivot:
            i = i+1
            list[i], list[j] = list[j], list[i]
    
    list[i + 1], list[high] = list[high], list[i+1]
    return (i+1)
    
def quick_sort(list, low, high):
    if len(list) == 1:
        return list
    elif low < high:
        partition_index = partition(list, low, high)
        quick_sort(list, low, partition_index - 1)
        quick_sort(list, partition_index + 1, high)
    return list    
    
if "__main__" == __name__:
    list = [10,9,8,7,6,5,4,3,2,1,0]
    list1 = bubblesort(list)
    print(list1)
    list2 = merge_sort(list)
    print(list2)
    list3 = insertion_sort(list)
    print(list3)
    list4 = shell_sort(list)
    print(list4)
    list5 = selection_sort(list)
    print(list5)
    list6 = quick_sort(list, 0, len(list)-1)
    print(list6)
    