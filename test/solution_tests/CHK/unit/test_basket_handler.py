from checkout.basket_handler import get_sku_dict, get_total_price, apply_offers
import pytest
from mock import patch

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

        sku_dict, total_price = apply_offers({
            "A": 4,
        })

        assert get_total_price(sku_dict, total_price) == 180

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
        WHEN the sku_dict is passed to apply_offer
        THEN the output is the sku_dict minus the freebie(s)
        """

        sku_dict, total_price = apply_offers({
            "B": 3,
            "E": 4
        })

        assert sku_dict == {
            "B": 1,
            "E": 4
        }

    def test_apply_offers_discount(self):
        """
        GIVEN eligibility for a discount offer
        WHEN the sku_dict is passed to apply_offer
        THEN the output is the sku_dict minus the discounted item(s) and the total price
        of the discount(s)
        """

        sku_dict, total_price = apply_offers({
            "A": 6,
            "C": 1
        })

        assert sku_dict == {
            "A": 1,
            "C": 1
        }

        assert total_price == 200

    def test_apply_offers_multiple(self):
        """
        GIVEN eligibility for multiple discount offers
        WHEN the sku_dict is passed to apply_offer
        THEN all discounts are applied in the correct order
        """

        sku_dict, total_price = apply_offers({
            "A": 4,
            "B": 2,
            "E": 2
        })

        assert sku_dict == {
            "A": 1,
            "B": 1,
            "E": 2
        }

        assert total_price == 130

    def test_apply_offers_handle_non_positives(self):
        """
        GIVEN eligibility for an offer
        WHEN a given sku hits <= 0
        THEN that sku is removed from the sku_dict
        """

        sku_dict, total_price = apply_offers({
            "A": 5,
            "B": 1,
            "E": 4
        })

        assert sku_dict == {
            "E": 4
        }

    def test_apply_offers_freebie_not_apply(self):
        """
        GIVEN eligibility for a freebie offer
        WHEN the sku_dict does not contain any of the free skus
        THEN the offer is not applied
        """

        sku_dict, total_price = apply_offers({
            "E": 2
        })

        assert sku_dict == {
            "E": 2
        }

    def test_apply_offers_bogof(self):
        """
        GIVEN eligibility for a bogof offer
        WHEN the sku_dict is passed to apply_offers
        THEN the bogof freebie is removed
        """

        sku_dict, total_price = apply_offers({
            "F": 5,
            "B": 1
        })

        assert sku_dict == {
            "F": 4,
            "B": 1
        }

    def test_apply_offers_bogof_multiple(self):
        sku_dict, total_price = apply_offers({
            "F": 6,
            "B": 1
        })

        assert sku_dict == {
            "F": 4,
            "B": 1
        }
