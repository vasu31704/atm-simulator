class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited {amount}. New balance is {self.balance}"
        else:
            return "Invalid deposit amount"

    def withdraw(self, amount):
        if amount > self.balance or amount <= 0:
            return "Invalid withdrawal amount or insufficient funds"
        else:
            self.balance -= amount
            return f"Withdrew {amount}. New balance is {self.balance}"


def main():
    atm = ATM(1000)
    while True:
        print("\n1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            print("Balance:", atm.check_balance())
            print("Thank you for using our ATM. Goodbye!")
        elif choice == '2':
            amount = float(input("Enter amount to deposit: "))
            print(atm.deposit(amount))
            print("Thank you for using our ATM. Goodbye!")
        elif choice == '3':
            amount = float(input("Enter amount to withdraw: "))
            print(atm.withdraw(amount))
            print("Thank you for using our ATM. Goodbye!")
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
