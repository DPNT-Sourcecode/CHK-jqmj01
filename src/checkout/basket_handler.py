from checkout.price_table import price_table
from typing import Tuple


def get_sku_dict(skus: str) -> dict:
    '''Get the total number of each SKU in the basket

    Args:
        skus (string): a string containing the SKUS of all the products in
        the basket (assumed to be a list of the SKUS like "AAABBC" for now)

    Returns:
        dict: a dict containing the quantity of each SKU in the string
    '''

    # convert to list
    sku_list = [sku for sku in skus]

    sku_dict = {}
    for sku in sku_list:
        if sku not in sku_dict:
            sku_dict[sku] = 1
        else:
            sku_dict[sku] = sku_dict[sku] + 1

    return sku_dict


def get_total_price(sku_dict: dict, total_price: int = 0) -> int:
    '''Get the total price of the SKUs in the input dict, after offers have
    been applied

    Args:
        skus (dict): a dict containing the number of each SKU in the basket,
        after offers have been applied

    Returns:
        int: the total price of all the SKUs in the basket
    '''

    for key, value in list(sku_dict.items()):
        if key in price_table["base_prices"]:
            while sku_dict[key] > 0:
                total_price += price_table["base_prices"][key]
                sku_dict[key] = sku_dict[key] - 1
        else:
            return -1

    return total_price


def apply_offers(sku_dict: dict) -> Tuple[dict, int]:
    total_price = 0

    for offer in price_table["offers"]:
        if offer["sku"] in sku_dict:
            original_quantity = sku_dict[offer["sku"]]

            if offer["offer"]["type"] == "freebie":
                while original_quantity >= offer["quantity"]:
                    if offer["offer"]["details"]["sku"] in sku_dict:
                        sku_dict[offer["offer"]["details"]["sku"]] -= (
                            offer["offer"]["details"]["quantity"]
                        )
                    original_quantity -= offer["quantity"]

            if offer["offer"]["type"] == "reduced_price":
                while original_quantity >= offer["quantity"]:
                    sku_dict[offer["sku"]] = (
                        sku_dict[offer["sku"]] -
                        offer["quantity"]
                    )
                    total_price += offer["offer"]["details"]
                    original_quantity -= offer["quantity"]

            if offer["offer"]["type"] == "bogof":
                while (original_quantity >=
                       offer["offer"]["details"]["total_items_needed"]):
                    # check for >= total items needed
                    original_quantity -= (
                        offer["offer"]["details"]["total_items_needed"])
                    # remove bogof deal quanity from
                    sku_dict[offer["offer"]["details"]["sku"]] -= (
                        offer["offer"]["details"]["quantity"]
                    )

            if sku_dict[offer["sku"]] <= 0:
                del sku_dict[offer["sku"]]

    return sku_dict, total_price
