import unittest
from bowling_game_kata.BowlingGame import BowlingGame


class BowlingGameTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.game = BowlingGame()

    def test_can_roll(self):
        self.assertIsNone(self.game.roll(5))
        self.assertEqual(self.game.rolls, [5])

    def test_can_roll_many(self):
        self.assertIsNone(self.game.rollMany([1, 2, 3]))
        self.assertEqual(self.game.rolls, [1, 2, 3])

    def test_can_score(self):
        self.assertEqual(self.game.score(), 0)

    def test_gutter_game(self):
        self.game.rollMany([1 for _ in range(20)])
        self.assertEqual(self.game.score(), 20)

    def test_bad_game(self):
        self.game.rollMany([0 for _ in range(20)])
        self.assertEqual(self.game.score(), 0)

    def test_perfect_game(self):
        self.game.rollMany([10 for _ in range(12)])
        self.assertEqual(self.game.score(), 300)

    def test_one_spare(self):
        self.game.rollMany([3, 7, 3])
        self.game.rollMany([0 for _ in range(17)])
        self.assertEqual(16, self.game.score())

    def test_one_strike(self):
        self.game.rollMany([10, 3, 4])
        self.game.rollMany([0 for _ in range(16)])
        self.assertEqual(24, self.game.score())

    def test_game_1(self):
        self.game.rollMany([1, 4, 7, 2, 6, 4, 10, 6, 4, 4, 3, 6, 1, 8, 0, 0, 0, 3, 5])
        self.assertEqual(98, self.game.score())

    def test_game_2(self):
        self.game.rollMany([1, 4, 4, 5, 6, 4, 5, 5, 10, 0, 1, 7, 3, 6, 4, 10, 2, 8, 6])
        self.assertEqual(133, self.game.score())
