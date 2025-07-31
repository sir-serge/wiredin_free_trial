import random

# Global variables
players = []
table = []
cells = []

MAX_HUMAN_BET = 99  # Max bet limit per turn for human

# Base Player class
class Player:
    def __init__(self, name, coin):
        self.name = name
        self.coin = coin
        self.bets = {i.name: 0 for i in table}  # Initialize bets on all cells to 0

    def set_bet_coin(self, bet_coin, bet_cell):
        self.coin -= bet_coin
        self.bets[bet_cell] += bet_coin
        # print(f"{self.name} bet {bet_coin} coin(s) to {bet_cell}.")
        print("{} bet {} coins(s) to {}".format(self.name,bet_coin,bet_cell))
    def reset_table(self):
        for key in self.bets:
            self.bets[key] = 0

# Human player class
class Human(Player):
    def __init__(self, name, coin):
        super().__init__(name, coin)

    def bet(self):
        if self.coin <= 0:
            print(f"{self.name} has no coins and cannot bet.")
            return

        max_valid_bet = min(self.coin, MAX_HUMAN_BET)
        while True:
            bet_coin_str = input(f"How many coins do you bet?: (1-{max_valid_bet}) ").strip()
            if self.enable_bet_coin(bet_coin_str, max_valid_bet):
                break
        bet_coin = int(bet_coin_str)

        while True:
            bet_cell = input("On what do you bet?: (R,B,1-8) ").strip()
            if self.enable_bet_cell(bet_cell):
                break

        super().set_bet_coin(bet_coin, bet_cell.upper())

    def enable_bet_coin(self, string, max_bet_coin):
        return string.isdigit() and 1 <= int(string) <= max_bet_coin

    def enable_bet_cell(self, string):
        return string.upper() in ['R', 'B'] or (string.isdigit() and 1 <= int(string) <= 8)

# Computer player class
class Computer(Player):
    def __init__(self, name, coin):
        super().__init__(name, coin)

    def bet(self):
        if self.coin <= 0:
            print(f"{self.name} has no coins and cannot bet.")
            return
        bet_coin = random.randint(1, min(99, self.coin))
        bet_cell = random.choice(cells)
        super().set_bet_coin(bet_coin, bet_cell)

# Cell class (no need to inherit Player)
class Cell:
    def __init__(self, name, rate, color):
        self.name = name
        self.rate = rate
        self.color = color

# ANSI color codes
class ColorBase:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    END = '\033[0m'

# Function to color output
def color(color_name, string):
    if color_name == "red":
        return ColorBase.RED + string + ColorBase.END
    elif color_name == 'green':
        return ColorBase.GREEN + string + ColorBase.END
    return string

# Green pipe used in table layout
def green_bar():
    return color("green", "|")

# Setup available cells from the table
def set_cell():
    global cells
    cells = [cell.name for cell in table]

# Create player instances
def create_player():
    global players
    my = Human("MY", 500)
    c1 = Computer("C1", 500)
    c2 = Computer("C2", 500)
    c3 = Computer("C3", 500)
    players = [my, c1, c2, c3]

# Set up roulette table with cells
def create_table():
    global table
    table = [Cell('R', 2, 'red'), Cell('B', 2, 'black')]
    for i in range(1, 9):
        color_name = 'red' if i % 2 != 0 else 'black'
        table.append(Cell(str(i), 8, color_name))

# Let all players place bets
def bet_player():
    for p in players:
        p.bet()

# Show the betting board with player bets
def show_table():
    row = green_bar() + '_____' + green_bar()
    for p in players:
        row += p.name + green_bar()
    print(row)

    for cell in table:
        row = green_bar() + color(cell.color, f"{cell.name}(×{cell.rate})") + green_bar()
        for p in players:
            row += str(p.bets[cell.name]).zfill(2) + green_bar()
        print(row)

# Randomly select a winning cell
def check_hit():
    win_index = random.randint(0, len(cells) - 1)
    print(f"Winning number is {cells[win_index]}.")
    return win_index

# Reward players based on winning cell (no extra output)
def win_player(win_index):
    win_cell = table[win_index]
    for p in players:
        amount = p.bets[win_cell.name]
        if amount > 0:
            p.coin += amount * win_cell.rate


# Reset all player bets to zero
def reset_table():
    for p in players:
        p.reset_table()

# Show current coin status for all players
def show_coin():
    print("[Players’ coin] " + ' / '.join(f"{p.name}: {p.coin}" for p in players) + " /")

# Check if any player is out of coins
def is_end_game():
    return any(p.coin <= 0 for p in players)

# End game message
def game_end():
    for p in players:
        if p.coin <= 0:
            print(f"Game Over! {p.name} has no coins left.")

# Setup game
def initialize():
    create_table()
    create_player()
    set_cell()

# Single round
def play_once():
    show_coin()
    bet_player()
    # show_coin()
    show_table()
    win_index = check_hit()
    win_player(win_index)
    reset_table()

# Game loop
def play():
    print("Debug: play()")
    initialize()
    # show_coin()
    while not is_end_game():
        play_once()
    game_end()

# Start game
play()
