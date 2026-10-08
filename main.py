expenses= {"food": 10.50, "gas": 25.00, "coffee": 7.75}
for category, amount in expenses.items():
    print("Expense:", category, "-", amount)
total=sum(expenses.values())
print("Total:", total)