def are_you_playing_banjo(name):
    if name[0] in ('R', 'r'):
        name += " plays banjo"
    else:
        name += " does not play banjo"
    return name