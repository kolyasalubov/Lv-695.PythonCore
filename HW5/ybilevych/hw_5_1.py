x = []
y= []
f = []

for i in range(1, 11):
    if i % 2 == 0:
        x.append(i)
    elif i % 3 == 0:
        y.append(i)
    elif i % 2 != 0 and i % 3 != 0:
        f.append(i)
print(
    f"Even numbers divisible by 2: {x}\nOdd numbers divisible by 3: {y}\nNumbers that are not divisible by 2 and 3: {f}"
)    
