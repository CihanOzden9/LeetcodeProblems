def findSingle(arr):

    result = 0
    
    for num in arr:
        result = num ^ result
    return result

array = [1,2,4,1,4,5,2,2]

output = findSingle(array)

print(output)