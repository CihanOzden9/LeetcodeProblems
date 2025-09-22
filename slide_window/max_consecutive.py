def func(nums,k):
    l = 0
    max_len = 0
    
    for r in range(len(nums)):
        if nums[r] == 0:
            k -= 1
        if k < 0:
            if nums[l] == 0:
                k += 1
            l += 1
        max_len = max(max_len, r-l+1)
    return max_len

arr = [1,1,1,0,0,0,1,1,1,1,0]
print(func(arr,2))
            