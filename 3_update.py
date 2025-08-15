import random
import math

teams = []
playing_teams = {'myself': False, 'enemy': False}


class Team:
    def __init__(self, name, attack, defense):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.total_score = 0

    def info(self):
        print(self.name + ': Offensive power:' + str(self.attack) +
              ' / Defensive power:' + str(self.defense))

    def get_hit_rate(self):
        return random.randint(10, self.attack)

    def get_out_rate(self):
        return random.randint(10, self.defense)


def create_teams():
    global teams
    team1 = Team('Atackers', 80, 20)
    team2 = Team('Defenders', 30, 70)
    team3 = Team('Averages', 50, 50)
    teams = [team1, team2, team3]


def show_teams():
    index = 1
    print('Information of all teams')
    for team in teams:
        print(str(index))
        team.info()
        index += 1


def choice_team(player):
    global choice_team_number_you  # store Player 1's choice for comparison

    if player == 'myself':  # Player 1
        player_name = 'Your'
        choice_team_number_you = input('Select ' + player_name + ' team(1-3)')
        valid_input = validation(choice_team_number_you)

        while valid_input is None:  # keep asking until valid
            choice_team_number = input('Select ' + player_name + ' team(1-3) ')
            valid_input = validation(choice_team_number)

    elif player == 'enemy':  # Player 2
        player_name = 'Opponent\'s'
        choice_team_number_opponent = input('Select ' + player_name + ' team(1-3)')

        while choice_team_number_you == choice_team_number_opponent:  # avoid duplicate team
            choice_team_number_opponent = input('Select ' + player_name + ' team(1-3)')

        valid_input = validation(choice_team_number_opponent)
        while valid_input is None:  # keep asking until valid
            choice_team_number_opponent = input('Select ' + player_name + ' team(1-3) ')
            valid_input = validation(choice_team_number_opponent)

    playing_teams[player] = teams[valid_input - 1]  # assign chosen team
    print(player_name + ' team is \'' + playing_teams[player].name + '\'')


def validation(number):
    # return valid team number (1–2) or None
    if number.isdigit():
        convert_to_digit = int(number)
        if 0 < convert_to_digit <= 3:
            return convert_to_digit
    return None


def get_play_inning(inning):
    if inning == 'top':
        hit_rate = playing_teams['myself'].get_hit_rate()
        out_rate = playing_teams['enemy'].get_out_rate()
    elif inning == 'bottom':
        hit_rate = playing_teams['enemy'].get_hit_rate()
        out_rate = playing_teams['myself'].get_out_rate()
    inning_score = math.floor((hit_rate - out_rate) / 10)
    if inning_score < 0:
        inning_score = 0
    return inning_score


def play():
    create_teams()
    show_teams()
    choice_team('myself')
    choice_team('enemy')
    score_boards = ['________|', 'You     |', 'Opponent|']
    for i in range(9):
        score_boards[0] += str(i + 1) + '｜'
        # attack of the top
        inning_score = get_play_inning('top')
        score_boards[1] += str(inning_score) + '｜'
        playing_teams['myself'].total_score += inning_score
        # attack of the bottom
        if i == 8 and playing_teams['myself'].total_score < playing_teams['enemy'].total_score:
            score_boards[2] += 'X｜'
        else:
            inning_score = get_play_inning('bottom')
            score_boards[2] += str(inning_score) + '｜'
            playing_teams['enemy'].total_score += inning_score
    score_boards[0] += 'R｜'
    score_boards[1] += str(playing_teams['myself'].total_score) + '｜'
    score_boards[2] += str(playing_teams['enemy'].total_score) + '｜'
    print(score_boards[0])
    print(score_boards[1])
    print(score_boards[2])


play() 
