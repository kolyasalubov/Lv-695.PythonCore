def correct_tail(body, tail):
    if body[-1] == tail:
        return True
    elif body[-1] != tail:
        return False

print(correct_tail("Fox", "y"))
