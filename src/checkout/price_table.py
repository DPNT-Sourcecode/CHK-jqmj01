price_table = {
    "base_prices": {
        "A": 50,
        "B": 30,
        "C": 20,
        "D": 15,
        "E": 40,
        "F": 10,
        "G": 20,
        "H": 10,
        "I": 35,
        "J": 60,
        "K": 70,
        "L": 90,
        "M": 15,
        "N": 40,
        "O": 10,
        "P": 50,
        "Q": 30,
        "R": 50,
        "S": 20,
        "T": 20,
        "U": 40,
        "V": 50,
        "W": 20,
        "X": 17,
        "Y": 20,
        "Z": 21
    },
    "offers": [  # in order of value to the customer
        {
            "offer": {
                "type": "multibuy",
                "details": {
                    "sku": ["Z", "Y", "S", "T", "X"],  # decending price order
                    "quantity": 3
                }
            }
        },
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
            "sku": "N",
            "quantity": 3,
            "offer": {
                "type": "freebie",
                "details": {
                    "sku": "M",
                    "quantity": 1
                }
            }
        },
        {
            "sku": "R",
            "quantity": 3,
            "offer": {
                "type": "freebie",
                "details": {
                    "sku": "Q",
                    "quantity": 1
                }
            }
        },
        {
            "sku": "F",
            "quantity": 2,
            "offer": {
                "type": "bogof",
                "details": {
                    "sku": "F",
                    "quantity": 1,
                    "total_items_needed": 3
                }
            }
        },
        {
            "sku": "U",
            "quantity": 3,
            "offer": {
                "type": "bogof",
                "details": {
                    "sku": "U",
                    "quantity": 1,
                    "total_items_needed": 4
                }
            }
        },
        {
            "sku": "A",
            "quantity": 5,
            "offer": {
                "type": "reduced_price",
                "details": 200
            }
        },
        {
            "sku": "A",
            "quantity": 3,
            "offer": {
                "type": "reduced_price",
                "details": 130
            }
        },
        {
            "sku": "B",
            "quantity": 2,
            "offer": {
                "type": "reduced_price",
                "details": 45
            }
        },
        {
            "sku": "H",
            "quantity": 10,
            "offer": {
                "type": "reduced_price",
                "details": 80
            }
        },
        {
            "sku": "H",
            "quantity": 5,
            "offer": {
                "type": "reduced_price",
                "details": 45
            }
        },
        {
            "sku": "K",
            "quantity": 2,
            "offer": {
                "type": "reduced_price",
                "details": 150
            }
        },
        {
            "sku": "P",
            "quantity": 5,
            "offer": {
                "type": "reduced_price",
                "details": 200
            }
        },
        {
            "sku": "Q",
            "quantity": 3,
            "offer": {
                "type": "reduced_price",
                "details": 80
            }
        },
        {
            "sku": "V",
            "quantity": 3,
            "offer": {
                "type": "reduced_price",
                "details": 130
            }
        },
        {
            "sku": "V",
            "quantity": 2,
            "offer": {
                "type": "reduced_price",
                "details": 90
            }
        },
    ]
}


