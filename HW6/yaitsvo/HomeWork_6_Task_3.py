def char_counter(stroka):
    list_of_chars = []
    for char in stroka:
        if char not in list_of_chars:
            list_of_chars.append(char)
    result = dict.fromkeys(list_of_chars, 0)
    for char in stroka:
        count = 0
        for chars in stroka:
            if char == chars:
                count += 1
        result[char] = count
    print(result)

s = input().lower()

char_counter(s)
