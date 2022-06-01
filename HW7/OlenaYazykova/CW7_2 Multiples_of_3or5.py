number=int(input("Enter an integer number: "))

def solution(number:int) ->int:
    """This function returns the sum of all the multiples of 3 or 5 below the number passed in. """

    sum1=0
    if number>0:
        for i in range(1,number):
            if i%3==0 or i%5==0:
                sum1+=i
    return sum1 
print(solution(number))
