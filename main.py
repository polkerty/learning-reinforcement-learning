'''
Tic-Tac-Toe
'''


class TicTacToeState:
    def __init__(self, state=None):
        if not state:
            state = ((0,) * 3,) * 3
        self.state = state

        self.winner = self.compute_winner()
        self.turn = self.compute_turn()

        self.value = 0.5

    def compute_turn(self):
        x_count = sum(cell == 1 for row in self.state for cell in row)
        o_count = sum(cell == 2 for row in self.state for cell in row)

        turn = 1 if x_count <= o_count else 2
        return turn

    def compute_winner(self):
        for w in [1, 2]:
            if (w,) * 3 in self.state:
                return w

            for col in range(3):
                if w == self.state[0][col] == self.state[1][col] == self.state[2][col]:
                    return w

            if w == self.state[0][0] == self.state[1][1] == self.state[2][2]:
                return w
            if w == self.state[0][2] == self.state[1][1] == self.state[2][0]:
                return w

    def neighbors(self):
        if self.winner:
            return []

        neighbors = []

        for row in range(3):
            for col in range(3):
                if self.state[row][col] == 0:
                    state = self.state[:row] + (
                        self.state[row][:col] + (self.turn,) + self.state[row][col + 1:],) + self.state[row + 1:]
                    neighbors.append(TicTacToeState(state))

        return neighbors

    def __str__(self):
        ret = ''
        for ri, row in enumerate(self.state):
            if ri == 0:
                ret += '_' * (len(row) * 2 + 1) + '\n'
            for ci, col in enumerate(row):
                if ci == 0:
                    ret += '|'
                ret += 'X' if col == 1 else 'O' if col == 2 else ' '
                ret += '|'
            ret += '\n'

            ret += '_' * (len(row) * 2 + 1) + '\n'

        return ret


if __name__ == '__main__':
    game = TicTacToeState()

    print(game)

    for neighbor in game.neighbors():
        print(neighbor)
