from price_table import price_table

def get_total_price(skus: str) -> int:
    '''Get the total price from the price table of multiple items
    
    Args: 
        skus (string): a string containing the SKUS of all the products in the basket 
        (assumed to be a list of the SKUS like "AAABBC" for now)

    Returns: 
        int: the total checkout value of the items
    '''

    sku_list = skus.split("")

    # count total of each sku in basket
    sku_dict = {}
    for sku in sku_list:
        if sku not in sku_dict:
            sku_dict[sku] = 1
        else:
            sku_dict[sku] = sku_dict[sku] + 1

    
