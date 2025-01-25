# Write a python program using function to convert Celsius to fahrenheit.

def celsius_to_fahrenheit(celsius):
    # Formula for conversion: (Celsius * 9/5) + 32
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def main():
    # Ask user for input in Celsius
    celsius = float(input("Enter temperature in Celsius: "))
    
    # Convert Celsius to Fahrenheit
    fahrenheit = celsius_to_fahrenheit(celsius)
    
    # Display the result
    print(f"{celsius}°C is equal to {fahrenheit}°F")

# Call the main function
main()
