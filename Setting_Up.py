"""
This file is named Setting_UP.py sets up the game of roulette with the Wheel Class
and Results Class
"""
import os
import time
import random

#Creating class to log to an output file, this will be inheritted 
class CasinoLogger:
    def __init__(self, log_path):
        self.log_path = log_path

    #Logging perfomace to output log
    def log_performance(self, player_name, total):
        try:
            with open(self.log_path, 'a') as log_file:
                log_file.write(f"{player_name}: ${total:.2f}\n")
        except Exception as e:
            print(f"Error logging performance: {e}")


#Creating Class of the wheel
class Wheel:
    def __init__(self):
        #Creating list 1 through 36
        self.nums = list(range(1, 37))

        #Assinging Red to even and black to odd
        self.colors = ['Red' if x % 2 == 0 else 'Black' for x in self.nums]

        #Creating tuple of all numbers and colors on wheel
        self.wheel = list(zip(self.nums, self.colors))

    #Spinning the Wheel
    def spin_wheel(self):
        #Getting random choice
        result = random.choice(self.wheel)

        return result

    #Removing previous spin from wheel
    def remove_from_wheel(self, result):
        #Removing the result
        self.wheel.remove(result)

        return result

    #Outputting the spin result
    def formatting_output(self, result):
        time.sleep(2)
        print(f'\nYour Spin Resulted in {result[1]}, {result[0]}')

    #Displaying the numbers left as strings
    def display_remaining_spots(self):
        #Getting the numbers left after last spin is removed
        remaining_numbers = [str(num) for num, color in self.wheel]
        time.sleep(1)

        print("Remaining numbers on the wheel:", ', '.join(remaining_numbers))


#Inheritting CasinoLogger
class Results(CasinoLogger):
    def __init__(self, wheel, log_path="lysek_casino_performance_log.txt"):
        super().__init__(log_path)
        self.wheel = wheel
        self.total = 0

    #Displaying the leader board at the end of the game
    def display_leaderboard(self):
        try:
            #Opening the file
            with open(self.log_path, 'r') as log_file:
                leaders = []

                #Going through each line in the file
                for line in log_file:
                    parts = line.strip().split(": ")
                    if len(parts) < 2:
                        continue
                    identifier, amount_str = parts[0], parts[1].replace('$', '').split(" - ")[0]
                    try:
                        amount = float(amount_str)
                        leaders.append((identifier, amount))
                    except ValueError:
                        continue

                #Sorting the leaderboard top to bottom
                leaders.sort(key=lambda x: x[1], reverse=True)

            #Printing the leader board
            print("\nAll-Time Leaderboard:")
            for rank, (identifier, amount) in enumerate(leaders, start=1):
                print(f"{rank}. {identifier} - ${amount:.2f}")

        #Checking for errors
        except FileNotFoundError:
            print("\nLeaderboard is currently empty.")
        except Exception as e:
            print(f"Error processing leaderboard: {e}")

    #Removing the previous spin from the wheel
    def update_wheel_and_feedback(self, result):
        self.wheel.remove_from_wheel(result)
        self.wheel.display_remaining_spots()

    #Checking to see if winner
    def check_winner(self, bet, spin, name):
        win = self.resolve_bet(bet, spin)
        if win:
            self.total += bet[1] * 1.5
            print(f"\nCongratulations, you won this round! Your total is now ${self.total:.2f}")
            if self.total >= 0:
                print(
                    f'\nYour potential payout next round is ${(self.total * 1.5):.2f}, or you could walk away with your current winnings.')
    #If Player lost
        else:
            if self.total > 0:
                #If the player has winnings from previous rounds, reset total to zero upon losing
                self.total = 0
            else:
                self.total -= bet[1]
                #If already at zero or negative, just update the display without changing the total
                pass
            print(f"\nSorry, you lost this round! Your total is now ${self.total:.2f}")
        
        self.update_wheel_and_feedback(spin)
        self.log_performance(name, self.total)


    #Checking if players bet equals the spin
    def resolve_bet(self, bet, spin):
        win_conditions = {
            'e': spin[0] % 2 == 0,
            'o': spin[0] % 2 != 0,
            'r': spin[1] == 'Red',
            'b': spin[1] == 'Black'
        }
        return win_conditions.get(bet[0], False)