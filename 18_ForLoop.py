# 18. For Loop

# Normal for loop
for x in range(1, 11):
    print(x)

print("------------------------------")

# Reverse for loop
for x in reversed(range(1, 11)):
    print(x)

print("------------------------------")

# For loop with step
for x in range(1, 11, 2):
    print(x)

print("------------------------------")

# For loop with string
credit_number = "1234-5678-9012-3456"

for x in credit_number:
    print(x)


print("------------------------------")

# For loop with continue/break
for x in range(1, 21):
    if x == 13:
        continue
    elif x == 17:
        break
    else:
        print(x)

print("------------------------------")
