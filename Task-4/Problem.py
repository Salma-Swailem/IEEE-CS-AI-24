try:
    def get_numbers():
        try:
            numbers = input("Enter a list of numbers separated by comma: ").split(',')
            numbers = [float(num) for num in numbers]
            return numbers
        except ValueError:
            print("Error: Please enter a valid list of numbers.")
            return get_numbers()


    def find_min(numbers):
        if not numbers:
            raise ValueError("List is empty")
        min_num = numbers[0]
        for num in numbers:
            if num < min_num:
                min_num = num
        return min_num


    def find_max(numbers):
        if not numbers:
            raise ValueError("List is empty")
        max_num = numbers[0]
        for num in numbers:
            if num > max_num:
                max_num = num
        return max_num


    def find_mean(numbers):
        if not numbers:
            raise ValueError("List is empty")
        return sum(numbers) / len(numbers)


    def find_mode(numbers):
        if not numbers:
            raise ValueError("List is empty")
        freq = {}
        for num in numbers:
            freq[num] = freq.get(num, 0) + 1
        modes = [key for key, value in freq.items() if value == max(freq.values())]
        return modes[0]


    def find_median(numbers):
        if not numbers:
            raise ValueError("List is empty")
        sorted_nums = sorted(numbers)
        n = len(sorted_nums)
        if n % 2 == 0:
            return (sorted_nums[n // 2 - 1] + sorted_nums[n // 2]) / 2
        else:
            return sorted_nums[n // 2]


    def find_range(numbers):
        if not numbers:
            raise ValueError("List is empty")
        return find_max(numbers) - find_min(numbers)


    def find_variance(numbers):
        if not numbers:
            raise ValueError("List is empty")
        mean = find_mean(numbers)
        variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
        return variance


    def find_STD(numbers):
        if not numbers:
            raise ValueError("List is empty")
        return find_variance(numbers) ** 0.5


    def find_Quartiles(numbers):
        if not numbers:
            raise ValueError("List is empty")
        sorted_nums = sorted(numbers)
        n = len(sorted_nums)
        Q1 = int(find_median(sorted_nums[:n // 2]))
        Q2 = int(find_median(sorted_nums))
        Q3 = int(find_median(sorted_nums[n // 2 + n % 2:]))
        return Q1, Q2, Q3


    def find_IQR(numbers):
        Q1, Q2, Q3 = find_Quartiles(numbers)
        return Q3 - Q1


    numbers = get_numbers()
    print("Min:", int(find_min(numbers)))
    print("Max:", int(find_max(numbers)))
    print("Mean:", find_mean(numbers))
    print(f"Mode: [{int(find_mode(numbers))}]")
    print("Median:", find_median(numbers))
    print("Range:", int(find_range(numbers)))
    print(f"Variance:{find_variance(numbers):.2f}")
    print(f"Standard Deviation: {find_STD(numbers):.5f}")
    Q1, Q2, Q3 = find_Quartiles(numbers)
    print(f"Quartiles: {Q1, Q2, Q3}")
    print("Interquartile Range (IQR):", int(find_IQR(numbers)))

except TypeError as e:
    print(f"\nError: {e}")
except ValueError as e:
    print(f"\nError: {e}")
except KeyError as e:
    print(f"\nError: {e}")
except KeyboardInterrupt:
    print("\nProgram interrupted by user.")