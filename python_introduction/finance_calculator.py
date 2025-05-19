monthly_income = float(input("Enter your monthly income: "))
total_monthly_expenses = float(input("Enter your total monthly expenses: "))
# Calculate the monthly savings
monthly_savings = monthly_income - total_monthly_expenses
# Print the monthly savings
print(f"Your monthly savings are: ${monthly_savings:.2f}")
# project the annual savings
annual_interest_rate = 0.05  # 5% annual interest rate
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * annual_interest_rate)
# Print the projected annual savings
print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}")