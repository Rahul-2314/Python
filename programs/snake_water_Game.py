# Snake Water Gun
# Snake, Water and Gun is a variation of the children's game "rock-paper-scissors" where players use hand gestures to represent a snake, water, or a gun. The gun beats the snake, the water beats the gun, and the snake beats the water. Write a python program to create a Snake Water Gun game in Python using if-else statements. Do not create any fancy GUI. Use proper functions to check for win.

import random


def decorate(fx):
    def mfx(*args, **kwargs):
        print("")
        print("="*97)
        fx(*args, **kwargs)
    return mfx


def computer():
    return random.choices(["Snake", "Water", "Gun"])


@decorate
def snake_water_gun():
    print("*"*30, "Welcome to the Snake Water Gun Game", "*"*30)
    print("\n===>>  Choose your options carefully---( 1 for Snake , 2 for Water , 3 for Gun )\n")
    # print("\n1 for Snake , 2 for Water , 3 for Gun\n")

    your_score=0
    computer_score=0

    user_input = int(input("Enter Your Choice (1/2/3) :"))
    if user_input==1:
        print("\nYou : Snake")
    elif user_input==2:
        print("\nYou : Water")
    elif user_input==3:
        print("\nYou : Gun")
    else:
        print("Choose Your Options Carefully")

    bot = computer()
    print("Computer :",bot)

    if bot == ["Snake"]:
        if user_input == 1:
            print("\nRESULT : Match Draw")
        elif user_input == 3:
            print("\nRESULT : You Win")
            your_score+=1
        elif user_input == 2:
            print("\nRESULT : You Lose")
            computer_score+=1
        else:
            print("\nChoose Carefully")

    if bot == ["Water"]:
        if user_input == 2:
            print("\nRESULT : Match Draw")
        elif user_input == 1:
            print("\nRESULT : You Win")
            your_score+=1
        elif user_input == 3:
            print("\nRESULT : You Lose")
            computer_score+=1
        else:
            print("\nChoose Carefully")

    if bot == ["Gun"]:
        if user_input == 3:
            print("\nRESULT : Match Draw")
        elif user_input == 2:
            print("\nRESULT : You Win")
            your_score+=1
        elif user_input == 1:
            print("\nRESULT : You Lose")
            computer_score+=1
        else:
            print("\nChoose Carefully")

    print("\nYour Score :",your_score)
    print("Computer Score :",computer_score)
    print("")

while True:
    snake_water_gun()

    play_again=input("Do you want to play again?(Press Enter to continue)  :")
    if play_again !="":
        break

