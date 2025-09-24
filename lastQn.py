import requests
import cv2 as cv
import os
import matplotlib.pyplot as plt
import numpy as np
import random


def load_image(card_images):
    image_name = 'cards.jpg'
    vsplit_number = 4
    hsplit_number = 13

    if not os.path.isfile(image_name):
        response = requests.get(
            'https://raw.githubusercontent.com/techgymjp/techgym_python/master/cards.jpg', allow_redirects=False)
        with open(image_name, 'wb') as image:
            image.write(response.content)

    img = cv.imread('./'+image_name)
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    h, w = img.shape[:2]
    crop_img = img[:h // vsplit_number * vsplit_number,
                   :w // hsplit_number * hsplit_number]

    card_images.clear()
    for h_image in np.vsplit(crop_img, vsplit_number):
        for v_image in np.hsplit(h_image, hsplit_number):
            card_images.append(v_image)


class Card:
    def __init__(self, mark, display_name, number, image):
        self.mark = mark
        self.display_name = display_name
        self.number = number
        self.image = image
        self.is_dealt = False


class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.total_number = 0


class Human(Player):
    def __init__(self):
        super().__init__('You')


class Computer(Player):
    def __init__(self):
        super().__init__('Computer')

class play_game:
    def __init__(self):
        self.players = [Human(), Computer()]
        self.cards = []
        self.marks = ['Spade', 'Heart', 'Diamond', 'Club']
        self.display_names = ['Ace', '2', '3', '4', '5', '6',
                 '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    def create_cards(self, card_images):
        numbers = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        for i, mark in enumerate(self.marks):
            for j, number in enumerate(numbers):
                self.cards.append(Card(mark, self.display_names[j], number, card_images[i*len(numbers)+j]))

    def show_cards(self, player):
        print(f"\n{player.name}'s cards: ", end="")
        for i, card in enumerate(player.cards):
            print(f"{card.display_name} of {card.mark}", end="  ")
            plt.subplot(1, len(player.cards), i + 1)
            plt.axis('off')
            plt.imshow(card.image)
        plt.show()
        print(f"  total: {player.total_number}")

    def deal_card(self, player, Cards):
        tmp_cards = list(filter(lambda n: n.is_dealt == False, self.cards))
        assert (len(tmp_cards) != 0), "No cards left"

        tmp_card = random.choice(tmp_cards)
        tmp_card.is_dealt = True

        player.cards.append(tmp_card)
        player.total_number += tmp_card.number
        self.calc_ace(player)

    def calc_ace(self, player):
        for card in player.cards:
            if player.total_number >= 22 and card.number == 11:
                player.total_number -= 10
                card.number = 1

    def choice(self):
        message = 'Hit[1] or stand[2]: '
        choice_key = input(message)
        while not self.enable_choice(choice_key):
            choice_key = input(message)
        return int(choice_key)

    def enable_choice(self, string):
        if string.isdigit():
            number = int(string)
            if number >= 1 and number <= 2:
                return True
            else:
                return False
        else:
            return False

    def is_blackjack(self, player):
        return player.total_number == 21

    def is_bust(self, player):
        return player.total_number > 21

    def hit(self):
        self.deal_card(self.players[0], self.cards)
        self.show_cards(self.players[0])
        
        if self.is_bust(self.players[0]):
            return 'lose'  # Player busts, loses immediately
        elif self.is_blackjack(self.players[0]):
            return 'win'   # Player hits 21
        else:
            choice_key = self.choice()
            if choice_key == 1:
                return self.hit()  # Continue hitting
            elif choice_key == 2:
                return self.stand()  # Stand and let dealer play

    def stand(self):
        # Dealer plays according to rules: hit until 17 or higher
        while self.players[1].total_number < 17:
            self.deal_card(self.players[1], self.cards)
            print(f"Dealer draws: {self.players[1].cards[-1].display_name} of {self.players[1].cards[-1].mark}")
        
        return self.judge()

    def judge(self):
        player_total = self.players[0].total_number
        dealer_total = self.players[1].total_number
        
        # Check for busts first
        if player_total > 21:
            return 'lose'
        elif dealer_total > 21:
            return 'win'
        
        # Neither busted, compare totals
        if player_total > dealer_total:
            return 'win'
        elif player_total < dealer_total:
            return 'lose'
        else:
            return 'draw'

    def show_result(self, result):
        for player in self.players:
            print(f"Cards of {player.name}:")
            self.show_cards(player)

        if result == 'draw':
            print('Draw!')
        elif result == 'win':
            print(f"{self.players[0].name} won!")
        else:
            print(f"{self.players[1].name} won!")

    def play_once(self):
        # Deal initial cards
        self.deal_card(self.players[0], self.cards)
        self.deal_card(self.players[1], self.cards)
        self.deal_card(self.players[0], self.cards)
        
        print("Dealer's face-up card:")
        print(f"{self.players[1].cards[0].display_name} of {self.players[1].cards[0].mark}")
        
        self.show_cards(self.players[0])
        
        # Check for initial blackjack
        if self.is_blackjack(self.players[0]):
            self.deal_card(self.players[1], self.cards)  # Dealer gets second card
            if self.is_blackjack(self.players[1]):
                return 'draw'
            else:
                return 'win'
        
        # Player's turn
        choice_key = self.choice()
        if choice_key == 1:
            result = self.hit()
        elif choice_key == 2:
            result = self.stand()
        
        return result

    def player_bets(self, result, bet_coins, coins):
        if result == 'win':
            return coins + bet_coins
        elif result == 'lose':
            return coins - bet_coins
        else:  # draw
            return coins

    def enable_bet_coin(self, input_coins, max_bet):
        if input_coins.isdigit():
            input_coins = int(input_coins)
            if 10 <= input_coins <= max_bet:
                return True
        return False

    def play(self):
        card_images = []
        load_image(card_images)
        self.create_cards(card_images)

        coins = 500
        while coins >= 10:  # Need at least 10 coins to play
            print(f'\nYou have {coins} coins')
            max_bet = min(100, coins)
            
            input_message = input(f'How many coins do you want to bet (10-{max_bet})? ')
            while not self.enable_bet_coin(input_message, max_bet):
                input_message = input(f'Invalid bet. Enter a number between 10 and {max_bet}: ')
            
            bet_coins = int(input_message)
            
            # Reset players for new game
            self.players = [Human(), Computer()]
            
            # Reset cards
            for card in self.cards:
                card.is_dealt = False
            
            print(f"\n--- New Game - Bet: {bet_coins} coins ---")
            result = self.play_once()
            self.show_result(result)
            
            coins = self.player_bets(result, bet_coins, coins)
            print(f"You now have {coins} coins")
        
        print("Game over! You don't have enough coins to continue playing.")


if __name__ == "__main__":
    play_game().play() 
