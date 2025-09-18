import random


class Player:
    def __init__(self, name, coin):
        self.name = name
        self.coin = coin
        self.bets = {}
        self.last_bet = None  # store (coin, cell) for possible doubling

    def set_bet_coin(self, bet_coin, bet_cell):
        self.coin -= bet_coin
        self.bets[bet_cell] = bet_coin
        self.last_bet = (bet_coin, bet_cell)  # remember last bet
        print(f"{self.name} bet {bet_coin} coin(s) to {bet_cell}.")

    def reset_table(self, table):
        for cell in table:
            self.bets[cell.name] = 0


class Human(Player):
    def __init__(self, name, coin):
        super().__init__(name, coin)

    def try_double_bet(self, table, computers):
        """Ask human if they want to bet double after a win"""
        if self.last_bet is None:
            return False  # no bet to double

        bet_coin, bet_cell = self.last_bet
        bet_double_message = input('You won! Do you want to bet double (y or n)? ')
        if bet_double_message.lower() == 'y':
            double_coin = bet_coin * 2
            self.reset_table(table)
            super().set_bet_coin(double_coin, bet_cell)

            # computers place bets normally for this round
            for comp in computers:
                comp.reset_table(table)
                comp.bet([c.name for c in table])
                # Remove initial bet print for computers who will double later

            print(f"MY Double bet placed: {double_coin} coin(s) on {bet_cell}.")
            return True
        return False

    def bet(self):
        max_bet_coin = min(99, self.coin)
        bet_coin = input(f'How many coins do you bet?:(1-{max_bet_coin}) ')
        while not self.enable_bet_coin(bet_coin, max_bet_coin):
            bet_coin = input(f'How many coins do you bet?:(1-{max_bet_coin}) ')

        bet_cell = input('On what do you bet?: (R, B, 1-8) ')
        while not self.enable_bet_cell(bet_cell):
            bet_cell = input('On what do you bet?: (R, B, 1-8) ')

        super().set_bet_coin(int(bet_coin), bet_cell)

    def enable_bet_coin(self, string, max_bet_coin):
        return string.isdigit() and 1 <= int(string) <= max_bet_coin

    def enable_bet_cell(self, string):
        return string in [str(i) for i in range(1, 9)] + ['R', 'B']


class Computer(Player):
    def __init__(self, name, coin):
        super().__init__(name, coin)

    def bet(self, cells):
        max_bet_coin = min(99, self.coin)
        bet_coin = random.randint(1, max_bet_coin)
        bet_cell = cells[random.randint(0, len(cells) - 1)]
        super().set_bet_coin(bet_coin, bet_cell)

    def try_double_bet(self, table):
        """50% chance to double on same cell after a win"""
        if self.last_bet is None:
            return False

        bet_coin, bet_cell = self.last_bet
        double_coin = bet_coin * 2
        if self.coin < double_coin:
            return False  # can't afford

        if random.random() < 0.5:  # 50% chance
            self.reset_table(table)
            super().set_bet_coin(double_coin, bet_cell)
            print(f"{self.name} chose to double! {double_coin} coin(s) on {bet_cell}.")
            return True
        return False


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
        self.cells = [cell.name for cell in self.table]

    def create_players(self):
        self.players = [
            Human('MY', 500),
            Computer('C1', 500),
            Computer('C2', 500),
            Computer('C3', 500)
        ]
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
        print(f'Winning number is {hit_cell}.')

        # Determine winners
        winners = []
        for player in self.players:
            won_cells = []
            if player.bets[hit_cell] >= 1:
                won_cells.append(hit_cell)
            if player.bets['R'] >= 1 and self.table[hit_cell_number].color == 'red':
                won_cells.append('R')
            if player.bets['B'] >= 1 and self.table[hit_cell_number].color == 'black':
                won_cells.append('B')
            if won_cells:
                winners.append((player, won_cells))
                for cell in won_cells:
                    self.win_player(player, cell)

        # Handle doubling
        human_wants_double = False
        doubling_computers = []
        for player, _ in winners:
            if isinstance(player, Human):
                if player.try_double_bet(self.table, [p for p in self.players if isinstance(p, Computer)]):
                    human_wants_double = True
            elif isinstance(player, Computer):
                if player.try_double_bet(self.table):
                    doubling_computers.append(player)

        # Show table after double bets
        if human_wants_double or doubling_computers:
            self.show_table()
            # If human doubled, spin for all again
            if human_wants_double:
                self.check_hit()
            # If only computers doubled, spin only for them
            elif doubling_computers:
                self.handle_computer_only_double(doubling_computers)

    def handle_computer_only_double(self, doubling_computers):
        hit_cell_number = random.randint(0, len(self.cells) - 1)
        hit_cell = self.cells[hit_cell_number]
        print(f'Winning number for computer double: {hit_cell}')
        for comp in doubling_computers:
            comp_won = False
            if comp.bets[hit_cell] >= 1:
                self.win_player(comp, hit_cell)
                comp_won = True
            if comp.bets['R'] >= 1 and self.table[hit_cell_number].color == 'red':
                self.win_player(comp, 'R')
                comp_won = True
            if comp.bets['B'] >= 1 and self.table[hit_cell_number].color == 'black':
                self.win_player(comp, 'B')
                comp_won = True
            if not comp_won:
                print(f"{comp.name} lost the double bet.")

    def win_player(self, player, bet_cell_name):
        table_cell = next((c for c in self.table if c.name == bet_cell_name), None)
        if table_cell:
            win_coin = player.bets[bet_cell_name] * table_cell.rate
            player.coin += win_coin
            print(f"{player.name} won on {bet_cell_name}. Gained {win_coin} coins.")

    def show_coin(self):
        message = '[Players\' coin] '
        message += ' / '.join(f"{p.name}: {p.coin}" for p in self.players)
        print(message)

    def create_table(self):
        self.table = [
            Cell('R', 2, 'red'),
            Cell('B', 2, 'black'),
            Cell('1', 8, 'red'),
            Cell('2', 8, 'black'),
            Cell('3', 8, 'red'),
            Cell('4', 8, 'black'),
            Cell('5', 8, 'red'),
            Cell('6', 8, 'black'),
            Cell('7', 8, 'red'),
            Cell('8', 8, 'black'),
        ]

    def show_table(self):
        row = self.green_bar() + '_____' + self.green_bar()
        for p in self.players:
            row += p.name + self.green_bar()
        print(row)
        for cell in self.table:
            row = self.green_bar() + self.color(cell.color, f"{cell.name}(x{cell.rate})") + self.green_bar()
            for p in self.players:
                row += str(p.bets[cell.name]).zfill(2) + self.green_bar()
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
        return any(p.coin <= 0 for p in self.players)

    def game_end(self):
        for p in self.players:
            if p.coin <= 0:
                print(f"Game ends as {p.name} has no coin.")

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
        self.game_end()


if __name__ == "__main__":
    Game_Play().play()
