try:
    N = int(input("Enter the number of commands: "))
    if N < 1:
        raise ValueError("Number of commands must be a positive integer.")

    my_list = []

    # Command dictionary
    commands_functions = {
        "insert": lambda command, index, elem: command.insert(index, elem),
        "print": lambda command: print(command),
        "remove": lambda command, elem: command.remove(elem),
        "append": lambda command, elem: command.append(elem),
        "sort": lambda command: command.sort(),
        "pop": lambda command: command.pop(),
        "reverse": lambda command: command.reverse()
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