

def func(nums):
    l = r = 0
    max_ones = 0
    del_pos = -1
    
    for i in range(len(nums)):
        if nums[i] == 0:
            max_ones = max(max_ones, r-l-1)
            l = del_pos + 1
            del_pos = r
        elif r == len(nums) -1:
            max_ones = max(max_ones, r - 1)
            
    return max_ones
    
        
        