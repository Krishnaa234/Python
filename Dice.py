# WAP to print a dice semulator

def dice():
    return rd.randint(1,6) # gives random values from 1 to 6

def main():
    print("Welcome to dice game")
    while True:
        input("Please hit enter button to roll the dice")
        result = dice()
        print("You got a number ",result)
        print(" ")
        play_again = input("Do you want to continue? Press yes or no: ")
        print(" ")
        if play_again.lower()=="no":
            print("Thanks for playing")
            break
if __name__=="__main__":
    main()
