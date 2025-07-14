#Personal Finance Calculator

#prompt the user to enter a monthly income and the total monthly expenses
monthly_income = float(input("Enter your monthly income: "))
total_monthly_expenses = float(input("Enter your total monthly expenses: "))

#calculate monthly savings
monthly_savings = monthly_income - total_monthly_expenses

#convert monthly savings to whole number (remove decimal)
monthly_savings = int(monthly_savings)

#calculate projected annual savings with 5% interest and converting the projected savings to whole number
annual_savings = monthly_savings * 12
projected_savings = int(annual_savings + annual_savings * 0.05)

#print the monthly savings of a user
print("Your monthly savings are $" + str(monthly_savings) + ".")

#print the projected savings of a user
print("Projected savings after one year, with interest, is: $" + str(projected_savings) + ".")