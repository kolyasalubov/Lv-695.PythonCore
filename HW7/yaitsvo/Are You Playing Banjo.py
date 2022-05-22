def are_you_playing_banjo(name):
    if name.lower().startswith('r'):
        return f'{name} plays banjo'
    return f'{name} does not play banjo'
print(are_you_playing_banjo('Rose'))