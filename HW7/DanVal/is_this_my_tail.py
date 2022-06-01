def correct_tail(body, tail):
    sub = body.split()[0][-1]
    if sub == tail:
        return True
    else:
        return False
