

def func(s):
    voweles = set("aeiouAEIOU")
    s = list(s)
    left, right = 0, len(s) -1   
    while left < right:
        if s[left] not in voweles:
            left += 1
            continue     
        if s[right] not in voweles:
            right -= 1
            continue        
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1        
    return "".join(s)
    
arr = "anne"
example = func(arr)
print(example)