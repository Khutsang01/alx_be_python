# Temperature conversion tool

# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# Convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# Main logic
def main():
    try:
        # Get temperature input
        temp_input = input("Enter the temperature to convert: ").strip()
        temperature = float(temp_input)  # Validate it’s numeric

        # Get temperature unit
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == 'C':
            converted = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted}°F")
        elif unit == 'F':
            converted = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted}°C")
        else:
            raise ValueError("Invalid temperature unit. Please enter 'C' or 'F'.")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

# Run the script
if __name__ == "__main__":
    main()