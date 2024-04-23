#Inheriting CasinoLogger to log Dealers output
class Dealer(CasinoLogger):
    def __init__(self, user_bet, log_path="lysek_casino_performance_log.txt"):
        super().__init__(log_path)
        self.user_bet = user_bet
        self.dealer_total = 0

    #Simulating what a player do for when user is dealer
    def manage_game(self):
        while True:
            #Randomly choses bet size
            bet_size = random.randint(100, 1001)
            bet_amount, bet_type = self.take_bets()

            #Spinning the wheel
            spin_result = self.wheel.spin_wheel()
            self.wheel.formatting_output(spin_result)

            #Checking if bettor won
            win = self.check_winner(bet_type, spin_result)
            self.pay_out(win, bet_amount)

            #If no numbers left
            if not self.wheel.wheel:
                print("No more numbers left on the wheel!")
                break

            #Checking to see if they want to play again
            decision = input("\nContinue playing? (Y/N): ").strip().lower()

            #Make sure its a valid decision
            while decision not in ['y', 'n']:
                print('Invalid input. Please enter "Y" for Yes or "N" for No.')
                decision = input("\nContinue playing? (Y/N): ").strip().lower()

            #Breaking the loop and outputting ending messages if they don't want to play anymore
            if decision == 'n':
                if self.dealer_total > 0:
                    print(f"\nThank you for playing! Your final total is ${self.dealer_total:.2f}")
                    print(
                        '\nPlease proceed to the chip booth to collect your winnings! We hope to see you again soon!')
                    time.sleep(2)
                    self.log_performance(name, self.dealer_total)
                else:
                    print(f"\nThank you for playing! Your final total is ${self.dealer_total:.2f}")
                    print('\nBetter Luck Next Time! We hope to see you again soon!')
                    time.sleep(2)
                    self.log_performance(name, self.dealer_total)
                break

    #Creating random simulation of what bettor would chose
    def take_bets(self):
        # Randomly choose bet amount between 100 and 1000 for bettor
        bet_amount = random.randint(100, 1000)

        print(f"\nThe Bettor is betting ${bet_amount}")

        # Randomly choose if bettor picks to bet color or even/odd
        bet_type = random.choice(['n', 'c'])
        bet_choice = None

        #If bettor is betting number when player is dealer
        if bet_type == 'n':
            #Randomly chosing even or odd
            bet_choice = random.choice(['e', 'o'])
            print(f"\nThe Bettor bet on {'Even' if bet_choice == 'e' else 'Odd'}")
            print('\nPress any key to spin the wheel:')
            spin_wheel = input()
            print('\nThe wheel is now spinning!')
            time.sleep(2)

        # If bettor is betting color when player is dealer
        elif bet_type == 'c':
            #Randomly chosing red or black
            bet_choice = random.choice(['r', 'b'])
            print(f"\nThe Bettor bet on {'Red' if bet_choice == 'r' else 'Black'}")
            print('\nPress any key to spin the wheel:')
            spin_wheel = input()
            print('\nThe wheel is now spinning!')
            time.sleep(2)
        return bet_amount, (bet_choice, bet_type)

    #Cecking to see if they won
    def check_winner(self, bet, spin):
        # Mapping bets to winning conditions
        if bet[1] == 'n':  # Number bet
            return (spin[0] % 2 == 0 and bet[0] == 'e') or (spin[0] % 2 != 0 and bet[0] == 'o')
        elif bet[1] == 'c':  # Color bet
            return (spin[1] == 'Red' and bet[0] == 'r') or (spin[1] == 'Black' and bet[0] == 'b')

    #Paying out the bettor or taking their money
    def pay_out(self, win, bet_amount):
        if win:
            self.dealer_total -= bet_amount * 1.5
            print(f"\nBettor wins! You pay out ${bet_amount * 1.5:.2f}. Your total is now ${self.dealer_total:.2f}")
        else:
            self.dealer_total += bet_amount
            print(f"\nBettor loses! You collect ${bet_amount:.2f}. Your total is now ${self.dealer_total:.2f}")