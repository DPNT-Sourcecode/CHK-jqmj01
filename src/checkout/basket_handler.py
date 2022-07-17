from checkout.price_table import price_table


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

    # check for invalid skus
    for sku in sku_list:
        if sku not in price_table:
            raise ValueError("Error: SKU not in price table")

    # count total of each sku in basket
    sku_dict = {}
    for sku in sku_list:
        if sku not in sku_dict:
            sku_dict[sku] = 1
        else:
            sku_dict[sku] = sku_dict[sku] + 1

    return sku_dict


def get_total_price(sku_dict: dict) -> int:
    '''Get the total price of the SKUS in the input dict

    Args:
        skus (dict): a dict containing the number of each SKU in the basket

    Returns:
        int: the total price of all the SKUs in the basket
    '''

    total_price = 0

    for key, value in list(sku_dict.items()):
        while sku_dict[key] > 0:
            if ("special offer" in price_table[key] and
               sku_dict[key] > price_table[key]["special_offer"]["quantity"]):
                # if special offer exists and quantity exceeds required
                total_price += price_table[key]["special_offer"]["price"]
                sku_dict[key] = (sku_dict[key] -
                                 price_table[key]["special_offer"]["quantity"])
            else:
                total_price += price_table[key]["price"]
                sku_dict[key] = sku_dict[key] - 1

    return total_price



