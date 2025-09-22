


def func(s):
    s = s.strip().split()
    return " ".join(s[::-1])
    
    
s = "   Hello    world   nalkdfn  "
print(func(s))