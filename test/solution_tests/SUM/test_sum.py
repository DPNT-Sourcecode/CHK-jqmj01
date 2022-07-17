from src.iwoca_challenges.challenge_1.sum_two_numbers import sum_two_numbers


class TestSum():
    def test_sum(self):
        assert sum_two_numbers(1, 2) == 3

