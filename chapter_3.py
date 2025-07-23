import random
import math
teams=[]
playing_teams={"myself":"enter your team choice (1-3)" ,"enemy":"enter your opponent's team(1-3)"}
class Team:
  def __init__(self, name,attack,defense):

    self.name = name
    self.attack=attack
    self.defense=defense

  def info(self):
    print(self.name + ': Offensive power:' + str(self.attack) + ' / Defensive power:' + str(self.defense))

  def show_info(self):
    print("Information of all teams")
    print(self.name + ': Offensive power:' + str(self.attack) + ' / Defensive power:' + str(self.defense))

  def get_hit_rate(self):
    return random.randint(10,self.attack)   
  
  def get_out_rate(self):
    return random.randint(10,self.defense)   



def create_teams():
  global teams
  team1=Team("Attackers", 80 ,20)
  team2=Team("Defenders", 30 ,70)
  team3=Team("Averages", 50, 50)
  teams=[team1,team2,team3]
  # team1.info()  

def show_info():
  global teams
  count=0
  for i in teams:
    count=count+1
    print(count)
    i.info()

def choice_team(choice):
    return int(input(choice))

def get_player_inning(inning_type):
  if inning_type=="top":
    score=teams[player].get_hit_rate()
    opponent_score=teams[opponent].get_out_rate()
  else:
    score=teams[opponent].get_hit_rate()
    opponent_score=teams[player].get_out_rate()    
  final=math.floor((score-opponent_score)/10)
  if final<0:
    final=0
  return final
  
  
def play():
  global player,opponent
  # player=0
  # opponent=0
  create_teams()
  show_info()
  player=choice_team(playing_teams["myself"])-1
  print(f"Your team is {teams[player].name}")
  opponent=choice_team(playing_teams["enemy"])-1
  print(f"Opponent’s team is {teams[opponent].name}")
  # debug_play=get_player_inning()
  # print(f"Debug: {debug_play}")
  score_board="________|"
  you="|"
  opponent_scores="|"
  add_top=0
  add_bottom=0
  for i in range(9):
    if i <8:
      score_board+=f" {i+1} |"
      top_score=get_player_inning("top")
      add_top+=top_score
      you+=(f" {top_score} |")
      bottom_score=get_player_inning("bottom")
      add_bottom+=bottom_score
      opponent_scores+=f" {bottom_score} |"
  else:
    if top_score==bottom_score:
      you+=(f" {top_score} |")
      opponent_scores+=f" {bottom_score} |"
      score_board+=f" {i+1} |"
      next
    else:
      score_board+=f" {i+1} |"
      if top_score>bottom_score:
        you+=(f" {top_score} |")
        # print(you)
        opponent_scores+=" X |"
        # print(opponent_scores)
      else:
        you+=" X |"
        # print(you)

        opponent_scores+=f" {bottom_score} |"
        # print(opponent_scores)
  print(f"{score_board} R |")
  print(f"You     {you} {add_top} | " )
  print(f"opponent{opponent_scores} {add_bottom} |")
play()