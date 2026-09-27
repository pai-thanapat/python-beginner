# 17. Compound Interest Calculator

principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter the principle amount: "))

    if principle < 0:
        print("Principle amount must be greater than 0")
    else:
        break

print(f"Principle amount: {principle}")

while True:
    rate = float(input("Enter the interest rate (in %): "))

    if rate < 0:
        print("Interest rate must be greater than 0")
    else:
        break

print(f"Interest rate: {rate}%")

while True:
    time = int(input("Enter the time period (in years): "))

    if time < 0:
        print("Time period must be greater than 0")
    else:
        break

print(f"Time period: {time} years")

total = principle * (1 + (rate / 100)) ** time

print(f"Total amount after {time} years: {total:.2f}")
