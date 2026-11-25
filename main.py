import json
expenses: dict[str, float]
try:
    with open("expenses.json", "r") as f:
        expenses = json.load(f)
except FileNotFoundError:
     expenses = {}
print("--- Expense Summary ---")
for category, amount in expenses.items():
    print(category, ":", amount)
print("---")
print("Total:", sum(expenses.values()))
while True:
    new_category = input("Enter a category (or type done to finish, remove to delete one): ")
    if new_category == "done":
        break
    if new_category =="remove":
        to_remove=input("which category do you want to remove? ")
        if to_remove in expenses:
            del expenses[to_remove]
            print("Removed:", to_remove)
        else:
            print("That category isn't in your list.")
        continue
    try:
        new_amount = float(input("Enter an amount: "))
    except ValueError:
        print("That's not a number. Try again.")
        continue
    expenses[new_category] = expenses.get(new_category, 0) + new_amount
    print("Added:", new_category, "-", new_amount)

print("Final total:", sum(expenses.values()))
with open("expenses.json","w") as f:
    json.dump(expenses, f)
