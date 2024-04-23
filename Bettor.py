class User_bet:
    def __init__(self):
        #Assigning the role
        self.player_role = self.choose_role()

    #Prompting the user for the role they want to play
    def choose_role(self):
        #Giving Guide lines of what dealer does and what bettor does
        print("\nNow it's time to choose whether to be the Bettor or the Dealer!")
        print("The Bettor gets to select a bet and if they win they get 1.5x their bet. \nThey then have the choice to walk away or play again where their bet + winnings roll over.")
        print("The Dealer on the other hand, spins the wheel and takes the wager if the bettor loses.")

        #Prompting the user for decision
        print(f"\nWould you like to be the Bettor (Type 'B') or Dealer (Type 'D')? ")
        role = input().strip().lower()

        #Checking if valid role is entered
        while role not in ['b', 'd']:
            print("Invalid Input. Please chose either Bettor (Type 'B') or Dealer (Type 'D')? ")
            role = input().strip().lower()

        return role

    #If user decides to be the bettor
    def bettor_bet(self, bet_size):
        if self.player_role == 'b':

            #Seeing if they want to bet numbers or colors
            print('\nThe Wheel has numbers 1 - 36, with Evens being Red and Odds being Black')
            print('You can chose to bet a even/odd or a color. They both will start out with a 50% probability but will fluctuate \nas the previous spin is removed from the board and you keep playing')
            print("\nTo Bet on Even/Odd (Type 'N') or Color (Type 'C'): ")
            bet_type = input().strip().lower()

            #Checking to make sure valid input
            while bet_type not in ['n', 'c']:
                print("Invalid Input. Please bet Even/Odd (Type 'N') or Color (Type 'C'):")
                bet_type = input().strip().lower()

            #If they want to bet numbers
            if bet_type == 'n':
                print("\nPlease Choose Even (Type 'E') or Odd (Type 'O') ")
                bet_choice = input().strip().lower()
                time.sleep(1)
                print('\nThe Wheel is now Spinning, Good Luck!')

                #Checking to make sure valid input
                while bet_choice not in ['e', 'o']:
                    print("Invalid input. Please Choose Even (Type 'E') or Odd (Type 'O'):")
                    bet_choice = input().strip().lower()
                    time.sleep(1)
                    print('\nThe Wheel is now Spinning, Good Luck!')

            #If user choses to bet colors
            else:
                print("\nPlease Chose Red (Type 'R') or Black (Type 'B')")
                bet_choice = input().strip().lower()
                time.sleep(1)
                print('\nThe Wheel is now Spinning, Good Luck!')

                #Making sure valid input
                while bet_choice not in ['r', 'b']:
                    print("Invalid input. Please Chose Red (Type 'R') or Black (Type 'B'):")
                    bet_choice = input().strip().lower()
                    time.sleep(1)
                    print('\nThe Wheel is now Spinning, Good Luck!')

            return (bet_choice, bet_size)