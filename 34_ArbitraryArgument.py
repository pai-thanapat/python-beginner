# 34. Arbitrary Argument


# *Arg
def add(*nums):
    total = 0

    for num in nums:
        total += num

    return total


def display_name(*args):

    for arg in args:
        print(arg, end=" ")

    print()


value = add(1, 2, 3, 4, 5)
print(value)

display_name("Mr.", "John", "Middle", "Doe", "III")

print("---------------------------------")


# **Kwarg
def print_address(**kwargs):

    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_address(street="123 Main St", city="Anytown", state="CA", zip_code="12345")
print("---------------------------------")


# Exercise


def shipping_label(*arg, **kwargs):

    for arg in arg:
        print(arg, end=" ")

    print()

    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    else:
        print(f"{kwargs.get('street')}")

    print(f"{kwargs.get('city')}, {kwargs.get('state')} {kwargs.get('zip_code')}")


shipping_label(
    "Dr.",
    "John",
    "Doe",
    "the III",
    street="123 Main St",
    city="Anytown",
    state="CA",
    zip_code="12345",
)
