def conditional_probability(event_a, event_b):
    total_count_a = sum(event_a)
    count_a_given_b = 0
    for i in range(min(len(event_a), len(event_b))):
        if event_a[i] == 1 and event_b[i] == 1:
            count_a_given_b += 1

    if total_count_a == 0:
        return 0

    return count_a_given_b / total_count_a


try:
    event_a = input("Enter events for A separated by commas (0 not occurring, 1 occurring): ").split(",")
    event_b = input("Enter events for B separated by commas (0 not occurring, 1 occurring): ").split(",")
    event_a = [int(x) for x in event_a]
    event_b = [int(x) for x in event_b]

    if not all(x in [0, 1] for x in event_a) or not all(x in [0, 1] for x in event_b):
        raise ValueError("Error: Inputs must be either 0 or 1.")

    print(conditional_probability(event_a, event_b))

except ValueError as e:
    if "either" in str(e):
        print(f"Error: {e}")
    else:
        print("Error: Please enter valid integers (0 or 1) separated by commas.")
except TypeError as e:
    print(f"\nError: {e}")
except KeyError as e:
    print(f"\nError: {e}")
except KeyboardInterrupt:
    print("\nProgram interrupted by user.")
except EOFError:
    print("\nEnd of file reached unexpectedly.")