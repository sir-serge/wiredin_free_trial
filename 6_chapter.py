import requests
import cv2 as cv
import os
import matplotlib.pyplot as plt
import numpy as np
import random

# Global variables for cards and players
card_images = []
cards = []
player = []

# Card suits, names, and values
marks = ['Hearts', 'Spades', 'Diamonds', 'Clubs']
display_names = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
numbers = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def load_image():
    """
    Load the card deck image, split into individual card images for display.
    Downloads image if not present locally.
    """
    image_name = 'cards.jpg'
    vsplit_number = 4
    hsplit_number = 13
    
    if not os.path.isfile(image_name):
        response = requests.get('https://raw.githubusercontent.com/techgymjp/techgym_python/master/cards.jpg', allow_redirects=False)
        with open(image_name, 'wb') as image:
            image.write(response.content)
    
    img = cv.imread('./' + image_name)
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    
    h, w = img.shape[:2]
    crop_img = img[:h // vsplit_number * vsplit_number, :w // hsplit_number * hsplit_number]
    
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


class human(Player):
    def __init__(self):
        super().__init__("you")


class Computer(Player):
    def __init__(self):
        super().__init__("computer")


def Creat_card():
    """
    Create all 52 card objects and assign corresponding images.
    """
    cards.clear()
    for i, mark in enumerate(marks):
        for j, number in enumerate(numbers):
            cards.append(Card(mark, display_names[j], number, card_images[i*len(numbers)+j]))


def show_cards(cards):
    """
    Display card images of the given cards visually.
    """
    for i, card in enumerate(cards):
        plt.subplot(1, 6, i + 1)
        plt.axis("off")
        plt.imshow(card.image)
    plt.show()


def deal_card(player):
    """
    Deal a random undealt card to the player, update total,
    and adjust Ace value if needed.
    """
    tmp_cards = list(filter(lambda n: not n.is_dealt, cards))
    assert len(tmp_cards) != 0, "No cards left"
    
    tmp_card = random.choice(tmp_cards)
    tmp_card.is_dealt = True
    
    player.cards.append(tmp_card)
    player.total_number += tmp_card.number
    
    calc_ace(player)


def choise():
    """
    Prompt user for hit or stand input and validate.
    """
    choise_message = 'hit[1] or stand[2]'
    choise_input = input(choise_message)
    
    while not enable_choise(choise_input):
        choise_input = input(choise_message)
    
    return int(choise_input)


def enable_choise(String):
    """
    Validate if input is '1' (hit) or '2' (stand).
    """
    if String.isdigit():
        return int(String) in [1, 2]
    return False


def win():
    """
    Display both players' cards and print 'won' message.
    """
    for playing in player:
        print(f'Cards of {playing.name}:')
        show_cards(playing.cards)
    print('won')


def Play_once():
    """
    Initial card deal and main game play loop for human player.
    """
    deal_card(player[0])
    deal_card(player[1])
    deal_card(player[0])
    
    show_cards(player[0].cards)
    
    if is_blackjack():
        win()
    else:
        if is_burst(player[0]):
            lose()
        else:
            player_choice = choise()
            if player_choice == 1:
                hit()
                return
            elif player_choice == 2:
                stand()


def is_blackjack():
    """
    Check if human player has blackjack (21).
    """
    return player[0].total_number == 21


def hit():
    """
    Player hits: deal card, check blackjack or bust,
    else prompt again.
    """
    deal_card(player[0])
    show_cards(player[0].cards)
    
    if is_blackjack():
        win()
    else:
        if is_burst(player[0]):
            lose()
        else:
            player_choice = choise()
            if player_choice == 1:
                hit()
                return
            elif player_choice == 2:
                stand()


def is_burst(player):
    """
    Return True if player's total number exceeds 21 (bust).
    """
    return player.total_number > 21


def lose():
    """
    Display both players' cards and print 'lost' message.
    """
    for playing in player:
        print(f'Cards of {playing.name}:')
        show_cards(playing.cards)
    print('lost')


def stand():
    """
    Player stands: computer takes cards until total >= 17,
    then judge and show result.
    """
    deal_card(player[1])
    
    while player[1].total_number < 17:
        deal_card(player[1])
    
    result = judge()
    show_result(result)


def judge():
    """
    Determine the result based on player totals.
    """
    difference = player[0].total_number - player[1].total_number
    
    if difference == 0:
        return 'draw'
    elif difference > 0:
        return 'win'
    else:
        return 'lose'


def show_result(result):
    """
    Display final cards and the game result.
    """
    for playing in player:
        print(f'Cards of {playing.name}:')
        show_cards(playing.cards)
    
    if result == 'draw':
        print('draw')
    elif result == 'win':
        print('won')
    else:
        print('lost')


def calc_ace(player):
    """
    Adjust value of Aces from 11 to 1 as needed to prevent busting.
    """
    for card in player.cards:
        if player.total_number > 21 and card.number == 11:
            player.total_number -= 10
            card.number = 1


def play():
    """
    Initialize the game and start playing.
    """
    load_image()
    Creat_card()
    player.append(human())
    player.append(Computer())
    Play_once()


play()
