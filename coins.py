import random
import math

class Team:
    def __init__(self, name, attack, defense):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.score = 0
        self.special_inning = False
    
    def info(self):
        print(f"{self.name}: offensive power: {self.attack} / defensive power: {self.defense}")
    
    def decide_special_inning(self):
        self.special_inning = random.randint(1, 5) == 1
    
    def get_attack(self):
        return self.attack * 2 if self.special_inning else self.attack
    
    def get_defense(self):
        return self.defense * 2 if self.special_inning else self.defense
    
    def get_hit_rate(self, special=False):
        atk = self.attack * 2 if special else self.attack
        return random.randint(10, atk)
    
    def get_out_rate(self, special=False):
        df = self.defense * 2 if special else self.defense
        return random.randint(10, df)
    
    def reset_special_inning(self):
        self.special_inning = False

class Game:
    def __init__(self):
        self.teams = [
            Team('Attackers', 80, 20),
            Team('Defenders', 30, 70),
            Team('Averages', 50, 50)
        ]
        self.my_team = None
        self.enemy_team = None

    def show_teams(self):
        print("Information of all teams")
        for i, team in enumerate(self.teams, 1):
            print(i)
            team.info()

    def choose_teams(self):
        while True:
            choice = input("Select your team (1-3) ")
            if choice.isdigit() and 1 <= int(choice) <= 3:
                self.my_team = self.teams[int(choice)-1]
                print(f"Your team is {self.my_team.name}")
                break
        while True:
            choice = input("Select opponent's team (1-3) ")
            if choice.isdigit() and 1 <= int(choice) <= 3 and self.teams[int(choice)-1] != self.my_team:
                self.enemy_team = self.teams[int(choice)-1]
                print(f"Opponent's team is {self.enemy_team.name}")
                break

    def prepare_inning(self):
        self.my_team.decide_special_inning()
        self.enemy_team.decide_special_inning()

    def get_play_inning(self, inning):
        if inning == 'top':
            hit_rate = self.playing_teams['myself'].get_hit_rate(special=self.my_team.special_inning)
            out_rate = self.playing_teams['enemy'].get_out_rate(special=self.enemy_team.special_inning)
        elif inning == 'bottom':
            hit_rate = self.playing_teams['enemy'].get_hit_rate(special=self.enemy_team.special_inning)
            out_rate = self.playing_teams['myself'].get_out_rate(special=self.my_team.special_inning)

        inning_score = math.floor((hit_rate - out_rate) / 10)
        if inning_score < 0:
            inning_score = 0
        return inning_score

    def play(self):
        self.show_teams()
        self.choose_teams()
        self.playing_teams = {'myself': self.my_team, 'enemy': self.enemy_team}
        scoreboard = ['________|']
        my_scores = ['You      |']
        enemy_scores = ['Opponent |']
        
        for inning in range(1, 10):
            self.prepare_inning()
            scoreboard.append(f"{inning}|")
            my_score = self.get_play_inning('top')
            my_scores.append(f"{my_score}|")
            self.my_team.score += my_score
            enemy_score = self.get_play_inning('bottom')
            enemy_scores.append(f"{enemy_score}|")
            self.enemy_team.score += enemy_score
            self.my_team.reset_special_inning()
            self.enemy_team.reset_special_inning()
            
        scoreboard.append("R|")
        my_scores.append(f"{self.my_team.score}|")
        enemy_scores.append(f"{self.enemy_team.score}|")
        print(''.join(scoreboard))
        print(''.join(my_scores))
        print(''.join(enemy_scores))

# Run the game

Game().play()
