
print("Welcome to Shiv Bank")

PIN = 1234567
chances = 3
balance = 999.99

# PIN verification
while chances > 0:
    try:
        pin = int(input("Enter your PIN: "))
    except ValueError:
        print("Please enter a valid numeric PIN.")
        continue

    if pin == PIN:
        print("\nLogin successful!")

        # ATM menu
        while True:
            print("\n----- ATM MENU -----")
            print("1. Check Balance")
            print("2. Withdraw Money")
            print("3. Deposit Money")
            print("4. Return Card")

            try:
                option = int(input("Enter your choice: "))
            except ValueError:
                print("Please enter a valid option.")
                continue

            if option == 1:
                print(f"Your current balance is: ₹{balance:.2f}")

            elif option == 2:
                try:
                    amount = float(input("Enter withdrawal amount: ₹"))
                except ValueError:
                    print("Please enter a valid amount.")
                    continue

                if amount <= 0:
                    print("Amount must be greater than zero.")
                elif amount > balance:
                    print("Insufficient balance.")
                else:
                    balance -= amount
                    print("Withdrawal successful!")
                    print(f"Remaining balance: ₹{balance:.2f}")

            elif option == 3:
                try:
                    amount = float(input("Enter deposit amount: ₹"))
                except ValueError:
                    print("Please enter a valid amount.")
                    continue

                if amount <= 0:
                    print("Amount must be greater than zero.")
                else:
                    balance += amount
                    print("Deposit successful!")
                    print(f"Updated balance: ₹{balance:.2f}")

            elif option == 4:
                print("Your card has been returned.")
                print("Thank you for using Shiv Bank!")
                break

            else:
                print("Invalid choice. Please select 1 to 4.")

        break

    else:
        chances -= 1
        print(f"Incorrect PIN. Attempts remaining: {chances}")

        if chances == 0:
            print("You have exceeded the maximum attempts.")

