class ConversionNotPossibleException(Exception):
    pass


def incompatibleUnits(fromUnit, toUnit):
    raise ConversionNotPossibleException(f"Error: cannot convert between {fromUnit} and {toUnit}. Can only convert temperature units with other temperature units and distance units with other distance units.")


def convert(fromUnit, toUnit, value):
    # Check all temperature conversions
    # Fahrenheit to C, K, F
    if fromUnit == "F":
        if toUnit == "C":
            value = (value - 32) * 5 / 9
        elif toUnit == "K":
            value = (value - 32) * 5 / 9 + 273.15
        elif toUnit == "F":
            value = value
        else:
            incompatibleUnits(fromUnit, toUnit)

    # Celsius to K, F, C
    elif fromUnit == "C":
        if toUnit == "K":
            value = value + 273.15
        elif toUnit == "F":
            value = (value * 9 / 5) + 32
        elif toUnit == "C":
            value = value
        else:
            incompatibleUnits(fromUnit, toUnit)

    # Kelvin to C, F, K
    elif fromUnit == "K":
        if toUnit == "C":
            value = value - 273.15
        elif toUnit == "F":
            value = (value - 273.15) * 9 / 5 + 32
        elif toUnit == "K":
            value = value
        else:
            incompatibleUnits(fromUnit, toUnit)

    # Yards to meters, miles, yards
    elif fromUnit == "Yards":
        if toUnit == "Meters":
            value *= 0.9144
        elif toUnit == "Miles":
            value /= 1760
        elif toUnit == "Yards":
            value = value
        else:
            incompatibleUnits(fromUnit, toUnit)

    # Meters to yards, miles, meters
    elif fromUnit == "Meters":
        if toUnit == "Yards":
            value /= 0.9144
        elif toUnit == "Miles":
            value *= 0.000621371
        elif toUnit == "Meters":
            value = value
        else:
            incompatibleUnits(fromUnit, toUnit)

    # Miles to yards, meters, miles
    elif fromUnit == "Miles":
        if toUnit == "Yards":
            value *= 1760
        elif toUnit == "Meters":
            value *= 1609.344
        elif toUnit == "Miles":
            value = value
        else:
            incompatibleUnits(fromUnit, toUnit)

    # Unsupported units
    else:
        incompatibleUnits(fromUnit, toUnit)

    return value * 1.0
