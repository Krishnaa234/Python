'''Program to input day number from 1 to 7 and print the respective day'''

x=int(input("Enter number from 1 to 7: "))
if x==1:
    print("Monday.")
elif x==2:
    print("Tuesday.")
elif x==3:
    print("Wednesday.")
elif x==4:
    print("Thursday.")
elif x==5:
    print("Friday.")
elif x==6:
    print("Saturday.")
elif x==7:
    print("Sunday.")
else:
    print("Entered a wrong input.")