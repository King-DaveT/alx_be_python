# Define variables, hours and seconds
x = input("Enter your monthly income:")
y = input("Enter your total monthly expenses:")
monthly_income =float(x)
monthly_expenses = float(y)
monthly_savings = float(monthly_income - monthly_expenses)
projected_savings = (monthly_savings * 12) + (monthly_savings * 12 * 0.05)
#Converting hours to seconds
print("Your monthly savings are", monthly_savings)
print("Projected savings after one year""," "with interest" "," "is", projected_savings)

