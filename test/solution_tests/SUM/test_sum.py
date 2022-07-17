from solutions.SUM import sum_solution
import pytest


class TestSum():
    def test_sum(self):
        """
        GIVEN the sum_two_numbers fuction
        WHEN two positive numbers between 0 and 100 are passed
        THEN the output is the sum of those two numbers
        """
        assert sum_solution.compute(1, 2) == 3

    def test_sum_raises_exception(self):
        """
        GIVEN the sum_two_numbers fuction
        WHEN one of the input numbers is outside the 0-100 range
        THEN a ValueError exception is raised
        """

        with pytest.raises(ValueError) as e:
            res = sum_solution.compute(195, 2)

        assert "num1 must be in the range 0-100" in str(e)

        with pytest.raises(ValueError) as e:
            res = sum_solution.compute(2, -100)
        
        assert "num2 must be in the range 0-100" in str(e)
