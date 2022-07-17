from checkout.basket_handler import get_sku_dict, get_total_price
from checkout.price_table import price_table

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    '''Get the total price from a list of SKUs
    
    Args: 
        skus (string): the skus in the basket 

    Returns: 
        int: the total price of all the skus
    '''


    skus_dict = get_sku_dict(skus)
    total_price = get_total_price(skus_dict)
    return total_price
