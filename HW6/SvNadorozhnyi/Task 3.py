def number_of_characters(word):
    return {i: word.count(i) for i in word}


enter_word = input("Enter your string: ")
print(number_of_characters(enter_word))