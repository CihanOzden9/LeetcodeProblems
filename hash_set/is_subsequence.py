

def func(s,t):
    # s = sub
    # t = parent

    t_ctrl = s_ctrl = 0
    while s_ctrl < len(s) and t_ctrl < len(t):
        if t[t_ctrl] == s[s_ctrl]:
            s_ctrl += 1
        t_ctrl += 1
    return s_ctrl == len(s)
        
            

print(func("abc","atbhjc"))
