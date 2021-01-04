# 4.01.21 3m 10.557s
# 4.01.21 2m 01.365s
# 4.01.21 1m 59.964s
from typing import List


class BowlingGame:
    def __init__(self):
        self.rolls: List[int] = []

    def roll(self, pins: int) -> None:
        self.rolls.append(pins)

    def rollMany(self, pins_list: List[int]) -> None:
        self.rolls += pins_list

    def _check_strike(self, roll_i) -> bool:
        return self.rolls[roll_i] == 10

    def _check_spare(self, roll_i) -> bool:
        return self.rolls[roll_i] + self.rolls[roll_i + 1] == 10

    def score(self) -> int:
        score = 0
        roll_i = 0
        for frame in range(10):
            if roll_i >= len(self.rolls):
                break
            if self._check_strike(roll_i):
                score += 10 + self.rolls[roll_i + 1] + self.rolls[roll_i + 2]
                roll_i += 1
            elif self._check_spare(roll_i):
                score += 10 + self.rolls[roll_i + 2]
                roll_i += 2
            else:
                score += self.rolls[roll_i] + self.rolls[roll_i + 1]
                roll_i += 2
        return score