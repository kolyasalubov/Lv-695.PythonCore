def correct_tail(body, tail):
    if body[-1] == tail[0]:
        return True
    else:
        return False

print(correct_tail("Fox", "x"))
print(correct_tail("Rhino", "x"))
