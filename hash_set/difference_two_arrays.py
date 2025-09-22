def func(nums1, nums2):
    nums1 = set(nums1)
    nums2 = set(nums2)
    answer = [list(nums1 - nums2), list(nums2-nums1)]
    return answer 

arr1 = [1,2,3]
arr2 = [2,4,6]
print(func(arr1, arr2))