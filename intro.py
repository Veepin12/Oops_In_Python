class ATM:
    def __init__(self):
        self.pin = ""
        self.balance = 0.0

    def menu(self):
        while True:
            choice = input('''
Hello, how would you like to proceed?
1. Create PIN
2. Deposit
3. Withdraw
4. Check balance
5. Exit
Enter your choice: ''').strip()

            if choice == "1":
                self.create_pin()
            elif choice == "2":
                self.deposit()
            elif choice == "3":
                self.withdraw()
            elif choice == "4":
                self.check_balance()
            elif choice == "5":
                print("Exit")
                break
            else:
                print("Invalid option. Please try again.")

    def create_pin(self):
        self.pin = input("Enter your PIN: ").strip()
        print("PIN set successfully.")

    def deposit(self):
        if not self.pin:
            print("Please set a PIN first.")
            return

        temp_pin = input("Enter your PIN: ").strip()
        if temp_pin != self.pin:
            print("Invalid PIN.")
            return

        try:
            amount = float(input("Enter the amount: "))
        except ValueError:
            print("Invalid amount.")
            return

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        self.balance += amount
        print(f"Deposit successful. New balance: {self.balance:.2f}")

    def withdraw(self):
        if not self.pin:
            print("Please set a PIN first.")
            return

        temp_pin = input("Enter your PIN: ").strip()
        if temp_pin != self.pin:
            print("Invalid PIN.")
            return

        try:
            amount = float(input("Enter the amount: "))
        except ValueError:
            print("Invalid amount.")
            return

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        if amount > self.balance:
            print("Insufficient funds.")
            return

        self.balance -= amount
        print(f"Withdrawal successful. Remaining balance: {self.balance:.2f}")

    def check_balance(self):
        if not self.pin:
            print("Please set a PIN first.")
            return

        temp_pin = input("Enter your PIN: ").strip()
        if temp_pin != self.pin:
            print("Invalid PIN.")
            return

        print(f"Current balance: {self.balance:.2f}")


if __name__ == "__main__":
    ATM().menu()