

def func(nums):
     total_sum = sum(nums)
     left_sum = 0
     for num in range(len(nums)):

         if left_sum == (total_sum - left_sum - nums[num]):
             return num
         left_sum += nums[num]
     return -1
     
nums = [1,7,3,6,5,6]
print(func(nums))