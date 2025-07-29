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
    if self.coin <= 99:
        coins = self.coin
    else:
        coins = 99
    bet_coin = random.randint(1, coins)

    set_random_key = random.randint(0, len(cells) - 1)
    bet_cell = cells[set_random_key]
    super().set_bet_coin(bet_coin, bet_cell)


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

   
def set_cell():
    global cells
    cells = [cell.name for cell in table] 


def create_player():
  global players
  my=Human("My",500)
  c1=computer("c1",500)
  c2=computer("c2",500)
  c3=computer("c3",500) 
  players=[my,c1,c2,c3]


def create_table():
    global table
    table=[]
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

def bet_player():
   for i in players:
       i.bet()

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
def check_hit():
  win_cell=random.randint(0,len(cells)-1)
  print(f'the winning number is {cells[win_cell]}')
  print(f'{cells}')
  for player in players:
      if player.bets[cells[win_cell]] >= 1:
          print(player.name + ' won ')
  return( win_cell)
def win_player(win_cell):
  number=0
  print(f"win cell {win_cell}")
  gained_message=(f'gained {number} coins')
  if(win_cell<3 and win_cell>=1):
      number+=(win_cell-1)*2 
      gained_message=(f'gained {number} coins')
  else:
      number+=win_cell*8
      gained_message=(f'gained {number} coins')

  print(gained_message)   
def show_coin():
  player_coins=('[player\'s coun] ')
  for i in players:
      player_coins+=(f"{i.name} : {i.coin} /")
  print(player_coins)

def initialize():
   create_table()
   create_player()
   set_cell()
def play_once():
   bet_player()
   show_coin()
   show_table()
   winn_gain=check_hit()
   win_player(winn_gain)
  #  show_coin()


def play():
  print('Debug:play()')
  initialize()
  # show_coin
  play_once()
  # create_table()
  # create_player()
  # show_coin()
  # set_cell()
  # # show_table() 
  # bet_player()
  # show_table()
  # winn_gain=check_hit()
  # win_player(winn_gain)
  # show_coin()

play()