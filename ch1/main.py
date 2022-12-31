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

    def play(self):
        agent1.new_game()
        agent2.new_game()
        state = TicTacToeState()

        print(state)

        while len(state.neighbors()):
            agent = self.agent1 if state.turn == 1 else self.agent2
            choice = agent.move(state.state, [n.state for n in state.neighbors()])
            state = TicTacToeState(choice)

            print(state)

        agent1.game_over(state.state, state.winner == 1)
        agent2.game_over(state.state, state.winner == 2)


if __name__ == '__main__':
    agent1: Agent = RLPlayer()
    agent2: Agent = RandomPlayer()
    game = Game(agent1, agent2)

    game.play()
