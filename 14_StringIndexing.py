# 14. String Indexing

credit_number = "1234-5678-9012-3456"

first_digit = credit_number[0]

print(f"First digit of credit number : {first_digit}")

first_four_digits = credit_number[0:4]

print(f"First four digits of credit number : {first_four_digits}")

second_four_digits = credit_number[5:9]

print(f"Second four digits of credit number : {second_four_digits}")

five_to_last_digits = credit_number[5:]

print(f"Five to last digits of credit number : {five_to_last_digits}")

last_digit = credit_number[-1]

print(f"Last digit of credit number : {last_digit}")

every_second_digit = credit_number[::2]

print(f"Every second digit of credit number : {every_second_digit}")

last_four_digits = credit_number[-4:]

print(f"Last four digits of credit number : {last_four_digits}")

reverse_credit_number = credit_number[::-1]

print(f"Reverse credit number : {reverse_credit_number}")
