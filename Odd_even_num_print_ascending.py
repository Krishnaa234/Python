n = int(input("Enter the number: "))
print("Odd number in ascending order till",n,": ")
for i in range(1, n+1, 2):
    print(i, end='\t' )
print(end='\n')
print("Enen number in ascending order till",n,": ")
for i in range(0, n+1, 2):
    print(i , end='\t' )