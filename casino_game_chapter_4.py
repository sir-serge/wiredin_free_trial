import random
players=[]
table=[]
cells=[]

class Player:
  def __init__(self, name,coin):
    self.name = name
    self.coin=coin
    self.bets={}
    for i in table:
      self.bets.update({i.name:00})

  def info(self):
    print(f" {self.name} : {self.coin}")

  def set_bet_coin(self,bet_coin,bet_cell):
     self.coin-=bet_coin
     self.bets[bet_cell] += bet_coin
     print(self.name + ' bets ' + str(bet_coin) + ' coin(s) to '+bet_cell)


     

class Human(Player):
  def __init__(self, name, coin,):
    super().__init__(name, coin) 
    # self.bet_cell=bet_cell


  def bet(self):
    bet_message="How many coins do you bet: (1-99)?"
    bet_coin=input(bet_message).strip()
    bet_cell_message=("On what do you bet?: (R, B, 1-8)") 
    bet_cell=input(bet_cell_message) 

    while not self.enable_bet_coin(bet_coin):
        bet_coin=input(bet_message)
    bet_coin_int=int(bet_coin)

    while not self.enable_bet_cell(bet_cell):
        bet_cell=input(bet_cell_message) 
    super().set_bet_coin(bet_coin_int,bet_cell)

  def enable_bet_coin(self,string):
    
    if not string.isdigit():
        return False 
    else:
        num = int(string)
        if num >99 or num <1 :
            return False
  
        else:
            return True
  def enable_bet_cell(self,string):
     if string=="R" or string=="b":
      return True
     elif string.isdigit() and 1 <= int(string) <= 8:
        return True
     else:
        return False
        

class computer(Player):

  def __init__(self, name, coin):
     super().__init__(name, coin)

  def bet(self):
    # coins=random.randint(1,99)
    if self.coin<=99:
      coins=99
    else:
       coins=self.coin
    bet_coin=random.randint(1,coins)
    cells=[]
    for i in table:
      cells.append(i.__dict__['name'])
      # print(cells)
    set_random_key=random.randint(0,(len(cells)-1))
    bet_cell=cells[set_random_key]
    super().set_bet_coin(bet_coin,bet_cell)

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
  #  for i in players:
  #     i.info()
   for i in players:
      i.bet()
  #  for i in players:
  #     i.info()

def bet_player():
   for i in players:
       i.bet()

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
  row = green_bar() + '_____' + green_bar()
  for player in players:
    row += player.name + green_bar()
  print(row)
 
  for cell in table:
    row = green_bar() + color(cell.color, cell.name + '(x' + str(cell.rate) + ')') + green_bar()
    for player in players:
      row += str(player.bets[cell.name]).zfill(2) + green_bar()
    print(row)

def set_cell():
   global cell
   cells=[]
   for i in table:
      cells.append(cell.__dict__['name'])

def play():
  print('Debug:play()')
  create_table()
  create_player()
  
  # show_player()
  show_table() 
  bet_player()
  show_table()
play()