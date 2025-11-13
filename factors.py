x = int(input("Enter the number: "))
y = []
print("The factors of", x, "are:")
for i in range(1, x + 1):  # Include x itself if needed
    if x % i == 0:
        y.append(i)
print(y)
print("Number of factors:", len(y))

n = int(input("Enter how many factors you want to see: "))
if n > len(y):
    print("Invalid input: number exceeds total factors.")
else:
    print("First", n, "factors:")
    for k in range(n):
        print(y[k], end=" ")
