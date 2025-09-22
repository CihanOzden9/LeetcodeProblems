
def fun(nums):
    result = 0
    count = 0
    for num in nums:
        if count == 0:
            result = num
        count += 1 if num == result else -1
            
    return result

array = [3,2,3]
deneme = fun(array)
print(deneme)