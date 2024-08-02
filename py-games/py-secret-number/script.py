'''
Main Module: The secret number game
'''
import random
import datetime
import time

def main():
    '''
    Main Module Method
    '''
    print("*" * 150)
    print("*" * 150)
    print(f"{'S E C R E T    N U M B E R    G A M E':^150}")
    print("*" * 150)
    print("*" * 150)

    MIN_NUMBER = 1
    MAX_NUMBER = 100

    player_name = input("Hello! What's your name? ")
    print(f"Welcome, {player_name}! I am thinking of a number between {MIN_NUMBER} and {MAX_NUMBER}. Can you guess it?")

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

        secret_number = random.randint(1,100)

        num_attempts = 0
        min_secret_number  = MIN_NUMBER
        max_secret_number = MAX_NUMBER
        player_numbers = []

        secret_found = False
        while not secret_found:
            
            num_attempts += 1
            
            print("-" * 150)
            total_numbers = max_secret_number - min_secret_number + 1
            player_number = int(input(f"Game {num_games:02d} > Attempt {num_attempts} (P: {1/(total_numbers):.2%} -> {total_numbers} numbers)\nPlease {player_name}, select a number between {MIN_NUMBER} - {MAX_NUMBER}: "))
            print("-" * 150)

            if (player_number < MIN_NUMBER or player_number > MAX_NUMBER):
                print(f"\u26A0  What are you doing, {player_name}!!! The number {player_number} is out of range (Range: {MIN_NUMBER}-{MAX_NUMBER})")
                num_attempts -= 1
                continue

            if (player_number in player_numbers):
                print(f"\u26A0  What are you doing, {player_name}!!! The number {player_number} is repeated (Values: {player_numbers})")
                num_attempts -= 1
                continue

            if (player_number < min_secret_number):
                print(f"\u26A0  Are you stupid, {player_name}? The number {player_number} is not the secret number. I said you that secret number is greater than {min_secret_number - 1}. \u261D")
                continue

            if (player_number > max_secret_number):
                print(f"\u26A0  Are you stupid, {player_name}? The number {player_number} is not the secret number. I said you that secret number is lower than {max_secret_number + 1}. \U0001F447")
                continue
        
            player_numbers.append(player_number)
                
            if player_number == secret_number:
                secret_found = True
                print(f"\u2705 Congratulations, {player_name}! The secret number was {secret_number} and you guessed it in {num_attempts} attempts (Attempts: {player_numbers})")
            elif player_number < secret_number:
                min_secret_number = player_number + 1
                print(f"\u274c Sorry, {player_name}! Your guess is too low: The number {player_number} is not the secret number. \u261D")
            elif player_number > secret_number:
                max_secret_number = player_number - 1
                print(f"\u274c Sorry, {player_name}! Your guess is too high: The number {player_number} is not the secret number. \U0001F447")

        
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