import random

try:
    random_number = random.randint(1, 100)
    guess = None
    attempts = 0
    while guess != random_number:
        guess = int(input("Enter your guess:"))
        attempts += 1

        if guess < 1 or guess > 100:
            raise ValueError("Guess must be between 1 and 100")

        if guess > random_number:
            print("Too high")
        elif guess < random_number:
            print("Too low")
        else:
            print()
            print("\033[92m" + "************************************************************")
            print("\033[92m" + f"Congratulations! You've guessed the number {random_number} in {attempts} attempts!")
            print("\033[92m" + "************************************************************")


except ValueError as e:
    if "Guess must be between 1 and 100" in str(e):
        print(e)
    else:
        print("Invalid input! Please enter a valid integer.")
except KeyboardInterrupt:
    print("\nGame aborted. Thanks for playing!")
