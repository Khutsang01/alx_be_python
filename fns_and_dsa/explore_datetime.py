# Expolore datetime module

from datetime import datetime, timedelta

# Part 1: Display the Current Date and Time
def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:", formatted_date)
    return current_date  # Return it for use in the next part

# Part 2: Calculate a Future Date
def calculate_future_date(current_date, days_to_add):
    future_date = current_date + timedelta(days=days_to_add)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print("Future date:", formatted_future_date)

# Run the script
if __name__ == "__main__":
    # Display current date and time
    current = display_current_datetime()

    # Prompt user for number of days to add
    try:
        days = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(current, days)
    except ValueError:
        print("Please enter a valid integer for the number of days.")