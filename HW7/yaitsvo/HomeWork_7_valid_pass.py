import re
s = "ABs3!1"
if len(s) < 6 or len(s) > 16:
    print('PASS INVALID: Password must be between 6 and 16 characters')
elif len(re.findall('[A-Z]', s)) == 0:
    print('PASS INVALID: No uppercase letters')
elif len(re.findall('[a-z]', s)) == 0:
    print('PASS INVALID: No lowercase letters')
elif len(re.findall('[0-9]', s)) == 0:
    print('PASS INVALID: No numbers')
elif len(re.findall('[$#@!?.*_()^=+%]', s)) == 0:
    print('PASS INVALID: No special symbols')
else:
    print('VALID PASS')
