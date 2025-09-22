def func(s):
    brackets = {"(":")",
                "{":"}",
                "[":"]"}
    stack = []
    
    for ch in s:
        if ch in brackets:
            stack.append(ch)
        else:
            if not stack:
                return False
            last = stack.pop()
            if brackets[last] != ch:
                return False
    return not stack
    
a = func("()[](")
print(a)

    