try:
    n = int(input())
    if n <= 0:
        raise ValueError("Number of participants must be a positive integer.")

    # Check for non-numeric values in the list
    try:
        A = list(map(int, input().split()))
    except ValueError:
        raise ValueError("Non-numeric value found in the list of scores.")

    # check if list is mt
    if not A:
        raise ValueError("List of scores is empty.")

    if len(A) < n:
        raise EOFError()

    # cast as set to exclude duplicates
    A = set(A)
    A = sorted(A, reverse=True)

    print(A[1])


except ValueError as e:
    print("\nError:", e)
except TypeError as e:
    print("\nError:", e)
except EOFError:
    print("\nError: Unexpected end of input.")
except KeyboardInterrupt:
    print("\nProgram interrupted by user.")