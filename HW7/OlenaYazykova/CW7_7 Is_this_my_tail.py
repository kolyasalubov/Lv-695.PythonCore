body=input("Enter the name of the animal: ")
tail=input("Enter the first letter of the tail: ")

def correct_tail(body, tail):
    sub = body[len(body)-1:]
    if sub == tail:
        return True
    else:
        return False

if correct_tail(body, tail)==True:
    print ("It's a right tail.")
else:
    print ("It's a wrong tail.")