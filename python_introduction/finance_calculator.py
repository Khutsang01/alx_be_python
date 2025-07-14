#Personal Finance Calculator

#prompt the user to enter a monthly income and the total monthly expenses
monthly_income = float(input("Enter your monthly income: "))
total_monthly_expenses = float(input("Enter your total monthly expenses: "))

#calculate monthly savings
monthly_savings = monthly_income - total_monthly_expenses

#project annual savings
annual_savings = monthly_savings * 12
projected_savings = annual_savings + (monthly_savings * 12 * 0.05)

#print the monthly savings of a user
print(f"Your monthly savings are ${monthly_savings}.")

#print the projected savings of a user
print(f"Projected savings after one year, with interest, is: ${projected_savings}.")