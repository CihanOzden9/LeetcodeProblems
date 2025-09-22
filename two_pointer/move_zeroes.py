

def func(nums):
    n_z_p = 0
    for digit in range(len(nums)):
        if nums[digit] != 0:
            nums[n_z_p], nums[digit] = nums[digit], nums[n_z_p]
            n_z_p += 1
    return nums

arr = [1,0,4,0,6]
print(func(arr))
            