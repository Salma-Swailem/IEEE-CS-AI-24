x = str(input())

if x == x[::-1]:
    print(f'The word {x} is a palindrome')
else:
    print(f'The word {x} is not a palindrome')
