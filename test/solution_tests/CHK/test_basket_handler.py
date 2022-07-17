from checkout.basket_handler import get_sku_dict, get_total_price, apply_offers
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

    def test_apply_offers_freebie(self):
        """
        GIVEN eligibility for a freebie offer
        WHEN the fru_dict is passed to apply_offer
        THEN the output is the fru_dict minus the freebie(s)
        """

        fru_dict, total_price = apply_offers({
            "B": 2,
            "E": 4
        })

        assert fru_dict == {
            "B": 0,
            "E": 4
        }

    def test_apply_offers_discount(self):
        """
        GIVEN eligibility for a discount offer
        WHEN the fru_dict is passed to apply_offer
        THEN the output is the fru_dict minus the discounted item(s) and the total price
        of the discount(s)
        """

        fru_dict, total_price = apply_offers({
            "A": 6,
            "C": 1
        })

        assert fru_dict == {
            "A": 1,
            "C": 1
        }

        assert total_price == 200