# 32. Default Argument

import time


def net_price(list_price, discount=0, tax=0.05):
    return list_price * (1 - discount) * (1 + tax)


def count(end, start=0):
    for x in range(start, end + 1):

        print(x)

        time.sleep(1)

    print("DONE!")


product1 = net_price(100, 0.1, 0.05)
print(f"Product 1: ${product1:.2f}")

product2 = net_price(100)
print(f"Product 2: ${product2:.2f}")

count(5, 3)
