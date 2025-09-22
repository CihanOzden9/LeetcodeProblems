
def findSingle(nums):
    ones,twos = 0,0
    for num in nums:
        ones = (ones ^ num) & -(twos + 1)
        twos = (twos ^ num) & -(ones + 1)
    return ones

arr = [1,1,1,9]
result = findSingle(arr)
print(result)