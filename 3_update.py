import random
import math

class Team:
    def __init__(self, name, attack, defense):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.total_score = 0

    def info(self):
        print(f"{self.name}: Offensive power:{self.attack} / Defensive power:{self.defense}")

    def get_hit_rate(self, special=False):
        atk = self.attack * 2 if special else self.attack
        return random.randint(10, atk)

    def get_out_rate(self, special=False):
        df = self.defense * 2 if special else self.defense
        return random.randint(10, df)


def create_teams():
    return [
        Team('Attackers', 80, 20),
        Team('Defenders', 30, 70),
        Team('Averages', 50, 50)
    ]


def show_teams(teams):
    print('Information of all teams')
    for i, team in enumerate(teams, start=1):
        print(i)
        team.info()


def choice_team(player, teams, chosen_number=None):
    if player == 'myself':
        player_name = 'Your'
    else:
        player_name = "Opponent's"

    while True:
        choice = input(f'Select {player_name} team (1-3): ')
        if not choice.isdigit():
            print("Invalid input! Must be a number 1–3.")
            continue
        choice_number = int(choice)
        if choice_number < 1 or choice_number > 3:
            print("Invalid input! Must be 1, 2, or 3.")
            continue
        if chosen_number and choice_number == chosen_number:
            print("That team is already taken! Pick another.")
            continue
        break
    print(f"{player_name} team is '{teams[choice_number - 1].name}'")
    return choice_number


def get_play_inning(inning, playing_teams):
    # Determine special innings independently for each team (1/5 chance)
    special_myself = random.randint(1, 5) == 1
    special_enemy = random.randint(1, 5) == 1

    if inning == 'top':
        hit_rate = playing_teams['myself'].get_hit_rate(special_myself)
        out_rate = playing_teams['enemy'].get_out_rate(special_enemy)
    else:  # bottom
        hit_rate = playing_teams['enemy'].get_hit_rate(special_enemy)
        out_rate = playing_teams['myself'].get_out_rate(special_myself)

    inning_score = math.floor((hit_rate - out_rate) / 10)
    if inning_score < 0:
        inning_score = 0

    # Print special inning info
    if special_myself and inning == 'top':
        print(">>> Your team is in a SPECIAL INNING! (Attack doubled)")
    if special_enemy and inning == 'top':
        print(">>> Opponent's defense is SPECIAL this inning! (Defense doubled)")
    if special_enemy and inning == 'bottom':
        print(">>> Opponent's team is in a SPECIAL INNING! (Attack doubled)")
    if special_myself and inning == 'bottom':
        print(">>> Your defense is SPECIAL this inning! (Defense doubled)")

    return inning_score


def play():
    # Local variables
    teams = create_teams()
    playing_teams = {}

    show_teams(teams)

    # Player picks
    player_choice = choice_team('myself', teams)
    playing_teams['myself'] = teams[player_choice - 1]

    # Opponent picks
    enemy_choice = choice_team('enemy', teams, chosen_number=player_choice)
    playing_teams['enemy'] = teams[enemy_choice - 1]

    score_boards = ['________|', 'You     |', 'Opponent|']

    for i in range(9):
        score_boards[0] += str(i + 1) + '｜'

        # top half
        inning_score = get_play_inning('top', playing_teams)
        score_boards[1] += str(inning_score) + '｜'
        playing_teams['myself'].total_score += inning_score

        # bottom half
        if i == 8 and playing_teams['myself'].total_score < playing_teams['enemy'].total_score:
            score_boards[2] += 'X｜'
        else:
            inning_score = get_play_inning('bottom', playing_teams)
            score_boards[2] += str(inning_score) + '｜'
            playing_teams['enemy'].total_score += inning_score

    # totals
    score_boards[0] += 'R｜'
    score_boards[1] += str(playing_teams['myself'].total_score) + '｜'
    score_boards[2] += str(playing_teams['enemy'].total_score) + '｜'

    # print scoreboard
    for line in score_boards:
        print(line)

    # Announce winner
    if playing_teams['myself'].total_score > playing_teams['enemy'].total_score:
        print("\n>>> You win!")
    elif playing_teams['myself'].total_score < playing_teams['enemy'].total_score:
        print("\n>>> Opponent wins!")
    else:
        print("\n>>> It's a draw!")


play()
