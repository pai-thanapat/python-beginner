# 20. Nested Loop

for x in range(3):

    for y in range(1, 10):

        print(y, end="")

    print()


# Example

rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
symbol = input("Enter a symbol to use: ")

for i in range(rows):
    for j in range(columns):

        print(symbol, end="")

    print()
