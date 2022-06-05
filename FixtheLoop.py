def list_animals(animals):
    return ''.join(
        '{}. {}\n'.format(i, animal)
        for i, animal in enumerate(animals, 1)
    )