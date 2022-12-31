from random import choice
from agent import State, Agent


class RandomPlayer(Agent):
    def move(self, _cur_state: State, possible_next_states: list[State]):
        return choice(possible_next_states)

    def new_game(self):
        # stub
        pass

    def game_over(self, state: State, did_win: bool):
        # stub
        pass
