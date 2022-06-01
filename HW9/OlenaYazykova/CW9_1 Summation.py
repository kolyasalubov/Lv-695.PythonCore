num=int(input("Enter the number: "))

def summation(num:int) ->int:
    """This function finds the summation of every number from 1 to num."""

    sum=0
    for i in range(num+1):
        sum+=i
    return sum

print(summation(num))
