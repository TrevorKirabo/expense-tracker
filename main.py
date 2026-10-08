expenses= {"food": 10.50, "gas": 25.00, "coffee": 7.75}
for category, amount in expenses.items():
    print("Expense:", category, "-", amount)
total=sum(expenses.values())
print("Total:", total)
new_category = input("Enter a category: ")
new_amount = float(input("Enter an amount: "))

expenses[new_category] = new_amount

print("Updated total:", sum(expenses.values()))