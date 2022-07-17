from checkout.basket_handler import get_sku_dict, get_total_price
import pytest

class TestBasketHandler():
    def test_get_sku_dict(self):
        """
        GIVEN the get_sku_dict method
        WHEN two positive numbers between 0 and 100 are passed
        THEN the output is the sum of those two numbers
        """
        assert get_sku_dict("AABBBCCD") == {
            "A": 2,
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
            "A": 2,
            "B": 3,
            "C": 2,
            "D": 1
        }) == 245

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
            "-": 1
        }) == -1

    def test_get_sku_dict_lower_case(self):
        """
        GIVEN the get_total_price method
        WHEN a lower case SKU is passed
        THEN the method counts the lower case SKU as if it were upper case
        """

        assert get_sku_dict("AABBbCCD") == {
            "A": 2,
            "B": 3,
            "C": 2,
            "D": 1
        }
