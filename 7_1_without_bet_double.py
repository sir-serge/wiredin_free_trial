import random

class Player:
    def __init__(self, name, coin):
        self.name = name
        self.coin = coin
        self.bets = {}

    def set_bet_coin(self, bet_coin, bet_cell):
        self.coin -= bet_coin
        self.bets[bet_cell] = bet_coin
        print(self.name + ' bet ' + str(bet_coin) + ' coin(s) to ' + bet_cell + '.')

    def reset_table(self, table):
        for cell in table:
            self.bets.update({cell.name: 0})


class Human(Player):
    def __init__(self, name, coin):
        super().__init__(name, coin)

    def bet(self):
        max_bet_coin = min(99, self.coin)
        bet_message = 'How many coins do you bet?:(1-' + str(max_bet_coin) + ')'
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
            return 1 <= number <= max_bet_coin
        return False

    def enable_bet_cell(self, string):
        if string.isdigit():
            number = int(string)
            return 1 <= number <= 8
        else:
            return string in ['R', 'B']


class Computer(Player):
    def __init__(self, name, coin):
        super().__init__(name, coin)

    def bet(self, cells):
        max_bet_coin = min(99, self.coin)
        bet_coin = random.randint(1, max_bet_coin)
        bet_cell = random.choice(cells)
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


class Game_Play:
    def __init__(self):
        self.players = []
        self.cells = []
        self.table = []

    def set_cells(self):
        self.cells.clear()
        for cell in self.table:
            self.cells.append(cell.name)

    def create_players(self):
        self.players.clear()
        human = Human('MY', 500)
        computer1 = Computer('C1', 500)
        computer2 = Computer('C2', 500)
        computer3 = Computer('C3', 500)
        self.players.extend([human, computer1, computer2, computer3])

        for player in self.players:
            player.reset_table(self.table)

    def bet_players(self):
        for player in self.players:
            if isinstance(player, Computer):
                player.bet(self.cells)
            else:
                player.bet()

    def check_hit(self):
        hit_cell_number = random.randint(0, len(self.cells) - 1)
        hit_cell = self.cells[hit_cell_number]
        print('Winning number is ' + hit_cell + '.')

        for player in self.players:
            # Case 1: Exact number bet
            if player.bets[hit_cell] >= 1:
                self.win_player(player, hit_cell)

            # Case 2: Bet on "R"
            if player.bets['R'] >= 1 and self.table[hit_cell_number].color == 'red':
                self.win_player(player, 'R')

            # Case 3: Bet on "B"
            if player.bets['B'] >= 1 and self.table[hit_cell_number].color == 'black':
                self.win_player(player, 'B')

    def win_player(self, player, bet_cell_name):
        table_cell = None
        for c in self.table:
            if c.name == bet_cell_name:
                table_cell = c
                break
        if table_cell:
            win_coin = player.bets[bet_cell_name] * table_cell.rate
            player.coin += win_coin
            print(player.name + ' won on ' + bet_cell_name +
                  '. Gained ' + str(win_coin) + ' coins.')

    def show_coin(self):
        message = '[Players\' coin] '
        for player in self.players:
            message += player.name + ': ' + str(player.coin) + ' / '
        print(message)

    def create_table(self):
        self.table.clear()
        self.table.append(Cell('R', 2, 'red'))
        self.table.append(Cell('B', 2, 'black'))
        self.table.append(Cell('1', 8, 'red'))
        self.table.append(Cell('2', 8, 'black'))
        self.table.append(Cell('3', 8, 'red'))
        self.table.append(Cell('4', 8, 'black'))
        self.table.append(Cell('5', 8, 'red'))
        self.table.append(Cell('6', 8, 'black'))
        self.table.append(Cell('7', 8, 'red'))
        self.table.append(Cell('8', 8, 'black'))

    def show_table(self):
        row = self.green_bar() + '_____' + self.green_bar()
        for player in self.players:
            row += player.name + self.green_bar()
        print(row)

        for cell in self.table:
            row = self.green_bar() + self.color(cell.color, cell.name +
                                                '(x' + str(cell.rate) + ')') + self.green_bar()
            for player in self.players:
                row += str(player.bets[cell.name]).zfill(2) + self.green_bar()
            print(row)

    def reset_table(self):
        for player in self.players:
            player.reset_table(self.table)

    def color(self, color_name, string):
        if color_name == 'red':
            return ColorBase.RED + string + ColorBase.END
        elif color_name == 'green':
            return ColorBase.GREEN + string + ColorBase.END
        else:
            return string

    def green_bar(self):
        return self.color('green', '｜')

    def is_game_end(self):
        for player in self.players:
            if player.coin <= 0:
                return True
        return False

    def game_end(self):
        for player in self.players:
            if player.coin <= 0:
                print('Game ends as ' + player.name + ' has no coin.')

    def initialize(self):
        self.create_table()
        self.create_players()
        self.set_cells()

    def play_once(self):
        self.reset_table()
        self.bet_players()
        self.show_table()
        self.check_hit()
        self.show_coin()

    def play(self):
        self.initialize()
        self.show_coin()
        while not self.is_game_end():
            self.play_once()
        else:
            self.game_end()


Game_Play().play()
