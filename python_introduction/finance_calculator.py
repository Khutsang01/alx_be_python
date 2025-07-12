#Personal Finance Calculator

#promt the user to enter a monthly income and the total monthly expence
monthly_income = int(input("Enter your monthly income "))
total_monthly_expences = int(input("Enter your total monthly expences "))

#calculate monthly savings
monthly_savings = monthly_income - total_monthly_expences

#project annual savings
projected_savings = (monthly_savings * 12) + (monthly_savings * 12 * 0.05)

#print the monthly savings of a user
print(f"Your monthly savings are ${monthly_savings}")

#print the projected savings of a user
print(f"Projected savings after one year, with interest, is: ${projected_savings}")