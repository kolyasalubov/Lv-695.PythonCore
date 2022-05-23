numb_of_anim=int(input("Enter the number of animals: "))
animals=[]
for i in range(numb_of_anim):
    animals.append(input(f"Enter animal name {i+1}: "))
print(animals)

def list_animals(animals:list) ->str:
    """This function returns a string as a numbered list of animals."""

    list = ''
    for i in range(len(animals)):
        list += str(i + 1) + '. ' + animals[i] + '\n'
    return list

print(list_animals(animals))