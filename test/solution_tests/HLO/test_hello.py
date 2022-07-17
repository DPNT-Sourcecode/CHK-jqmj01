from lib.solutions.HLO.hello_solution import hello
from solutions.HLO.hello_solution import hello
import pytest


class TestSum():
    def test_sum(self):
        """
        GIVEN the hello_solution fuction
        WHEN a string is passed
        THEN the output is in the format "Hello, {input}!"
        """
        assert hello("John") == "Hello, John!"

    
