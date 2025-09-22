

def func(chars):
    i = 0 #dizi döngüsü
    res = 0
    
    while i < len(chars):
        char = chars[i]
        group_len = 1
        
        while i + group_len < len(chars) and chars[i + group_len] == char:
            group_len += 1 # sayaç görevi
        
        chars[res] = char
        res += 1
        if group_len > 1:
            for digit in str(group_len):
                 chars[res] = digit
                 res += 1
        
        i += group_len
        
    return res

arr = ["a","a","b","b","b"]
print(func(arr))
        
        