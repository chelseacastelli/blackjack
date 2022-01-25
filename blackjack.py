
import random

class Blackjack:
    def __init__(self, name, money):
       self.player = name
       self.money = money
       self.min_bet = 25.00

    def deal_card(self):
        card_values = {}

        for num in range(2, 11):
            card_values[num] = num

        card_values.update({'J': 10, 'Q': 10, 'K': 10, 'A': 11})

        return random.choice(list(card_values.items()))

    def hit(self):
        pass

    
    def stand(self, card_total, wager):
        if card_total >= 15 and card_total <= 21:
            self.money += round((wager + wager/2))
            print('Great job, you win!\nYour current pot is ${money}'.format(money = '{:.2f}'.format(round(self.money, 2))))
            break
        else:
            self.money -= wager
            print('You lose, sorry!\nYour current pot is ${money}'.format(money = '{:.2f}'.format(round(self.money, 2))))
            break


    def play(self):
        play = True
        print(f'Hello {self.player}! Welcome to BlackJack!\n\n3 to 2 Ratio\n$20 minimum\nThere is no dealer. If you sit with a total between 15 - 21, you win! Anything else, you lose.')

        while play:
            card_total = 0
            cards = []
            wager = ''
        
            while True:
                wager = float(input('What is your wager? '))
                if wager >= self.min_bet and wager <= self.money:
                    break
                else:
                    print('Please enter valid wager... ')

            for i in range(2):
                new_card = self.deal_card()
                card_total += new_card[1]
                cards.append(new_card[0])

            print(f'\nYour cards:\n{cards}\n\nTotal: {card_total}\n')
            
            while True:
                hit_or_stand = input('\nHit or Stand? ')
                
                if hit_or_stand[0].lower() != 'h':
                    self.stand(card_total, wager)
                
                else:
                    new_card = self.deal_card()
                    card_total += new_card[1]
                    cards.append(new_card[0])
                    print('\nCards: ', cards, '\n\nTotal: ', card_total)


                if card_total > 21:
                    self.money -= wager
                    print('You lose, sorry!\nYour current pot is ${money}'.format(money = '{:.2f}'.format(round(self.money, 2))))
                    break

                elif card_total == 21:
                    self.money += round((wager + wager/2))
                    print('Great job, you win!\nYour current pot is ${money}'.format(money = '{:.2f}'.format(round(self.money, 2))))
                    break

            if input('Would you like it play again? ')[0].lower() == 'n':
                play = False
                print('Thanks for playing!')
  

game_1 = Blackjack('Chelsea', 100)
game_1.play()