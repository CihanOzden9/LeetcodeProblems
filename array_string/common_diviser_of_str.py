import math
def func(str1, str2):
    if str1 + str2 != str2 + str1:
        return " "
    gcd_len = math.gcd(len(str1), len(str2))
    return str1[:gcd_len]
        
a = "abababab"
b = "ababab"
deneme = func(a, b)
print(deneme)
    
    