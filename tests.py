
from conversions import (
    convertCelsiusToKelvin,
    convertCelsiusToFahrenheit,
    convertFahrenheitToCelsius,
    convertFahrenheitToKelvin,
    convertKelvinToCelsius,
    convertKelvinToFahrenheit
)

from conversions_refactored import (
    convert
)
if __name__ == "__main__":

    c_to_k_test_cases = [0.0, -273.0, 2000.0, 20.0, -40.0]
    c_to_f_test_cases = [0.0, 50.0, -50.0, -7.0, 8.0]

    f_to_c_test_cases = [0.0, 450.0, 32.0, 212.0, -4.0]
    f_to_k_test_cases = [0.0, -460.0, -40.0, 99.0, 32.0]

    k_to_c_test_cases = [0.0, 244.0, 274.0, 233.0, 268.0]
    k_to_f_test_cases = [0.0, 250.0, 257.0, 239.0, 282.0]

    c_to_c_test_cases = [0.0, 25.5, -17.2, 120.0, -273.15]  
    f_to_f_test_cases = [32.0, 90.6, -40.0, 212.0, -459.67]  
    k_to_k_test_cases = [0.0, 273.15, 310.15, 77.0, 500.5]   



    miles_to_yards_test_cases = [2.0, 10.0, 7.5, 4.0, 100.0]
    miles_to_meters_test_cases = [1.0, 12.0, 4.4, 2.1, 50.0]

    yards_to_miles_test_cases = [1.0, 60.0, 7.3, 40.0, 5.0]
    yards_to_meters_test_cases = [1.0, 0.8, 9.0, 37.0, 8.3, 5.0]

    miles_to_meters_test_cases = [1.0, 55.0, 11.0, 23.5, 0.4]
    meters_to_miles_test_cases = [1.0, 0.9, 44.0, 68.0, 200.0]

    meters_to_meters_test_cases = [43.0, 23.2, 323.3, 111.1, 2.0]
    miles_to_miles_test_cases = [1.0, 2.5, 3.75, 4.2, 5.8]
    yards_to_yards_test_cases = [10.0, 20.5, 30.75, 40.2, 50.8]

    incompatible_units_test_cases = [23.5, 230.0, -50.1, 43.0, -60.3]
    

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
        print(f"The result f or {fk}°Fahrenheit is: {fk}°F = {conversion:.2f}°K")
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


    print("Refactored Test Cases: Temperatures")
    for i in range(5):
        print(f"Celsius to Fahrenheit is: {convert('C', 'F', c_to_f_test_cases[i])}°F")
        print(f"Fahrenheit to Celsius is: {convert('F', 'C', f_to_f_test_cases[i])}°F")
        print(f"Fahrenheit to Kelvin is: {convert('F', 'K', f_to_k_test_cases[i])}°K")
        print(f"Kelvin to Celsius is: {convert('K', 'C', k_to_c_test_cases[i])}°C")
        print(f"Kelvin to Fahrenheit is: {convert('K', 'F', k_to_f_test_cases[i])}°F")
        print(f"Celsius to Celsius is: {convert('C', 'C', c_to_c_test_cases[i])}°F")
        print(f"Fahrenheit to Fahrenheit is: {convert('F', 'F', f_to_f_test_cases[i])}°F")
        print(f"Kelvin to Kelvin is: {convert('K', 'K', k_to_k_test_cases[i])}°K")
        print()

    print()
    print("Refactored Test Cases: Distances")
    for i in range(5):
        print(f"Miles to Yards is: {convert('Miles', 'Yards', miles_to_yards_test_cases[i])} Yards")
        print(f"Miles to Meters is: {convert('Miles', 'Meters', miles_to_meters_test_cases[i])} Meters")
        print(f"Yards to Miles is: {convert('Yards', 'Miles', yards_to_miles_test_cases[i])} Miles")
        print(f"Yards to Meters is: {convert('Yards', 'Meters', yards_to_meters_test_cases[i])} Meters")
        print(f"Miles to Meters is: {convert('Miles', 'Meters', miles_to_meters_test_cases[i])} Meters")
        print(f"Meters to Miles is: {convert('Meters', 'Miles', meters_to_miles_test_cases[i])} Miles")
        print(f"Meters to Meters is: {convert('Meters', 'Meters', meters_to_meters_test_cases[i])} Meters")
        print(f"Miles to Miles is: {convert('Miles', 'Miles', miles_to_miles_test_cases[i])} Miles")
        print(f"Yards to Yards is: {convert('Yards', 'Yards', yards_to_yards_test_cases[i])} Yards")
        print()

    print()
    print("Refactored Test Cases: Incompatible Units")
    for i in range(5):
        print(f"Miles to Fahrenheit is: {convert('Miles', 'F', incompatible_units_test_cases[i])}")
        print(f"Miles to Celsius is: {convert('Miles', 'C', incompatible_units_test_cases[i])}")
        print(f"Miles to Kelvin is: {convert('Miles', 'K', incompatible_units_test_cases[i])}")
        print(f"Meters to Fahrenheit is: {convert('Meters', 'F', incompatible_units_test_cases[i])}")
        print(f"Meters to Celsius is: {convert('Meters', 'C', incompatible_units_test_cases[i])}")
        print(f"Meters to Kelvin is: {convert('Meters', 'K', incompatible_units_test_cases[i])}")
        print(f"Yards to Fahrenheit is: {convert('Yards', 'F', incompatible_units_test_cases[i])}")
        print(f"Yards to Celsius is: {convert('Yards', 'C', incompatible_units_test_cases[i])}")
        print(f"Yards to Kelvin is: {convert('Yards', 'K', incompatible_units_test_cases[i])}")
        print(f"Fahrenheit to Miles is: {convert('F', 'Miles', incompatible_units_test_cases[i])}")
        print(f"Fahrenheit to Yards is: {convert('F', 'Yards', incompatible_units_test_cases[i])}")
        print(f"Fahrenheit to Meters is: {convert('F', 'Meters', incompatible_units_test_cases[i])}")
        print(f"Celsius to Miles is: {convert('C', 'Miles', incompatible_units_test_cases[i])}")
        print(f"Celsius to Yards is: {convert('C', 'Yards', incompatible_units_test_cases[i])}")
        print(f"Celsius to Meters is: {convert('C', 'Meters', incompatible_units_test_cases[i])}")
        print(f"Kelvin to Miles is: {convert('K', 'Miles', incompatible_units_test_cases[i])}")
        print(f"Kelvin to Yards is: {convert('K', 'Yards', incompatible_units_test_cases[i])}")
        print(f"Kelvin to Meters is: {convert('K', 'Meters', incompatible_units_test_cases[i])}")
        print()






    
