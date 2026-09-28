# 41. if __name__ = "__main__"

from module import ImportModule as import_module


def favorite_food(food):

    print(f"Your favorite food is {food}")


def main():

    print("Main script is running.")

    favorite_food("pizza")
    import_module.favorite_drink("soda")

    print("Goodbye.")


if __name__ == "__main__":
    main()
