# 15. Format Specifier

price1 = 3000.14159
price2 = -1987.65
price3 = 1200000.34

# Decimal Places
print(f"Price 1 : {price1:.3f}")
print(f"Price 2 : {price2:.2f}")
print(f"Price 3 : {price3:.1f}")

print("------------------------------")

# Width
print(f"Price 1 : ${price1:10}")
print(f"Price 2 : ${price2:10}")
print(f"Price 3 : ${price3:10}")

print("------------------------------")

# Leading Zeros
print(f"Price 1 : ${price1:010}")
print(f"Price 2 : ${price2:010}")
print(f"Price 3 : ${price3:010}")

print("------------------------------")

# Left Justify
print(f"Price 1 : {price1:<10}$")
print(f"Price 2 : {price2:<10}$")
print(f"Price 3 : {price3:<10}$")

print("------------------------------")

# Right Justify
print(f"Price 1 : {price1:>10}$")
print(f"Price 2 : {price2:>10}$")
print(f"Price 3 : {price3:>10}$")

print("------------------------------")

# Center Justify
print(f"Price 1 : {price1:^10}$")
print(f"Price 2 : {price2:^10}$")
print(f"Price 3 : {price3:^10}$")

print("------------------------------")

# Sign
# Plus sign
print(f"Price 1 : {price1:+}")
print(f"Price 2 : {price2:+}")
print(f"Price 3 : {price3:+}")

# Comma sign
print(f"Price 1 : {price1:,.2f}")
print(f"Price 2 : {price2:,.2f}")
print(f"Price 3 : {price3:,.2f}")
