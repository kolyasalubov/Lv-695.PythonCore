length_of_list=int(input("Set the length of the array: "))
l=[]
for i in range(0,length_of_list):
    l.append(input("Enter {i} number: "))

def reverse_list(l:list) ->list:
    """return a list with the reverse order of l"""

    #the first way
    #return l[::-1]
    #the second way
    return list(reversed(l))

#l=[1,2,3,4,5]
print (reverse_list(l))