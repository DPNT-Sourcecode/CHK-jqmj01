from price_table import price_table

def get_sku_dict(skus: str) -> int:
    '''Get the total number of each SKU in the basket
    
    Args: 
        skus (string): a string containing the SKUS of all the products in the basket 
        (assumed to be a list of the SKUS like "AAABBC" for now)

    Returns: 
        int: the total checkout value of the items
    '''

    # convert to list
    sku_list = skus.split("")

    # count total of each sku in basket
    sku_dict = {}
    for sku in sku_list:
        if sku not in sku_dict:
            sku_dict[sku] = 1
        else:
            sku_dict[sku] = sku_dict[sku] + 1

    return sku_dict
    

    
