def find_common(set_1, set_2):
    """
    Find the common elements between two sets

    Args:
        set_1 (set): first set
        set_2 (set): second set

    Returns:
        set: A new set containing the common elements in set_1 and set_2
    """
    return set_1.intersection(set_2)


try:
    set_1 = set(map(str.strip, input().split()))
    set_2 = set(map(str.strip, input().split()))
    if not set_1 or not set_2:
        raise ValueError("Both sets must contain elements.")
    print(find_common(set_1, set_2))

except ValueError as e:
    print("\nError:", e)
except KeyboardInterrupt:
    print("\nProgram interrupted by user.")
