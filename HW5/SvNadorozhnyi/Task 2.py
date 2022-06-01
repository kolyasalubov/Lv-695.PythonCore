while True:
    user_login = input("Enter your login: ")

    if user_login == "First":
        print(f"Welcome {user_login}")
        break
    else:
        print("Try again or try to restore your login")
        continue
