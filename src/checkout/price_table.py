price_table = {
    "base_prices": {
        "A": 50,
        "B": 30,
        "C": 20,
        "D": 15,
        "E": 40
    },
    "offers": [
        {
            "sku": "E",
            "quantity": 2,
            "offer": {
                "type": "freebie",
                "details": {
                    "sku": "B",
                    "quantity": 1
                } 
            }
        },
        {
            "sku": "A",
            "quantity": 5,
            "offer": {
                "type": "reduced_price",
                "offer": 200
            }
        },
        {
            "sku": "A",
            "quantity": 3,
            "offer": {
                "type": "reduced_price",
                "offer": 130
            }
        },
        {
            "sku": "B",
            "quantity": 2,
            "offer": {
                "type": "reduced_price",
                "offer": 45
            }
        },
    ]
}




