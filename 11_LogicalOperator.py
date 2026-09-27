# 11. Logical Operators

temperature = 25
is_raining = False
is_sunny = True

if temperature > 30 or temperature < 0 or is_raining:
    print("The weather is not suitable for outdoor activities.")
else:
    print("The weather is suitable for outdoor activities.")

if temperature >= 28 and is_sunny:
    print("It's a great day for a picnic!")
elif temperature <= 0 and is_sunny:
    print("It's a sunny winter day!")
elif temperature <= 0 and not is_sunny:
    print("It's a cold and cloudy day.")
else:
    print("The weather is moderate.")
