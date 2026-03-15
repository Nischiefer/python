class Player:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass

class HumanPlayer(Player):
    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square_str = input(f'Player {self.letter}, what is your next move? (0-8): ').strip()
            try:
                val = int(square_str)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid number. Try again.')
        return val

class RandomComputerPlayer(Player):
    def get_move(self, game):
        import random
        square = random.choice(game.available_moves())
        return square
