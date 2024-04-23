
Author: Jarrett Lysek
Class: CPSC 1050
Date 4/18/2024
Project 2 

Game Title: Falling Roulette at the Lysek Casino
Map: Lysek Casino
Outputs: All time Leaderboard


Hello and Welcome to my RPG game! The game will take place in a navigable casino. The that we will play is called Fallining Roulette. There are two players in this game. First the bettor, who will be making the decisions during the game and will have the option to continue playing or to take their winnings each round. The Second player is the dealer who will win if the bettor busts. The game is structured as a minimum of a $100 buy in and a maximum of $1000,from there the bettor picks can chose to bet a number: even or odd or can bet a color: red or black. A roulette wheel is then spun and if their bet wins they are paid out 1.5x and that number is taken off the board. This is where the falling part aka persistent states occurs. The number it landed on will now be taken off the board and the bettor will then have the option to either take their winnings or play again with the wheel now only having 35 numbers. If they decide to play again they can bet again which now the board won't have a 50/50 probablity. The bets keep rolling over so you win you can't change your bet size it is just your inital bet + the profit from the last round. So if they bet $100 the first round and won, now they have $150. If they decide to play again and win they will have 1.5*150 $225 and this loop continue till the player losses or decides to walk away. The goal of the gameis to make the most money and be first on the all-time leaderboard which will be an ouput log.
