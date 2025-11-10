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