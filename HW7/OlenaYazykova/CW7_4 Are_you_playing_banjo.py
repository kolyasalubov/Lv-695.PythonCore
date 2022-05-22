name=input("Enter your name: ")

def are_you_playing_banjo(name:str)->str:
    """This function gives a string whether the person plays the banjo depending on his name."""

    if name[0]=="R" or  name[0]=="r":
        return f"{name} plays banjo"
    else:
        return f"{name} does not play banjo"

print(are_you_playing_banjo(name))