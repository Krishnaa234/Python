# WAP to play stone, paper, scissor 

def user_input():
    user_ch = input("Enter your choice (stone/paper/scissor)").lower()
    while user_ch not in ["stone", "paper", "scissor"]:
        print("Invalid choice. Choose again")
        user_ch = input("Enter your choice (stone/paper/scissor)").lower()
    return user_ch

def comp_input():
    return rd.choice(["stone", "paper", "scissor"])

def winner(user_ch, comp_ch):
    if user_ch == comp_ch:
        return "It's a tie"
    elif(user_ch == "stone" and comp_ch=="scissor") or (user_ch=="paper" and comp_ch=="stone") or (user_ch=="scissor" and comp_ch=="paper"):
        return "User won"
    else:
        return "You lost"

def main():
    print("Welcome to the game")
    while True:
        user_ch = user_input()
        comp_ch = comp_input()
        print("Your choice: ", user_ch)
        print("Computer choice: ", comp_ch)
        print(winner(user_ch, comp_ch))
        play_again = input("Do you want to play again? Yes or No: ").lower()
        if play_again == "no":
            print("Thank you for playing")
            break

if __name__ == "__main__":
    main()
