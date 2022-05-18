num=int(input("Enter a number:"))
print(f"Before: {num} is {type(num)}")
def number_to_string(num):
    return str(num)
print(f"After: {num} is {type(number_to_string(num))}")