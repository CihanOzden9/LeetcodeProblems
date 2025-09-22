my_input = ["5","2","c","d","+"]

def func(ops:list[str]):
    
    stack = []
    
    for op in ops:
        if op =="c":
            stack.pop()
        elif op == "+":
            stack.append(stack[-1] + stack[-2])
        elif op == "d":
            stack.append(2 * stack[-1])
        else:
            stack.append(int(op))
    return sum(stack)

deneme = func(my_input)
print(deneme)