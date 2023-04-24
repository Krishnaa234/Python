n = int(input("Enter the number of elements in the list: "))
lst = []
print("Enter any ", n, "element: ")
for i in range (0,n):
  e = input()
  lst.append(e)
print(lst)