from checkout.basket_handler import get_sku_dict, get_total_price
import pytest

class TestBasketHandler():
    def test_get_sku_dict(self):
        """
        GIVEN the get_sku_dict method
        WHEN two positive numbers between 0 and 100 are passed
        THEN the output is the sum of those two numbers
        """
        assert get_sku_dict("AAABBBCCD") == {
            "A": 3,
            "B": 3,
            "C": 2,
            "D": 1
        }

    def test_get_total_price(self):
        """
        GIVEN the get_total_price method
        WHEN a dict of sku quantities is passed
        THEN the output sum of the basket quantities
        """

        assert get_total_price({
            "A": 1,
            "B": 1,
            "C": 1,
            "D": 1
        }) == 115
    
    def test_get_total_price_special_offer(self):
        """
        GIVEN eligibility of a special offer
        WHEN a dict of sku quantities is passed
        THEN the output sum takes into account the special offer
        """

        assert get_total_price({
            "A": 3,
        }) == 130

    def test_get_total_price_invalid(self):
        """
        GIVEN the get_total_price method
        WHEN an invalid SKU is passed to the method
        THEN the output returns -1
        """

        assert get_total_price({
            "A": 2,
            "B": 3,
            "C": 2,
            "a": 1
        }) == -1
