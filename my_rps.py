# my rock paper scessior game
import random
import sys


def play_game():
    game_count = 0
    player_wins = 0
    computer_wins = 0
    draw = 0
    play_again = True

    def rps():

        choice_list = ["rock", "paper", "scissors"]
        computer_choice = random.choice(choice_list)
        user_choice = input("Hi, Please Enter....\n rock or paper or scissors🤗🤗\n\n")

        def chose_winner(computer_choice, user_choice):
            nonlocal computer_wins
            nonlocal player_wins
            nonlocal draw
            if user_choice == "rock" and computer_choice == "scissors":
                player_wins += 1
                return "You are the winner 🎉🎊"
            elif user_choice == "rock" and computer_choice == "paper":
                computer_wins += 1
                return "Python is the winner 🐍"
            elif user_choice == "rock" and computer_choice == "rock":
                draw += 1
                return "Draw"
            elif user_choice == "scissors" and computer_choice == "scissors":
                draw += 1
                return "Draw"
            elif user_choice == "scissors" and computer_choice == "paper":
                player_wins += 1
                return "You are the winner 🎉🎊"
            elif user_choice == "scissors" and computer_choice == "rock":
                computer_wins += 1
                return "Python is the winner 🐍"
            elif user_choice == "paper" and computer_choice == "paper":
                draw += 1
                return "Draw"
            elif user_choice == "paper" and computer_choice == "rock":
                player_wins += 1
                return "You are the winner 🎉🎊"
            elif user_choice == "paper" and computer_choice == "scissors":
                computer_wins += 1
                return "Python is the winner 🐍"

        game_result = chose_winner(computer_choice, user_choice)
        print("the resul is : " + game_result + "\n")

        print("computer choice is " + str(computer_choice) + "\n")
        print("Computer wins are : " + str(computer_wins) + "\n")
        print("Player wins are : " + str(player_wins) + "\n")
        print("Draws are : " + str(draw) + "\n")
        nonlocal game_count
        game_count += 1
        print("game count is " + str(game_count))
        while True:
            playagain = input("\nY for Yes or \nQ to Quit\n")
            if playagain.lower() not in ["y", "q"]:
                continue
            else:
                break

        if playagain.lower() == "y":
            return rps()
        else:
            print("\n🎉🎉🎉🎉")
            print("Thank you for playing!\n")
            sys.exit("Bye! 👋")

    return rps()


play_game()
