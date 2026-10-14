# 57. Decorator


def add_sprinkel(func):
    def wrapper(*args, **kwargs):
        print("Adding sprinkel to the ice cream! 🍨")

        func(*args, **kwargs)

    return wrapper


def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("Adding fudge to the ice cream! 🍫")

        func(*args, **kwargs)

    return wrapper


@add_sprinkel
@add_fudge
def get_ice_cream(flavor):
    print(f"Here's your {flavor} ice cream! 🍦")


get_ice_cream("vanilla")
