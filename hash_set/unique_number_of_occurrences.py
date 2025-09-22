 

def func(arr):
    
    dic = {}
    
    for num in arr:
        dic[num] = dic.get(num, 0) + 1
    occerrences = dic.values()
    
    if len(occerrences) == len(set(occerrences)):
        return True
    return False

arr = [1,2]
print(func(arr))