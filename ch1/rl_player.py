from state import TicTacToeState
from agent import State, Agent
from random import random, choice
from typing import Optional


class RLPlayer(Agent):
    def __init__(self, alpha=0.1, exploit_ratio=0.8):
        # construct our model
        self.model: dict[State, float] = dict()
        self.alpha = alpha
        self.exploit_ratio = exploit_ratio

        self.last_move_was_greedy = False
        self.last_move = None

    def get_win_prob(self, state: State):
        if state not in self.model:
            self.model[state] = 0.5
        return self.model[state]

    def set_win_prob(self, state: State, win_prob: float):
        self.model[state] = win_prob

    def rank_neighbors(self, state: State):
        neighbors = [n.state for n in TicTacToeState(state).neighbors()]
        neighbors.sort(key=self.get_win_prob, reverse=True)
        return neighbors

    def update_win_prob(self, cur_state: State, adjusted_win_prob: Optional[float] = None):
        if adjusted_win_prob is not None:
            self.set_win_prob(cur_state, adjusted_win_prob)
        cur_win_prob = self.get_win_prob(cur_state)
        previous_win_prob = self.get_win_prob(self.last_move)
        self.set_win_prob(self.last_move, previous_win_prob + self.alpha * (cur_win_prob - previous_win_prob))

    def move(self, cur_state: State, possible_next_states: list[State]):

        # Update state for last move
        if self.last_move and self.last_move_was_greedy:
            self.update_win_prob(cur_state)

        exploit = random() < self.exploit_ratio
        explore = not exploit

        if explore:
            self.last_move_was_greedy = False
            self.last_move = choice(possible_next_states)
            return self.last_move
        else:
            self.last_move_was_greedy = True
            self.last_move = self.rank_neighbors(cur_state)[0]
            return self.last_move

    def new_game(self):
        self.last_move_was_greedy = False
        self.last_move = None

    def game_over(self, state: State, did_win: bool):
        if self.last_move_was_greedy:
            self.update_win_prob(state, 1 if did_win else 0)
