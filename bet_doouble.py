import random


class Player:
    def __init__(self, name, coin):
        self.name = name
        self.coin = coin
        self.bets = {}
        self.last_winning_bet = None  # store (coin, cell) for possible doubling

    def set_bet_coin(self, bet_coin, bet_cell):
        self.coin -= bet_coin
        self.bets[bet_cell] = bet_coin
        print(self.name + ' bet ' + str(bet_coin) +
              ' coin(s) to ' + bet_cell + '.')

    def reset_table(self, table):
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
            if 1 <= number <= max_bet_coin:
                return True
            else:
                return False
        else:
            return False

    def enable_bet_cell(self, string):
        if string.isdigit():
            number = int(string)
            if 1 <= number <= 8:
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

    def bet(self, cells):
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


class Game_Play:
    def __init__(self):
        self.players = []
        self.cells = []
        self.table = []
        self.win_player_bets = []  # Array to store winning players data

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

    def check_double_betting(self):
        """Check if any players want to double their winning bets"""
        players_to_double = []
        
        for win_data in self.win_player_bets:
            player_name = win_data[0]
            bet_cell = win_data[1]
            bet_coins = win_data[2]
            
            # Find the player object
            player = None
            for p in self.players:
                if p.name == player_name:
                    player = p
                    break
            
            if player is None:
                continue
                
            if isinstance(player, Human):
                # Ask human if they want to double
                double_message = input(f'{player.name}, you won on {bet_cell}! Do you want to bet double (y or n)? ')
                if double_message.lower() == 'y':
                    double_coins = bet_coins * 2
                    if player.coin >= double_coins:
                        players_to_double.append((player, bet_cell, double_coins))
                    else:
                        print(f"Not enough coins to double bet. You have {player.coin} coins.")
            
            elif isinstance(player, Computer):
                # Random choice for computer
                if random.choice([True, False]):
                    double_coins = bet_coins * 2
                    if player.coin >= double_coins:
                        players_to_double.append((player, bet_cell, double_coins))
                        print(f"{player.name} chose to double their bet on {bet_cell}!")
        
        return players_to_double

    def apply_double_bets(self, players_to_double):
        """Apply the double bets for selected players"""
        for player, bet_cell, double_coins in players_to_double:
            # Reset player's bets first
            player.reset_table(self.table)
            # Place the double bet
            player.set_bet_coin(double_coins, bet_cell)

    def bet_players(self):
        # First check if any winning players want to double their bets
        players_to_double = self.check_double_betting()
        
        # Clear the win_player_bets array for next round
        self.win_player_bets.clear()
        
        # Apply double bets first
        if players_to_double:
            self.apply_double_bets(players_to_double)
            # Get list of players who doubled
            doubled_players = [p[0] for p in players_to_double]
        else:
            doubled_players = []

        # Regular betting for players who didn't double
        for player in self.players:
            if player not in doubled_players:
                if isinstance(player, Computer):
                    player.bet(self.cells)
                else:
                    player.bet()

    def check_hit(self):
        hit_cell_number = random.randint(0, len(self.cells) - 1)
        hit_cell = self.cells[hit_cell_number]
        print('Winning number is ' + hit_cell + '.')

        for player in self.players:
            # Track which bet types this player won on to avoid duplicates
            player_wins = []
            
            # Case 1: Exact number bet
            if player.bets[hit_cell] >= 1:
                player_wins.append((hit_cell, player.bets[hit_cell]))

            # Case 2: Bet on "R"
            if player.bets['R'] >= 1 and self.table[hit_cell_number].color == 'red':
                player_wins.append(('R', player.bets['R']))

            # Case 3: Bet on "B"
            if player.bets['B'] >= 1 and self.table[hit_cell_number].color == 'black':
                player_wins.append(('B', player.bets['B']))
            
            # Process all wins for this player
            for bet_cell_name, bet_amount in player_wins:
                self.win_player(player, bet_cell_name, bet_amount)

    def win_player(self, player, bet_cell_name, bet_coins):
        table_cell = None
        for c in self.table:
            if c.name == bet_cell_name:
                table_cell = c
                break
        if table_cell:
            win_coin = bet_coins * table_cell.rate
            player.coin += win_coin
            print(player.name + ' won on ' + bet_cell_name +
                  '. Gained ' + str(win_coin) + ' coins.')
            
            # Check if this player-cell combination already exists to avoid duplicates
            existing_entry = None
            for entry in self.win_player_bets:
                if entry[0] == player.name and entry[1] == bet_cell_name:
                    existing_entry = entry
                    break
            
            if existing_entry:
                # Update existing entry with higher bet amount
                existing_entry[2] = max(existing_entry[2], bet_coins)
            else:
                # Add new winning player data to the array
                self.win_player_bets.append([player.name, bet_cell_name, bet_coins])

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


if __name__ == "__main__":
    Game_Play().play()
