n = int(input())

factors = []
x = 2
while n > 1:
    while n % x == 0:
        factors.append(x)
        n /= x

    x += 1

print(f"Prime Factors: {', '.join(map(str, set(factors)))}")
