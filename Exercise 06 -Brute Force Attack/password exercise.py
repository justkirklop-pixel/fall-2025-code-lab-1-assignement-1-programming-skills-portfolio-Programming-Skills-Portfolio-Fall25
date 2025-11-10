correct_password = "12345"

entered = input("Enter the password: ")
while entered != correct_password:
    print("Incorrect password. Try again.")
    entered = input("Enter the password: ")

print("Password accepted. Welcome!")

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
