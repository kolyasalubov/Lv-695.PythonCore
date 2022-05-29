print("Are you playing banjo?")
def areYouPlayingBanjo(name):
    if name[0] == 'r':
        return print(name+ ''+" plays banjo")
    else:
         return print(name+''+" does not play banjo")
areYouPlayingBanjo(str(input().lower()))

