try:
    word_count = {}

    with open('Sample.txt') as file:
        for line in file:
            words = line.split()
            for word in words:
                word = word.strip('.').lower()
                if word:  # checks if word is not empty string
                    # if word is in word_count increment counter by 1 if not append word to list
                    word_count[word] = word_count.get(word, 0) + 1

    for word, count in sorted(word_count.items()):
        print(f'{word}: {count}')


except FileNotFoundError:
    print("Error: File not found.")