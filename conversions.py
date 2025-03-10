
def convertCelsiusToKelvin(celsius):
    """Takes in a float representing a Celsius measurement, and returns that temperature converted into Kelvins"""
    kelvin = 0
    kelvin = celsius + 273.15
    if kelvin < 0:
        kelvin = 0
    
    return kelvin


def convertCelsiusToFahrenheit(celsius):
    """Takes in a float representing a Celsius measurement, and returns that temperature converted into Fahrenheit"""
    fahrenheit = 0
    fahrenheit = (celsius * 9/5) + 32
    
    return fahrenheit

def convertFahrenheitToCelsius(fahrenheit):
    """Takes in a float representing a Fahrenheit measurement, and returns that temperature converted into Celsius"""
    celsius = 0
    celsius = (fahrenheit - 32) * 5/9
    
    return celsius

def convertFahrenheitToKelvin(fahrenheit):
    """Takes in a float representing a Fahrenheit measurement, and returns that temperature converted into Kelvin"""
    kelvin = 0
    kelvin = (fahrenheit - 32) * 5/9 + 273.15
    if kelvin < 0:
        kelvin = 0
    
    return kelvin

def convertKelvinToCelsius(kelvin):
    """Takes in a float representing a Kelvin measurement, and returns that temperature converted into Celsius"""
    celsius = 0
    celsius = kelvin - 273.15
    
    return celsius

def convertKelvinToFahrenheit(kelvin):
    """Takes in a float representing a Kelvin measurement, and returns that temperature converted into Fahrenheit"""
    fahrenheit = 0
    fahrenheit = (kelvin - 273.15) * 9/5 + 32
    
    return fahrenheit


if __name__ == "__main__":

    c_to_k_test_cases = [0, -273, 2000, 20, -40]
    c_to_f_test_cases = [0, 50, -50, -7, 8]

    f_to_c_test_cases = [0, 450, 32, 212, -4]
    f_to_k_test_cases = [0, -460, -40, 99, 32]

    k_to_c_test_cases = [0, 244, 274, 233, 268]
    k_to_f_test_cases = [0, 250, 257, 239, 282]

    

    print("Celsius to Kelvin Conversion Tests:")
    for ck in c_to_k_test_cases:
        conversion = convertCelsiusToKelvin(ck)
        print(f"The result for {ck}°Celsius is: {ck}°C = {conversion:.2f}°K")
    print()
    
    print("\nCelsius to Fahrenheit Conversion Tests:")
    for cf in c_to_f_test_cases:
        conversion = convertCelsiusToFahrenheit(cf)
        print(f"The result for {cf}°Celsius is: {cf}°C = {conversion:.2f}°F")
    print()
    
    print("Fahrenheit to Celsius Conversion Tests:")
    for fc in f_to_c_test_cases:
        conversion = convertFahrenheitToCelsius(fc)
        print(f"The result for {fc}°Fahrenheit is: {fc}°F = {conversion:.2f}°C")
    print()
    
    print("Fahrenheit to Kelvin Conversion Tests:")
    for fk in f_to_k_test_cases:
        conversion = convertFahrenheitToKelvin(fk)
        print(f"The result for {fk}°Fahrenheit is: {fk}°F = {conversion:.2f}°K")
    print()

    print("Kelvin to Celsius Conversion Tests:")
    for kc in k_to_c_test_cases:
        conversion = convertKelvinToCelsius(kc)
        print(f"The result for {kc}°Kelvin is: {kc}°K = {conversion:.2f}°C")
    print()

    print("Kelvin to Fahrenheit Conversion Tests:")
    for kf in k_to_f_test_cases:
        conversion = convertKelvinToFahrenheit(kf)
        print(f"The result for {kf}°Kelvin is: {kf}°K = {conversion:.2f}°F")
    print()
        
