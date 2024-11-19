
expenses = []

def add_expense():
    name = input("enter your name: ")
    description = input("Enter description: ")
    amount = float(input("Enter amount: "))
    expenses.append({"description": description, "amount": amount})
    print("Expense added!")
    with open(f'{name}.txt', 'a') as file:
        file.write(f"=================\ndescription : {description}\namount : {amount}\n")

def view_expenses():
    name = input("enter your name: ")
    # for i, expense in enumerate(expenses, 1):
    #     print(f"{i}. {expense['description']} - ${expense['amount']}")
    with open(f"{name}.txt" , "r") as file:
        a = i=file.readlines()
        for i in a:
            print(i)

def calculate_total():
    total = sum(expense["amount"] for expense in expenses)
    print("Total Amount Spent: $", total)

while True:
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Calculate Total")
    print("4. Quit")
    choice = input("Choose an option: ")

    if choice == '1':
        add_expense()
    elif choice == '2':
        view_expenses()
    elif choice == '3':
        calculate_total()
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")