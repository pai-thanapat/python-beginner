# 24. Quiz Game

questions = (
    "How many elements are in the periodic table?",
    "Which animal lays the largest eggs?",
    "What is the most abundant gas in the Earth's atmosphere?",
    "How many bones are in the human body?",
    "Which planet in the solar system is the hottest?",
)

options = (
    ("A) 118", "B) 119", "C) 120", "D) 121"),
    ("A) Whale", "B) Crocodile", "C) Elephant", "D) Ostrich"),
    ("A) Nitrogen", "B) Oxygen", "C) Carbon Dioxide", "D) Argon"),
    ("A) 206", "B) 207", "C) 208", "D) 209"),
    ("A) Mercury", "B) Venus", "C) Earth", "D) Mars"),
)

answers = ("A", "D", "A", "A", "B")
guess = []
score = 0
question_num = 0

for question in questions:

    print("--------------------------")
    print(question)

    for option in options[question_num]:

        print(option)

    user_guess = input("Enter (A, B, C, D): ").upper()
    guess.append(user_guess)

    if user_guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("WRONG!")
        print(f"{answers[question_num]} is the correct answer.")

    question_num += 1

print("--------------------------")
print("       Quiz Results       ")
print("--------------------------")
print(f"Answers: {answers}")
print(f"Guesses: {guess}")
print(f"Score: {score}/{len(questions)}")
