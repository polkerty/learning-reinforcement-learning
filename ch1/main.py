'''
Tic-Tac-Toe
'''
from rl_player import RLPlayer
from random_player import RandomPlayer
from state import TicTacToeState
from agent import Agent


class Game:
    def __init__(self, agent1: Agent, agent2: Agent):
        self.agent1 = agent1
        self.agent2 = agent2

    def play(self, print_boards=False):
        agent1.new_game()
        agent2.new_game()
        state = TicTacToeState()

        if print_boards:
            print(state)

        while len(state.neighbors()):
            agent = self.agent1 if state.turn == 1 else self.agent2
            choice = agent.move(state.state, [n.state for n in state.neighbors()])
            state = TicTacToeState(choice)

            if print_boards:
                print(state)

        agent1.game_over(state.state, state.winner == 1)
        agent2.game_over(state.state, state.winner == 2)

        return state.winner


if __name__ == '__main__':
    from random import seed

    seed('and-where-are-all-the-gods')

    agent2 = RLPlayer()
    agent1 = RandomPlayer()
    game = Game(agent1, agent2)

    winners = {0: 0, 1: 0, 2: 0}
    for _ in range(100000):
        winner = game.play()
        winners[winner] += 1

        print(f'{_}\tX: {winners[1]}\tY: {winners[2]}\tDraw: {winners[0]}')

    # for x, y in agent2.model.items():
    #     if y == 0.5:
    #         continue
    #     print(x, y)
