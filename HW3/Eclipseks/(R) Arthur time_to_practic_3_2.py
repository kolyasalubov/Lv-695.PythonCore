digitl_natural = input("Write 4digit numbers:")

dobutoc =  int(str(digitl_natural)[0]) * int(str(digitl_natural)[1]) * int(str(digitl_natural)[2]) * int(str(digitl_natural)[3])
print(f"{digitl_natural[0]} * {digitl_natural[1]} * {digitl_natural[2]} * {digitl_natural[3]} = ", dobutoc)
print()

revers = int(''.join(reversed(digitl_natural)))
print(f"{digitl_natural} in revers = ", revers)
print()

sort = int("".join(sorted(digitl_natural)))
print(f"{digitl_natural} sort =", sort)
 