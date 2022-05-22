length_of_list_sheep=int(input("Set the length of the array: "))
sheep=[]
for i in range(0,length_of_list_sheep):
    sheep.append(bool(input("Enter '1' if the sheep is present or '' if the sheep is absent: ")))

def count_sheeps(sheep:list)->int:
    """ function that counts the number of sheep present in the array """

    count_sheep=0
    for i in range(0,len(sheep)):
        if sheep[i]==True:
            count_sheep+=1
    return count_sheep

print(f"The number of sheep that are present is {count_sheeps(sheep)}.")