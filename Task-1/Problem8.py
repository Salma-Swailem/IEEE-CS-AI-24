n = int(input())

f = []
for i in range(1, n):
    if n % i == 0:
        f.append(i)

if sum(f) == n:
    print(f"{n} is a perfect number")
else:
    print(f"{n} is not a perfect number")
