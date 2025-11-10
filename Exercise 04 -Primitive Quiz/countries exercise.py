answer = input("What is the capital of France? ")
if answer.lower() == "paris":
    print("Correct!")
else:
    print("Incorrect. The correct answer is Paris.")

quiz = {
    "France": "Paris",
    "Germany": "Berlin",
    "Italy": "Rome",
    "Spain": "Madrid",
    "Portugal": "Lisbon",
    "Netherlands": "Amsterdam",
    "Belgium": "Brussels",
    "Sweden": "Stockholm",
    "Norway": "Oslo",
    "Greece": "Athens"
}

score = 0
for country, capital in quiz.items():
    answer = input(f"What is the capital of {country}? ")
    if answer.strip().lower() == capital.lower():  # Ignore spaces and capitalization
        print("Correct! 🎉\n")
        score += 1
    else:
        print(f"Wrong! ❌ The correct answer is {capital}.\n")

print(f"You got {score} out of {len(quiz)} correct!")