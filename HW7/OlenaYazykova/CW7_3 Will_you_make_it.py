distance_to_pump=float(input("Enter the distance to pump (miles): "))
mpg=float(input("Enter the speed of your car (miles per gallon): "))
fuel_left=float(input("Enter how many gallons left: "))

def zero_fuel(distance_to_pump:float, mpg:float, fuel_left:float)->bool:
    """This function checks if there are enough gallons to get to the pump."""

    if distance_to_pump/mpg<=fuel_left:
        return True
    else:
        return False

if zero_fuel(distance_to_pump, mpg, fuel_left)==1:
    print("You can get to the pump.")
else:
    print("You can't get to the pump.")