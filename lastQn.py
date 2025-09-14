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
        # cards.clear()
        numbers = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        # display_names = ['Ace', '2', '3', '4', '5', '6',
        #                  '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        # marks = ['Spade', 'Heart', 'Diamond', 'Club']
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



    def win(self):
        self.show_result('win',self.players,self.cards)


    def lose(self):
        self.show_result('lose',self.players,self.cards)


    def choice(self):
        message = 'Hit[1] or stand[2]'
        choice_key = input(message)
        while not self.enable_choice(choice_key):
            choice_key = input(message)
        return int(choice_key)


    def enable_choice(string):
        if string.isdigit():
            number = int(string)
            if number >= 1 and number <= 2:
                return True
            else:
                return False
        else:
            return False


    def is_blackjack(self):
        if (self.players[0].total_number == 21):
            return True
        else:
            return False


    def is_bust(self):
        if (self.players[0].total_number >= 22):
            return True
        else:
            return False


    def hit(self):
        self.deal_card(self.players[0],self.cards)
        self.show_cards(self.players[0])
        if self.is_blackjack():
            self.win()
        elif self.is_bust():
            self.lose(self.players,self.cards)
        else:
            choice_key = self.choice()
            if choice_key == 1:
                self.hit(self.players)
            elif choice_key == 2:
                self.stand(self.players,self.cards)


    def stand(self):
        self.deal_card(self.players[1],self.cards)
        if self.is_bust(self.players[1]):
            self.win(self.players,self.cards)
        else:
            if self.players[1].total_number < 17:
                self.stand(self.players,self.cards)
            else:
                result = self.judge(self.players)
                self.show_result(result,self.players,self.cards)


    def judge(self):
        diff = self.players[0].total_number - self.players[1].total_number
        if diff == 0:
            result = 'draw'
        elif diff >= 1:
            result = 'win'
        else:
            result = 'lose'
        return result


    def show_result(result,self):
        for player in self.players:
            print(f"Cards of {player.name}:")
            self.show_cards(player.cards)

        if result == 'draw':
            print('Draw')
        elif result == 'win':
            print(f"{self.players[0].name} won")
        else:
            print(f"{self.players[1].name} won")



    def play_once(self):
        self.deal_card(self.players[0], self.cards)
        self.deal_card(self.players[1], self.cards)
        self.deal_card(self.players[0], self.cards)
        self.show_cards(self.players[0])
        if self.is_blackjack():
            self.win(self.players,self.cards)
        else:
            choice_key = self.choice()
            if choice_key == 1:
                self.hit(self.players,self.cards)
            elif choice_key == 2:
                self.stand(self.players,self.cards)


    def player_bets(result,bet_coins,coins):
            if result.lower()=='win':
                coins+=bet_coins
            elif result.lower()=='lose':
                coins-=bet_coins
            return coins
    def enable_bet_coin(self,input_coins):
        if input_coins.isdigit():
            input_coins = int(input_coins)
            if input_coins <=100 and input_coins >0:
                return True
    def play(self):
        # cards = []

        # players = []
        card_images = []
        load_image(card_images)
        self.create_cards(card_images)


        coins=500
        while coins>0:
            print(f'you have {coins} s')
            if coins<100:
                input_message=input(f'how many coins do want to bet(10-{coins})')
            else:
                input_message=input('how many coins do want to bet(10-100)')
            while not self.enable_bet_coin(input_message):
                if coins < 100:
                    input_message = input(f'how many coins do want to bet(10-{coins})')
                else:
                    input_message = input('how many coins do want to bet(10-100)')
            bet_coins=int(input_message)
            while bet_coins>100 or bet_coins<10 or bet_coins>coins:
                bet_coins=int(input_message)
            self.players.append(Human())
            self.players.append(Computer())
            self.play_once()
            coins+=self.player_bets(self.judge(self.players),bet_coins,coins)



play_game().play()
