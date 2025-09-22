def func(nums):
    
    first = float("inf")
    second = float("inf")
    
    for num in nums:
        if num <= first:
            first = num
            
        elif num <= second:
            second = num
        else:
            return True
    return False

arr = [2,1,4,5,3]
print(func(arr))
        