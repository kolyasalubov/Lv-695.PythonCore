def are_you_playing_banjo(name):
    if name[0] in {'r', 'R'}:
        return f"{name} plays banjo"
    else:
        return f"{name} does not play banjo"