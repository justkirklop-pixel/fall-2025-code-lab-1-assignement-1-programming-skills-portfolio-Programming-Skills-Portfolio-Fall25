word1 = "Coding"
word2 = "is"
word3 = "Cool"
print(word1 + " " + word2 + " " + word3)

num1 = 8
num2 = 10
sum_result = num1 + num2
print(sum_result)

bio = {
    "name": "Justin Lopez",
    "hometown": "Riyadh",
    "age": 21
}

print(bio["name"], bio["hometown"], bio["age"], sep="\n")

name = input("Enter your full name: ")
hometown = input("Enter your hometown: ")

try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Please enter a number for your age.")
    age = 0  
bio = {
    "name": name,
    "hometown": hometown,
    "age": age
}

print(bio["name"], bio["hometown"], bio["age"], sep="\n")

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

days_in_month = {
    1: 31, 
    2: 28,  
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

while True:
    month = int(input("Enter a month number (1-12), or 0 to exit: "))

    if month == 0:
        print("Program ended. Goodbye!")
        break

    if month in days_in_month:
        if month == 2:
            leap = input("Is it a leap year? (yes/no): ").lower()
            if leap == "yes":
                print("February has 29 days in a leap year.\n")
            else:
                print("February has 28 days.\n")
        else:
            print(f"Month {month} has {days_in_month[month]} days.\n")
    else:
        print("Invalid month number! Please enter a number between 1 and 12.\n")

correct_password = "12345"
max_attempts = 5
attempts = 0

while attempts < max_attempts:
    entered = input("Enter the password: ")
    attempts += 1

    if entered == correct_password:
        print("Password accepted. Welcome!")
        break
    else:
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"Incorrect password. You have {remaining} attempt(s) left.")
        else:
            print("Maximum attempts reached. Authorities have been alerted.")
           
import getpass

correct_password = 12345  
max_attempts = 5
attempts = 0

while attempts < max_attempts:
    raw = getpass.getpass("Enter the numeric password (input hidden): ")
    attempts += 1

    try:
        entered = int(raw)
    except ValueError:
        entered = None
        print("Invalid input. Please enter digits only.")
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"You have {remaining} attempt(s) left.\n")
        continue

    if entered == correct_password:
        print("Password accepted. Welcome!")
        break
    else:
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"Incorrect password. You have {remaining} attempt(s) left.\n")
        else:
            print("Maximum attempts reached. Authorities have been alerted.")

print("=== Gojira x Kong: Counting Challenge ===\n")

print("Gojira begins his rise from 0 to 50:")
for i in range(0, 51, 1):
    print(i)
print("Gojira has reached 50!\n")

print("Kong descends from Skull Island heights (50 down to 0):")
for i in range(50, -1, -1):
    print(i)
print("Kong has reached ground level!\n")

print("Shimo powers up from 30 to 50:")
for i in range(30, 51, 1):
    print(i)
print("Shimo’s icy energy is fully charged!\n")

print("Scar King strikes from 50 down to 10 in bursts of power:")
for i in range(50, 9, -2):
    print(i)
print("Scar King’s energy fades to 10!\n")

print("Titan alliance rises together from 100 to 200:")
for i in range(100, 201, 5):
    print(i)
print("The Titans have united at maximum strength — 200!\n")

print("=== End of Titan Counting Simulation ===")

names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

search_name = "Sam"

if search_name in names:
    print(f"{search_name} was found in the Titan registry!")
else:
    print(f"{search_name} was not found in the Titan registry.")

def hello():
    print("Hello titans of the earth") 

def main():
    hello()  

if __name__ == "__main__":
    main()

def check_even_odd(number):
    if number % 2 == 0:
        return f"{number} is even — Gojira approves!"
    else:
        return f"{number} is odd — Kong swings into action!"

def main():
    while True:
        try:
            num = int(input("Enter a number to test if it's even or odd (or type -1 to exit): "))
            
            if num == -1:
                print("Exiting the Titan even/odd checker. Farewell!")
                break
            
            result = check_even_odd(num)
            print(result)
            print()  

        except ValueError:
            print("Invalid input! Please enter an integer number.\n")

if __name__ == "__main__":
    main()