 # Personal Daily Reminder

# Loop to ensure valid input is entered
while True:
    task = input("Enter your task: ").strip()
    priority = input("Priority (high/medium/low): ").lower().strip()
    time_bound = input("Is it time-bound? (yes/no): ").lower().strip()

    # Basic validation for priority
    if priority not in ["high", "medium", "low"]:
        print("Invalid priority. Please enter 'high', 'medium', or 'low'.\n")
        continue

    # Basic validation for time_bound
    if time_bound not in ["yes", "no"]:
        print("Invalid input for time-bound. Please enter 'yes' or 'no'.\n")
        continue

    # If all inputs are valid, break the loop
    break

# Match case to react to priority
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"

# Modify reminder based on time sensitivity
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder = "Note: " + reminder + ". Consider completing it when you have free time."

# Print the final reminder
print(f"Reminder: {reminder}")