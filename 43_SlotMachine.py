# 43. Slot Machine

import random


def spin_row():
    symbols = ["🍒", "🍉", "🍋", "🔔", "⭐"]

    return [random.choice(symbols) for _ in range(3)]


def print_row(row):

    print("---------------------------------------------")
    print("           " + "    |    ".join(row) + "             ")
    print("---------------------------------------------")


def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        match row[0]:
            case "🍒":
                return bet * 3
            case "🍉":
                return bet * 4
            case "🍋":
                return bet * 5
            case "🔔":
                return bet * 10
            case "⭐":
                return bet * 20

    return 0


def main():
    balance = 100

    print("---------------------------------------------")
    print("           Welcome to Python Slots           ")
    print("               🍒 🍉 🍋 🔔 ⭐             ")
    print("---------------------------------------------")

    while balance > 0:

        print(f"Current balance : {balance}")

        bet = input("Place your bet amount ('n' to stop) : ")

        if bet.lower() == "n":
            break

        if not bet.isdigit():
            print("Invalid amount.")
            continue

        bet = int(bet)

        if bet <= 0:
            print("Bet must be greater than zero")
            continue
        elif bet > balance:
            print("Insufficient funds.")
            continue

        balance -= bet

        row = spin_row()
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"YOU WON ${payout}.")
        else:
            print("Sorry, you lost this round.")

        balance += payout

    print("---------------------------------------------")
    print(f"Game end. Your final balance is ${balance}")
    print("---------------------------------------------")


if __name__ == "__main__":
    main()
