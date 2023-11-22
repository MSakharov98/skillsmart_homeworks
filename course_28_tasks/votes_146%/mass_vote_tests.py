import unittest
from mass_vote import MassVote

class MassVoteTestCase(unittest.TestCase):
    def test_majority_winner(self):
        N = 5
        Votes = [10, 20, 30, 40, 50]
        self.assertEqual(MassVote(N, Votes), "minority winner 5")

    def test_minority_winner(self):
        N = 4
        Votes = [10, 20, 30, 30]
        self.assertEqual(MassVote(N, Votes), "minority winner 3")

    def test_no_winner(self):
        N = 3
        Votes = [10, 20, 30]
        self.assertEqual(MassVote(N, Votes), "no winner")

    def test_tie(self):
        N = 5
        Votes = [10, 20, 30, 30, 30]
        self.assertEqual(MassVote(N, Votes), "no winner")

    def test_zero_votes(self):
        N = 3
        Votes = [0, 0, 0]
        self.assertEqual(MassVote(N, Votes), "no winner")

    def test_single_candidate(self):
        N = 1
        Votes = [10]
        self.assertEqual(MassVote(N, Votes), "majority winner 1")


if __name__ == '__main__':
    unittest.main()
