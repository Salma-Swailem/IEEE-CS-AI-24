def probability_distribution(data):
    total_count = len(data)
    distribution = {}

    for key in data:
        if key in distribution:
            distribution[key] += 1
        else:
            distribution[key] = 1

    for key, value in distribution.items():
        distribution[key] = value / total_count

    return distribution


try:
        data = input("Enter a list of values separated by commas: ").split(",")
        data = [int(x) for x in data]
        print(probability_distribution(data))

except ValueError:
    print("Error: Please enter valid integers separated by spaces.")
except TypeError as e:
    print(f"\nError: {e}")
except KeyError as e:
    print(f"\nError: {e}")
except KeyboardInterrupt:
    print("\nProgram interrupted by user.")
except EOFError:
    print("\nEnd of file reached unexpectedly.")