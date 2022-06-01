def are_you_playing_banjo(name):
    return(f"{name} plays banjo" if name[0].title() == "R" else f"{name} does not play banjo")
    

print(are_you_playing_banjo("Oleg"))
print(are_you_playing_banjo("Rob"))
    