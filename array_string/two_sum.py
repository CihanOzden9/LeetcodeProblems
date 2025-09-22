def fun(nums, target):
    seen = {}
    for i,num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff],i]
        seen[num] = i
        
array = [1,2,3,5,6]
result = fun(array,9)
print(result)