name=input("What is your name?")
key=True
while key:
    age=input("How old are you?")
    if age.isdigit():
        key=False
    else:
        print("Data format error!")
place_of_residence=input("Where do you live?")
print(f"Hello, {name},")
print(f"Your age is {age} years old,")
print(f"You live in {place_of_residence}.")
