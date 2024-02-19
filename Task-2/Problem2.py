try:
    N = int(input('Enter number of students: '))
    if N < 2 or N > 5:
        raise ValueError("Invalid number. number of students range is 2 to 5.")

    records = []  # store all records
    second_lowest_students = []  # stores students with 2nd to lowest score

    for i in range(N):  # iterator to take user records input
        student = input("Enter student: ")
        if not student.isalpha():
            raise ValueError("Invalid student name. Please enter alphabetic characters only.")

        try:
            score = float(input("Enter score: "))
        except ValueError:
            raise ValueError("Invalid score value.")

        records.append([student, score])

    if not records:
        raise ValueError("No records were entered.")

    records.sort(key=lambda record: record[1])

    lowest_score = records[0][1]
    second_lowest_score = None

    # find second to lowest score
    for _, score in records:
        if score > lowest_score:
            second_lowest_score = score
            break

    for student, score in records:
        if score == second_lowest_score:
            second_lowest_students.append(student)

    second_lowest_students.sort()
    for student in second_lowest_students:
        print(student)

except ValueError as e:
    print(e)
except TypeError as e:
    print("\nInvalid Value Type", e)
except EOFError:
    print("\nError: Unexpected end of input.")
except KeyboardInterrupt:
    print("\nProgram interrupted by user.")
