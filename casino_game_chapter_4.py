import random
players=[]
table=[]
bet={}

class Player:
  def __init__(self, name,coin,bet):
    self.name = name
    self.coin=coin
    self.bet=bet

  def info(self):
    print(f" {self.name} : {self.coin}")

  def set_bet_coin(self,bet_coin):
     self.coin-=bet_coin
     print(self.name + ' bets ' + str(bet_coin) + ' coin.')

     


class Human(Player):
  def __init__(self, name, coin):
    super().__init__(name, coin) 

  def bet(self):
    bet_message="How many coins do you bet: (1-99)?"
    bet_coin=input(bet_message)
    while not self.enable_bet_coin(bet_coin):
        bet_coin=input(bet_message)
    super().set_bet_coin(int(bet_coin))
    # print(bet_coin)
    return bet_coin

  def enable_bet_coin(self,string):
    
    if not string.isdigit():
        return False 
    else:
        num = int(string)
        if num >99 or num <1 :
            return False
  
        else:
            return True

class computer(Player):

  def __init__(self, name, coin):
     super().__init__(name, coin)

  def bet(self):
    coins=random.randint(1,99)
    if self.coin<=99:
      coins=self.coin
    bet_coin=random.randint(1,coins)
    super().set_bet_coin(bet_coin)


class cell(Player):
   def __init__(self, name, rate,color):
      self.name=name
      self.rate=rate
      self.color=color

class ColorBase:
  BLACK = '\033[30m'
  RED = '\033[31m'
  GREEN = '\033[32m'
  END = '\033[0m'

def create_player():
  global players
  my=Human("My",500)
  c1=computer("c1",500)
  c2=computer("c2",500)
  c3=computer("c3",500) 
  players=[my,c1,c2,c3]
  

def show_player():
   global players
   for i in players:
      i.info()
   for i in players:
      i.bet()
   for i in players:
      i.info()

def create_table():
    global table
    table.append(cell('R', 2, 'red'))
    table.append(cell('B', 2, 'black'))
    table.append(cell('1', 8, 'red'))
    table.append(cell('2', 8, 'black'))
    table.append(cell('3', 8, 'red'))
    table.append(cell('4', 8, 'black'))
    table.append(cell('5', 8, 'red'))
    table.append(cell('6', 8, 'black'))
    table.append(cell('7', 8, 'red'))
    table.append(cell('8', 8, 'black'))

def color(color_name,string):
   if color_name=="red":
      return ColorBase.RED + string + ColorBase.END
   elif color_name == 'green':
      return ColorBase.GREEN + string + ColorBase.END
   else:
      return string
def green_bar():
      return color("green","|")

def show_table():
   global table
   for i in table:
    print(green_bar() + color(i.color, ( i.name + '(x' + str(i.rate) + ')')) +green_bar())


def play():
  print('Debug:play()')
  # create_player()
  # show_player()
  create_table()
  show_table()    


play()