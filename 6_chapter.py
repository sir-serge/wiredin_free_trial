import requests
import cv2 as cv
import os
import matplotlib.pyplot as plt
import numpy as np
import random

card_images = []

cards=[]

player=[]
marks = ['Hearts', 'Spades', 'Diamonds', 'Clubs']
display_names = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
numbers = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def load_image():
  image_name = 'cards.jpg'
  vsplit_number = 4
  hsplit_number = 13
  
  if not os.path.isfile(image_name):
    response = requests.get('https://raw.githubusercontent.com/techgymjp/techgym_python/master/cards.jpg', allow_redirects=False)
    with open(image_name, 'wb') as image:
      image.write(response.content)
   
  img = cv.imread('./'+image_name)
  img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
 
  h, w = img.shape[:2]
  crop_img = img[:h // vsplit_number * vsplit_number, :w // hsplit_number * hsplit_number]
  
  card_images.clear()
  for h_image in np.vsplit(crop_img, vsplit_number):
    for v_image in np.hsplit(h_image, hsplit_number):
      card_images.append(v_image)

#class card 
class Card:
  # initialization class
  def __init__(self,mark,display_name,number,image):
    self.mark=mark
    self.display_name=display_name
    self.number=number
    self.image=image
    self.is_dealt=False

#class player 
class Player:
  def __init__(self,name):
    self.name=name
    self.cards=[]
    self.total_number=0

#class human
class human(Player):
  def __init__(self):
    super().__init__("you")

class Computer(Player):
  def __init__(self):
    super().__init__("computer")

#fuction to create card as instance of class card
def Creat_card():
  cards.clear()

  for i, mark in enumerate(marks):
    for j, number in enumerate(numbers):
      # Create and append a Card with the current suit, name, value, and its corresponding image from a flat 52-card list.
      cards.append( Card(mark, display_names[j], number, card_images[i*len(numbers)+j]) )



#function to display card details 
def show_cards(cards):
  for i,card in enumerate(cards):  
    print(f"{card.display_name} of {card.mark}")
    plt.subplot(1,6,i+1)
    plt.axis("off")
    plt.imshow((card.image))
  plt.show()

def deal_card(player):
  tmp_cards = list(filter(lambda n: n.is_dealt == False, cards))
  assert (len(tmp_cards) != 0), "No cards left"

  tmp_card = random.choice( tmp_cards )
  tmp_card.is_dealt = True

  player.cards.append( tmp_card )
  player.total_number += tmp_card.number
  
def choise():
  choise_message=('hit[1] or stand[2]')
  choise_input=input(choise_message)
  while not enable_choise(choise_input):
    choise_input=input(choise_message)
  return int(choise_input)


def enable_choise(String):
  if String.isdigit():
    int_choise=int(String)
    if int_choise ==1 or int_choise==2:
      return True
    else:
      return False
  else:
    False
def win():
  print('won')

def Play_once():
  deal_card(player[0])
  deal_card(player[1])
  deal_card(player[0])
  show_cards(player[0].cards)
  if is_blackjack():
    win()
  else:
    if is_burst():
      lose()
    else:
      player_choice=choise()
      if player_choice==1:
        hit()
  
def is_blackjack():
  if player[0].total_number==21:
    return True
  else:
    return False

def hit():
  deal_card(player[0])
  show_cards(player[0].cards)
  if is_blackjack():
    win()
  else:
    if is_burst():
      lose()
    else:
      player_choice=choise()
      if player_choice==1:
        hit()

def is_burst():
  print(player[0].total_number)
  if player[0].total_number>21:
    
    return True
  else:
    return False


def lose():
  print('lost')

def play():
  print('Debug: play()')
  load_image()
  Creat_card()
  player.append(human())
  player.append(Computer())
  Play_once()
play()