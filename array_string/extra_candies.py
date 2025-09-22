
def func(candies, extraCandies):
    result = []
    max_candy = max(candies)
    for candy in candies:
         result.append((candy+extraCandies) >= max_candy)
    return result     
arr = [4,2,1,1,2]
deneme = func(arr,1)
print(deneme)
        