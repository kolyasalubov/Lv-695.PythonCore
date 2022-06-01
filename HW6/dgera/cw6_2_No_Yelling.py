def filter_words(st):
    st_new = []
    character_prev = ''
    for character in st:
        if character == ' ' and character_prev == ' ':
            continue
        else:
            st_new.append(character)
        character_prev = character
    return ''.join(st_new).strip().capitalize()