import random

def rps():
    print('Welcome to Rock, Paper, Scissors.')
    print('You will be playing against a computer.')
    print('There will be three rounds.')
    cw = 0
    pw = 0
    t = 0
    for rnum in range(3):
        res = ""
        choices = ["Rock", "Paper", "Scissors"]
        comp_choice = choices[random.randint(0, 2)]
        print("""(1) Rock
(2) Paper
(3) Scissors""")
        user_choice = input('Enter the number according to your choice: ')
        if user_choice.strip() == '1' or user_choice.strip() == '2' or user_choice.strip() == '3':
            if comp_choice == "Rock" and user_choice.strip() == "2":
                res = "Player Wins!"
            elif comp_choice == "Rock" and user_choice.strip() == "3":
                res = "Computer Wins!"
            elif comp_choice == "Paper" and user_choice.strip() == "1":
                res = "Computer Wins!"
            elif comp_choice == "Paper" and user_choice.strip() == "3":
                res = "Player Wins!"
            elif comp_choice == "Scissors" and user_choice.strip() == "1":
                res = "Player Wins!"
            elif comp_choice == "Scissors" and user_choice.strip() == "2":
                res = "Computer Wins!"
        else:
            print("Invalid choice. Exiting game now! Rerun the program to play again!")
            break
        if res == "Player Wins!":
            pw += 1
        elif res == "Computer Wins!":
            cw += 1
        else:
            t += 1
    if user_choice.strip() == '1' or user_choice.strip() == '2' or user_choice.strip() == '3':
        print("Losses:", cw)
        print("Wins:", pw)
        print("Ties:", t)
        if cw < pw:
            print('Nice! You beat the computer!')
        elif cw == pw:
            print('Ooh! A tie!')
        else:
            print('Better luck next time!')

rps()
