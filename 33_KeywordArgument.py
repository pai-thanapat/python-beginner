# 33. Keyword Argument


def hello(greeting, title, first_name, last_name):
    print(f"{greeting} {title}{first_name} {last_name}")


hello("Hello", title="Mr.", last_name="Doe", first_name="John")


# Exercise


def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"


phone_number = get_phone(country="1", area="123", first="456", last="7890")
print(f"Phone number: {phone_number}")
