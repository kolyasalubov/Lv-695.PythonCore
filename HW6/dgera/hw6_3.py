def symbol_counter(*args) -> dict:
    """
    Calculates the number of characters included in the string
        Returns:
            dict: 'key' is leter, 'value' is number of letters in the string
    """
    
    dict_counter = {}
    for symbol in args:
        dict_counter[symbol] = args.count(symbol)
    return dict_counter


print('Please enter a string:')
user_string = input()

result_dict = symbol_counter(*user_string)

print('\n======= Result =======')
# print(symbol_counter(*user_string))
for key, value in result_dict.items():
    print(f'Symbol "{key}" appears in the string {value} time/s')
