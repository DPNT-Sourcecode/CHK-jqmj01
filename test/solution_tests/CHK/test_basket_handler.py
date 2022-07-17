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
        }) == 240

    def test_get_total_price_exception(self):
        """
        GIVEN the get_total_price method
        WHEN a dict of sku quantities is passed
        THEN the output sum of the basket quantities
        """

        with pytest.raises(ValueError) as e:
            res = get_total_price({
                "a": 1
            })

        assert "Error: SKU not in price table" in str(e)