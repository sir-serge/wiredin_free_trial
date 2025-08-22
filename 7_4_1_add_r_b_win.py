import random

table = []


class Player:
    def __init__(self, name, coin):
        self.name = name
        self.coin = coin
        self.bets = {}
        self.reset_table()

    def set_bet_coin(self, bet_coin, bet_cell):
        self.coin -= bet_coin
        self.bets[bet_cell] = bet_coin
        print(self.name + ' bet ' + str(bet_coin) +
              ' coin(s) to ' + bet_cell + '.')

    def reset_table(self):
        for cell in table:
            self.bets.update({cell.name: 0})


class Human(Player):
    def __init__(self, name, coin):
        super().__init__(name, coin)

    def bet(self):
        if self.coin >= 99:
            max_bet_coin = 99
        else:
            max_bet_coin = self.coin
        bet_message = 'How many coins do you bet?:(1-' + \
            str(max_bet_coin) + ')'
        bet_coin = input(bet_message)
        while not self.enable_bet_coin(bet_coin, max_bet_coin):
            bet_coin = input(bet_message)

        bet_message = 'On what do you bet?: (R, B, 1-8)'
        bet_cell = input(bet_message)
        while not self.enable_bet_cell(bet_cell):
            bet_cell = input(bet_message)

        super().set_bet_coin(int(bet_coin), bet_cell)

    def enable_bet_coin(self, string, max_bet_coin):
        if string.isdigit():
            number = int(string)
            if number >= 1 and number <= max_bet_coin:
                return True
            else:
                return False
        else:
            return False

    def enable_bet_cell(self, string):
        if string.isdigit():
            number = int(string)
            if number >= 1 and number <= 8:
                return True
            else:
                return False
        else:
            if string == 'R' or string == 'B':
                return True
            else:
                return False


class Computer(Player):
    def __init__(self, name, coin):
        super().__init__(name, coin)

    def bet(self, cells):  # Pass cells as parameter
        if self.coin >= 99:
            max_bet_coin = 99
        else:
            max_bet_coin = self.coin
        bet_coin = random.randint(1, max_bet_coin)

        bet_cell_number = random.randint(0, len(cells) - 1)
        bet_cell = cells[bet_cell_number]
        super().set_bet_coin(bet_coin, bet_cell)


class Cell:
    def __init__(self, name, rate, color):
        self.name = name
        self.rate = rate
        self.color = color


class ColorBase:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    END = '\033[0m'


def set_cells(cells):
    cells.clear()  
    for cell in table:
        cells.append(cell.name)  # Simplified from cell.__dict__['name']


def create_players(players):
    players.clear()  # Clear any existing players
    human = Human('MY', 500)
    computer1 = Computer('C1', 500)
    computer2 = Computer('C2', 500)
    computer3 = Computer('C3', 500)
    # Use extend() to add all players to the existing list
    players.extend([human, computer1, computer2, computer3])


def bet_players(players, cells):
    for player in players:
        if isinstance(player, Computer):
            player.bet(cells)  # Pass cells to Computer players
        else:
            player.bet()  # Human players don't need cells


def check_hit(cells, players):
    hit_cell_number = random.randint(0, len(cells) - 1)
    hit_cell = cells[hit_cell_number]
    print('Winning number is ' + hit_cell + '.')

    for player in players:
        # Case 1: Exact number bet
        if player.bets[hit_cell] >= 1:
            win_player(player, hit_cell)

        # Case 2: Bet on "R"
        if player.bets['R'] >= 1 and table[hit_cell_number].color == 'red':
            win_player(player, 'R')

        # Case 3: Bet on "B"
        if player.bets['B'] >= 1 and table[hit_cell_number].color == 'black':
            win_player(player, 'B')


def win_player(player, bet_cell_name):
    table_cell = None
    for c in table:
        if c.name == bet_cell_name:
            table_cell = c
            break   # stop searching when found

    if table_cell:  # if we found it
        win_coin = player.bets[bet_cell_name] * table_cell.rate
        player.coin += win_coin
        print(player.name + ' won on ' + bet_cell_name +
              '. Gained ' + str(win_coin) + ' coins.')


def show_coin(players):
    message = '[Players\' coin] '
    for player in players:
        message += player.name + ': ' + str(player.coin) + ' / '
    print(message)


def create_table():
    global table
    table.append(Cell('R', 2, 'red'))
    table.append(Cell('B', 2, 'black'))
    table.append(Cell('1', 8, 'red'))
    table.append(Cell('2', 8, 'black'))
    table.append(Cell('3', 8, 'red'))
    table.append(Cell('4', 8, 'black'))
    table.append(Cell('5', 8, 'red'))
    table.append(Cell('6', 8, 'black'))
    table.append(Cell('7', 8, 'red'))
    table.append(Cell('8', 8, 'black'))


def show_table(players):
    row = green_bar() + '_____' + green_bar()
    for player in players:
        row += player.name + green_bar()
    print(row)

    for cell in table:
        row = green_bar() + color(cell.color, cell.name +
                                  '(x' + str(cell.rate) + ')') + green_bar()
        for player in players:
            row += str(player.bets[cell.name]).zfill(2) + green_bar()
        print(row)


def reset_table(players):
    for player in players:
        player.reset_table()


def color(color_name, string):
    if color_name == 'red':
        return ColorBase.RED + string + ColorBase.END
    elif color_name == 'green':
        return ColorBase.GREEN + string + ColorBase.END
    else:
        return string


def green_bar():
    return color('green', '｜')


def is_game_end(players):
    for player in players:
        if player.coin <= 0:
            return True
    return False


def game_end(players):
    for player in players:
        if player.coin <= 0:
            print('Game ends as ' + player.name + ' has no coin.')


def initialize(cells, players):
    create_table()
    create_players(players)
    set_cells(cells)


def play_once(cells, players):
    reset_table(players)
    bet_players(players, cells)
    show_table(players)
    check_hit(cells, players)
    show_coin(players)


def play():
    players = []
    cells = []
    initialize(cells, players)
    show_coin(players)
    while not is_game_end(players):
        play_once(cells, players)
    else:
        game_end(players)


play()
