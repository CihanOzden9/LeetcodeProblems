

def func(nums,k):
    n = len(nums)
    
    
    window = sum(nums[:k])
    operation = window
    for i in range(n-k):
        window = (window - nums[i] + nums[i+k])
        operation = max(window, operation)
    return operation/k

arr = [1,12,-5,-6,50,3]
print(func(arr,4))                      
        

