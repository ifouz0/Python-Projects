import random
import os

def main():
    os.system("cls")

    print("*" * 150)
    print("*" * 150)
    title = "R O C K ,  P A P E R   A N D   S C I S S O R S  ( \u270A \u270B \u270C ) V.10"
    print(f"{title:^150}")
    print("*" * 150)
    print("*" * 150)


    MAX_ROUNDS = 5
    player_name = None
    total_games = 0
    total_wins = 0
    total_losses = 0
    round_num = 0
    round_wins = 0
    round_drafts = 0
    round_losses = 0
    computer_move = None
    player_move = None

    player_name = input("Hello! What's your name? ")
    print(f"Welcome, {player_name}! We will play the famous game rock, paper and scissors.")
    print(f"The winner will be the best of {MAX_ROUNDS} rounds. Are you ready?")

    while True:

        total_games += 1
        round_num = 0
        round_wins = 0
        round_drafts = 0
        round_losses = 0

        print("-" * 150)
        print(f"- Let's start!!! Game number: {total_games} (Best of {MAX_ROUNDS} rounds)")
        print("-" * 150)

        while round_wins < MAX_ROUNDS and round_losses < MAX_ROUNDS:
            
            round_num += 1

            print("1, 2, 3!!! Rock, paper and scissors...")
            computer_move = random.choice("RPS")

            while True:
                player_move = input("Please, select a value ( R: \u270A | P: \u270B | S: \u270C ): ")
                if player_move not in "RPS":
                    print(f"\U0001F6A9 ERROR: Repeat, {player_name}!! Please select a correct value  ( R: \u270A | P: \u270B | S: \u270C )...")
                    continue
                break
            
            if player_move == computer_move:
                print(f"\U0001F7E1 Repeat, {player_name}!! We select the same...")
                round_drafts += 1
            elif computer_move == "R" and player_move == "P":
                print(f"\u2705 Congratulations, {player_name}. You win this round! Paper \u270B (you)  beats rock \u270A (computer).")
                round_wins += 1
            elif computer_move == "R" and player_move == "S":
                print(f"\u274c Sorry, {player_name}. You lost this round! Rock \u270A (computer) beats scissor \u270C (you).")
                round_losses += 1
            elif computer_move == "P" and player_move == "R":
                print(f"\u274c Sorry, {player_name}. You lost this round! Paper \u270B (computer) beats rock \u270A (you).")
                round_losses += 1
            elif computer_move == "P" and player_move == "S":
                print(f"\u2705 Congratulations, {player_name}. You win this round! Scissor \u270C (you)  beats paper \u270B (computer).")
                round_wins += 1
            elif computer_move == "S" and player_move == "R":
                print(f"\u2705 Congratulations, {player_name}. You win this round! Rock \u270A (you) beats scissor \u270C (computer).")
                round_wins += 1
            elif computer_move == "S" and player_move == "P":
                print(f"\u274c Sorry, {player_name}. You lost this round! Scissor \u270C (computer) beats paper \u270B (you)")
                round_losses += 1
            
            print("-" * 150)
            print(f"- Game number:    {total_games} (Best of {MAX_ROUNDS} rounds)")
            print("-" * 150)
            print(f"- Round number:          {round_num}")
            print(f"- Round player wins:     {round_wins} ({round_wins/round_num:.2%}) -> Win: {round_wins}/{MAX_ROUNDS} ({round_wins/MAX_ROUNDS:.2%})")
            print(f"- Round computer wins:   {round_losses} ({round_losses/round_num:.2%}) -> Win: {round_losses}/{MAX_ROUNDS} ({round_losses/MAX_ROUNDS:.2%})")
            print(f"- Round drafts:          {round_drafts} ({round_drafts/round_num:.2%})")
            print("-" * 150)
            print(f"- Total player wins:     {total_wins}")
            print(f"- Total computer wins:   {total_losses}")
            print("-" * 150)
            

        if round_wins > round_losses:
            total_wins += 1
            print(f"\u2705 Congratulations, {player_name}. You win this game!!")
        else:
            total_losses += 1   
            print(f"\u274c Sorry, {player_name}. You lost this game!!!")
        

        print("-" * 150)
        print(f"- Total games:      {total_games}")
        print("-" * 150)
        print(f"- Player wins:      {total_wins} ({total_wins/total_games:.2%})")
        print(f"- Computer wins:   {total_losses} ({total_losses/total_games:.2%})")
        print("-" * 150)
        
        finish = input(f"Do you want to play another time, {player_name}? (Y/N): ")
        if (finish.upper() != "Y"): 
            break

        os.system("cls")

    print(f"Bye bye!! Thanks to play with us...")



if __name__ == "__main__":
    main()