try:
    N = int(input("Enter the number of commands: "))
    if N < 1:
        raise ValueError("Number of commands must be a positive integer.")

    my_list = []

    # Command dictionary
    commands_functions = {
        "insert": lambda my_list, index, elem: my_list.insert(index, elem),
        "print": lambda my_list: print(my_list),
        "remove": lambda my_list, elem: my_list.remove(elem),
        "append": lambda my_list, elem: my_list.append(elem),
        "sort": lambda my_list: my_list.sort(),
        "pop": lambda my_list: my_list.pop(),
        "reverse": lambda my_list: my_list.reverse()
    }

    # Take user command input and arbitrary arguments
    for i in range(N):
        command, *args = input().split()
        if command in commands_functions:
            commands_functions[command](my_list, *(map(int, args)))
        else:
            raise KeyError("Invalid command.")


except ValueError as e:
    print(f"\nError: {e}")
except IndexError:
    print("\nInvalid number of arguments for the command.")
except TypeError as e:
    print(f"\nError: {e}")
except KeyError as e:
    print(f"\nError: {e}")
except KeyboardInterrupt:  # to handle user interruption
    print("\nProgram interrupted by user.")