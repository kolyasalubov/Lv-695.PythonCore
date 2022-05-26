name=input("Enter your name:")
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
         return "Hello, {name}!".format(name=name)
print(greet(name))
