n = int(input("Enter the number: "))
for i in range(1, n+1, 2):
    print(i * '*')
for i in range(n-2, 0, -2):
    print(i * '*')