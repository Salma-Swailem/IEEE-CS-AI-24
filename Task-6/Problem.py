try:
    def get_numbers():
        try:
            count = input("Enter a list of number frequencies separated by comma: ").split(',')
            count = [int(num) for num in count]
            return count
        except ValueError:
            print("Error: Please enter a valid list of numbers.")
            return get_numbers()


    def sampleStats(count):

        minimum = float('inf')
        maximum = float('-inf')
        sum_values = 0
        sum_frequencies = 0
        mode_count = 0
        mode = None
        total_count = sum(count)
        med0 = med1 = -1

        for number, frequency in enumerate(count):
            if frequency > 0:
                minimum = min(minimum, number)
                maximum = max(maximum, number)

                if frequency > mode_count:
                    mode_count = frequency
                    mode = number

                sum_values += (number * frequency)
                sum_frequencies += frequency

                if sum_frequencies >= (total_count + 1) // 2 and med0 < 0:
                    med0 = number
                if sum_frequencies >= (total_count + 2) // 2 and med1 < 0:
                    med1 = number

        mean = float(sum_values) / sum_frequencies

        return [minimum, maximum, round(mean, 5), float(med0 + med1) / 2, mode]



    data_array = get_numbers()
    print(data_array)
    print(sampleStats(data_array))

except TypeError as e:
    print(f"\nError: {e}")
except ValueError as e:
    print(f"\nError: {e}")
except KeyError as e:
    print(f"\nError: {e}")
except KeyboardInterrupt:
    print("\nProgram interrupted by user.")
except EOFError:
    print("\nEnd of file reached unexpectedly.")