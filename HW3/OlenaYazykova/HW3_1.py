zen_of_python_line10="Errors should never pass silently."
exist_better=zen_of_python_line10.count("better")
exist_never=zen_of_python_line10.count("never")
exist_is=zen_of_python_line10.count("is")
if exist_better==1:
    print(f'Word "better" found {exist_better} time')
else:
    print(f'Word "better" found {exist_better} times')
if exist_never==1:
    print(f'Word "never" found {exist_never} time')
else:
    print(f'Word "never" found {exist_never} times')
if exist_is==1:
    print(f'Word "is" found {exist_is} time')
else:
     print(f'Word "is" found {exist_is} times')
print(zen_of_python_line10.upper())
print(zen_of_python_line10.replace("i","&"))
