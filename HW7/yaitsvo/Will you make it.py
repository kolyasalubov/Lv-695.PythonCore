def zero_fuel(distance_to_pump, mpg, fuel_left):
    return distance_to_pump <= mpg * fuel_left
print((zero_fuel(100, 50, 1)))

