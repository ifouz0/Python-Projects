'''
Main Module: The secret letter game
'''
import datetime
import random
import string
import time

def main():
    '''
    Main Module Method
    '''
    print("*" * 150)
    print("*" * 150)
    print(f"{'S E C R E T    L E T T E R    G A M E':^150}")
    print("*" * 150)
    print("*" * 150)

    letters = string.ascii_uppercase
    MIN_LETTER = letters[0]
    MAX_LETTER = letters[-1]

    player_name = input("Hello! What's your name? ")
    print(f"Welcome, {player_name}! I am thinking of a letter between {MIN_LETTER} and {MAX_LETTER}. Can you guess it?")

    print("Preparing the game...")
    for seconds in range(5, 0, -1):
        print(f"The game will start in {seconds} seconds")
        time.sleep(1)
        
    num_games = 0
    num_attempts = 0
    player_record = 0

    start_time = datetime.datetime.now()

    exit_game = False
    while not exit_game:
        
        num_games += 1

        secret_letter = random.choice(letters)

        num_attempts = 0
        min_secret_letter  = MIN_LETTER
        max_secret_letter = MAX_LETTER
        player_letters = []

        secret_found = False
        while not secret_found:
            
            num_attempts += 1
            
            print("-" * 150)
            total_letters = letters.index(max_secret_letter) - letters.index(min_secret_letter) + 1
            player_letter = input(f"Game {num_games:02d} > Attempt {num_attempts} (P: {1/(total_letters):.2%} -> {total_letters} letters)\nPlease {player_name}, select a letter between {MIN_LETTER} - {MAX_LETTER}: ")
            player_letter = player_letter.upper()
            print("-" * 150)

            if (player_letter < MIN_LETTER or player_letter > MAX_LETTER):
                print(f"\u26A0  What are you doing, {player_name}!!! The letter {player_letter} is out of range (Range: {MIN_LETTER}-{MAX_LETTER})")
                num_attempts -= 1
                continue

            if (player_letter in player_letters):
                print(f"\u26A0  What are you doing, {player_name}!!! The letter {player_letter} is repeated (Values: {player_letters})")
                num_attempts -= 1
                continue

            if (player_letter < min_secret_letter):
                print(f"\u26A0  Are you stupid, {player_name}? The letter {player_letter} is not the secret letter. I said you that secret letter is greater than {letters[letters.index(min_secret_letter) - 1]}. \u261D")
                continue

            if (player_letter > max_secret_letter):
                print(f"\u26A0  Are you stupid, {player_name}? The letter {player_letter} is not the secret letter. I said you that secret letter is lower than {letters[letters.index(max_secret_letter) + 1]}. \U0001F447")
                continue
        
            player_letters.append(player_letter)
                
            if player_letter == secret_letter:
                secret_found = True
                print(f"\u2705 Congratulations, {player_name}! The secret letter was {secret_letter} and you guessed it in {num_attempts} attempts (Attempts: {player_letters})")
            elif player_letter < secret_letter:
                min_secret_letter = letters[letters.index(player_letter) + 1]
                print(f"\u274c Sorry, {player_name}! Your guess is too low: The letter {player_letter} is not the secret letter. \u261D")
            elif player_letter > secret_letter:
                max_secret_letter = letters[letters.index(player_letter) - 1]
                print(f"\u274c Sorry, {player_name}! Your guess is too high: The letter {player_letter} is not the secret letter. \U0001F447")

        
        if num_games == 1:
            player_record = num_attempts
        else:
            if num_attempts < player_record:
                print(f"\u2705 Congratulations, {player_name}! You have a new record of {num_attempts} attempts. The last record was {player_record} attempts")
                player_record = num_attempts
            elif num_attempts == player_record:
                print(f"\u2705 Uyyy, {player_name}! You were near to beat your record of {player_record} attempts")
            else:
                print(f"\u2705 Ufff, {player_name}! Your personal record is {player_record} attempts. You did worse this thime")
        

        player_key = input(f"Do you want to play more, {player_name}? (Y): ")
        exit_game = True if (player_key not in 'Yy') else False 



    end_time = datetime.datetime.now()
    duration = end_time - start_time

    print(f"Total time: {duration.total_seconds():.2f} seconds")
    print(f"Good job, {player_name}! Thanks for playing with us! You play {num_games} times and your record is {player_record} attempts")



if __name__ == "__main__":
    main()