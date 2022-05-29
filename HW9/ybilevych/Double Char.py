def double_char(s):
    f = ''
    for i in range(len(s)):
        f += s[i]*2
    return f
    
print(double_char('Hello World!'))