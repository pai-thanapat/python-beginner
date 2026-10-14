# 58. Exception Handling

try:
    number = int(input("Enter a number: "))

    print(f"1/{number} = {1/number}")
except ZeroDivisionError:
    print("Please enter a number other than zero.")
except ValueError:
    print("Please enter a valid integer.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("Execution completed.")
