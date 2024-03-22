try:
    prior_a = float(input("Enter the prior probability of event A: "))
    prior_b = float(input("Enter the prior probability of event B: "))
    conditional_b_given_a = float(input("Enter the conditional probability of B given A: "))

    if not (0 <= prior_a <= 1) or not (0 <= prior_b <= 1) or not (0 <= conditional_b_given_a <= 1):
        raise ValueError("Probabilities must be between 0 and 1.")

    bayes_theorem = (conditional_b_given_a * prior_a) / prior_b

    print(bayes_theorem)

except ValueError as e:
    if "0" in str(e):
        print(f"Error: {e}")
    else:
        print("Error: Please enter a valid number")
except TypeError:
    print("Error: Please enter a valid number")
except KeyError as e:
    print(f"\nError: {e}")
except KeyboardInterrupt:
    print("\nProgram interrupted by user.")
except EOFError:
    print("\nEnd of file reached unexpectedly.")
