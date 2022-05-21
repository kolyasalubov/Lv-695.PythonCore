def zero_fuel(distance_to_pump, mpg, fuel_left):
    if distance_to_pump / mpg <= fuel_left:
        return True
    else:
        return False

print(zero_fuel(100, 50, 1))
print(zero_fuel(50, 50, 1))