State = tuple[tuple[int, ...], ...]


class Agent:
    def move(self, _cur_state: State, possible_next_states: list[State]):
        pass

    def new_game(self):
        # stub
        pass

    def game_over(self, state: State, did_win: bool):
        # stub
        pass
