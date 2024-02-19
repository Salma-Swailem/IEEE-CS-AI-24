try:
    n = float(input("Enter number: "))
except ValueError:
    print("\nInvalid input: Please enter a valid number")
except KeyboardInterrupt:
    print("\nProgram interrupted by user.")