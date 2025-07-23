import random

class Player:
  def __init__(self, name,coin):
    self.name = name
    self.coin=coin
  def info(self):
    print(f" {self.name} : {self.coin}")
  def set_bet_coin(self,bet_coin):
     


class Human(Player):
    def __init__(self, name, coin):
        super().__init__(name, coin) 

    def bet(self):
        bet_message="How many coins do you bet: (1-99)?"
        bet_coin=input(bet_message)
        while not self.enable_bet_coin(bet_coin):
            bet_coin=input(bet_message)

        print(bet_coin)
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
           


def get_player():
  my=Human("My",3)
  my.info()
  my.bet()


def play():
  print('Debug:play()')
  get_player()

play()