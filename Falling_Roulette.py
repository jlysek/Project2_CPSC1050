""""
Author: Jarrett Lysek
Class: CPSC 1050
Date 4/18/2024

This is the main file called Falling_Roulette to run the falling roulette game

Game Title: Falling Roulette at the Lysek Casino
Map: Lysek Casino
Outputs: All time Leaderboard


Hello and Welcome to my RPG game! The game will take place in a navigable casino. The that we will play is called Fallining Roulette. There are two players in this game.
First the bettor, who will be making the decisions during the game and will have the option to continue playing or to take their winnings
each round. The Second player is the dealer who will win if the bettor busts. The game is structured as a minimum of a $100 buy in and a maximum of $1000,
from there the bettor picks can chose to bet a number: even or odd or can bet a color: red or black. A roulette wheel is then spun and
if their bet wins they are paid out 1.5x and that number is taken off the board. This is where the falling part aka persistent states occurs. The number it landed
on will now be taken off the board and the bettor will then have the option to either take their winnings or play again with the wheel now only having 35 numbers.
If they decide to play again they can bet again which now the board won't have a 50/50 probablity. The bets keep rolling over so you win you can't change your
bet size it is just your inital bet + the profit from the last round. So if they bet $100 the first round and won, now they have $150. If they decide to play again
and win they will have 1.5*150 $225 and this loop continue till the player losses or decides to walk away. The goal of the gameis to make the most money and be first on the
all-time leaderboard which will be an ouput log.
"""

#Imports
import os
import time
import random
from Setting_Up import Wheel
from Setting_Up import Results 
from Dealer import Dealer
from Bettor import User_bet

#Main 
def main():

    # Greeting the user and explaining how the game works
    print("\nHello and Welcome to my RPG game! The game will take place in a navigable casino. \nThe that we will play called Fallining Roulette. There are two players in this game."
      "\nFirst the bettor, who will be making the decisions during the game and will have the \noption to continue playing or to take their winnings"
      "\neach round. The Second player is the dealer who will win if the bettor busts. \nThe game is structured as a minimum of a $100 buy in and a maximum of $1000,"
      "\nfrom there the bettor picks can chose to bet a number: even or odd or can bet \na color: red or black. A roulette wheel is then spun and"
      "\nif their bet wins they are paid out 1.5x and that number is taken off the board. \nThis is where the falling part aka persistent states occurs. The number it landed"
      "\non will now be taken off the board and the bettor will then have the option to \neither take their winnings or play again with the wheel now only having 35 numbers."
      "\nIf they decide to play again they can bet again which now the board won't have \na 50/50 probablity. The bets keep rolling over so you win you can't change your"
      "\nbet size it is just your inital bet + the profit from the last round. \nSo if they bet $100 the first round and won, now they have $150. If they decide to play again"
      "\nand win they will have 1.5*150 $225 and this loop continue till the player \nlosses or decides to walk away.  The goal is to make the most money and be first on the "
      "\nall time leaderboard which will be an ouput log.")


    #Beggining message welcoming the user
    print("\nThank you for choosing the play at the Lysek Casino, Please provide your name to use as a Player ID. ")
    name = input()
    print(f'\nPerfect {name}, We are glad you are here! Lets Begin!')

    #Initializing all the classes and a tracker
    wheel = Wheel()
    user = User_bet()
    results = Results(wheel)
    tracker = 0

    #Main loop to go through play
    while True:

        #If user decides to be the dealer
        if user.player_role == 'd':
            print("\nThank you for choosing to be the Dealer!")
            dealer = Dealer(user)
            dealer.wheel = wheel
            dealer.manage_game(name)

            #Breaking out of loop when they are done and going to output log
            break

        #If user decides to be the bettor
        elif user.player_role == 'b':
            if results.total <= 0:
                #Getting bet
                print("\nThe minimum bet for this table is $100, the maximum is $1000, Please chose your initial wager size: ")
                bet_size = float(input())

                #Making sure bet is valid
                while bet_size < 100 or bet_size > 1000:
                    print('Invalid input. Please enter a number between 100 and 1000.')
                    bet_size = float(input())

            bet = user.bettor_bet(bet_size)
            if not bet:
                continue

            #Running the actual game once bet size is given
            spin = wheel.spin_wheel()
            wheel.formatting_output(spin)
            results.check_winner(bet, spin, name)

            #If no numbers left
            if not wheel.wheel:
                print("No more numbers left on the wheel!")
                break

            #Prompting to see if they want to keep playing
            print("\nDo you want to continue playing? (Y/N): ")
            dec = input().strip().lower()

            #Making sure decision is valid
            while dec not in ['y', 'n']:
                print('Invalid input. Please Enter Y for Yes or N for No')
                dec = input().strip().lower()

            #If user dosen't want to play anymore
            if dec != 'y':
                if results.total > 0:
                    print(f"\nThank you for playing! Your final total is ${results.total:.2f}")
                    print('\nPlease proceed to the chip booth to collect your winnings! We hope to see you again soon!')
                else:
                    print(f"\nThank you for playing! Your final total is ${results.total:.2f}")
                    print('\nBetter Luck Next Time! We hope to see you again soon!')
                break

    #Displaying the Leaderboard at the end
    results.display_leaderboard()

if __name__ == '__main__':
    main()