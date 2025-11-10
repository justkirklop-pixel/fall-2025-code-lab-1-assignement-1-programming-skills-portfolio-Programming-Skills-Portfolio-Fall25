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
    age = 0  # Default value if user enters something invalid

bio = {
    "name": name,
    "hometown": hometown,
    "age": age
}

# Step 3: Print all information on separate lines
print(bio["name"], bio["hometown"], bio["age"], sep="\n")
