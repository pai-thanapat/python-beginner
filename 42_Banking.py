# 42. Banking


def show_balance(balance):

    print(f"Your balance is ${balance:.2f}")


def deposite():
    amount = float(input("Enter an amount to be deposited : "))

    if amount <= 0:

        print(f"The amount {amount} is not valid to deposit")

        return 0
    else:
        return amount


def withdraw(balance):
    amount = float(input("Enter an amount to be withdrawn : "))

    if amount <= 0:

        print(f"The amount {amount} is not valid to deposit")

        return 0
    elif amount > balance:

        print(f"Insufficient funds")

        return 0
    else:
        return amount


def main():
    balance = 0
    is_running = True

    while is_running:
        print("-------------------------------------")
        print("|          Banking Program          |")
        print("-------------------------------------")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("-------------------------------------")

        choice = input("Enter your choice (1-4) : ")

        match choice:
            case "1":
                show_balance(balance)
            case "2":
                balance += deposite()
            case "3":
                balance -= withdraw(balance)
            case "4":
                is_running = False
            case _:
                print(f"Invalid selection choice {choice}")

    print("Thank you! Have a nice day.")


if __name__ == "__main__":
    main()
