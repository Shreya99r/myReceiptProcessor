import math


def calculate_retailer_points(receipt):
    """
    Computes points based on the count of alphanumeric characters in the retailer's name.
    
    Args:
        receipt (dict): Contains the retailer's name under the key 'retailer'.

    Returns:
        int: Number of points based on valid characters in the retailer's name.
    """
    return sum(1 for char in receipt.get("retailer", "") if char.isalnum())


def calculate_purchase_day_points(receipt):
    """
    Awards 6 points if the day of the purchase is odd.
    
    Args:
        receipt (dict): Contains the purchase date under the key 'purchaseDate'.

    Returns:
        int: 6 points if day is odd, otherwise 0.
    """
    try:
        return 6 if int(receipt.get("purchaseDate", "")[-2:]) % 2 != 0 else 0
    except (TypeError, ValueError):
        return 0


def calculate_purchase_time_points(receipt):
    """
    Awards 10 points if the purchase time is between 2:01 PM and 3:59 PM.

    Args:
        receipt (dict): Contains the purchase time under the key 'purchaseTime'.

    Returns:
        int: 10 points if the time is within the range, otherwise 0.
    """
    time_str = receipt.get("purchaseTime", "")
    try:
        hour, minute = map(int, time_str.split(':'))
        if (hour == 14 and minute > 0) or (15 <= hour < 16):
            return 10
        return 0
    except ValueError:
        return 0


def calculate_total_multiples_points(receipt):
    """
    Awards 25 points if the total amount is a multiple of 0.25.

    Args:
        receipt (dict): Contains the total amount under the key 'total'.

    Returns:
        int: 25 points if the total is a multiple of 0.25, otherwise 0.
    """
    try:
        return 25 if float(receipt.get("total", 0)) % 0.25 == 0 else 0
    except ValueError:
        return 0


def calculate_round_dollar_points(receipt):
    """
    Awards 50 points if the total amount is a round dollar (without cents).

    Args:
        receipt (dict): Contains the total amount under the key 'total'.

    Returns:
        int: 50 points if the amount has no cents, otherwise 0.
    """
    try:
        return 50 if float(receipt.get("total", 0)) % 1 == 0 else 0
    except ValueError:
        return 0


def calculate_item_pair_points(receipt):
    """
    Awards 5 points for every pair of items on the receipt.

    Args:
        receipt (dict): Contains a list of items under the key 'items'.

    Returns:
        int: Points based on the number of item pairs.
    """
    return (len(receipt.get("items", [])) // 2) * 5


def calculate_description_points(receipt):
    """
    Awards points based on item descriptions. If the length of an item's description (trimmed) is a multiple of 3,
    20% of the item's price (rounded up) is awarded.

    Args:
        receipt (dict): Contains a list of items under the key 'items' with 'shortDescription' and 'price'.

    Returns:
        int: Points accumulated from item descriptions.
    """
    points = 0
    for item in receipt.get("items", []):
        description = item.get("shortDescription", "").strip()
        try:
            if len(description) % 3 == 0 and description:
                points += math.ceil(float(item.get("price", 0)) * 0.2)
        except ValueError:
            continue
    return points


def calculate_total_points(receipt):
    """
    Aggregates total points from all defined rules for the given receipt.

    Args:
        receipt (dict): The receipt data with various keys.

    Returns:
        int: Cumulative points awarded.
    """
    calculations = [
        calculate_retailer_points,
        calculate_purchase_day_points,
        calculate_purchase_time_points,
        calculate_total_multiples_points,
        calculate_round_dollar_points,
        calculate_item_pair_points,
        calculate_description_points
    ]
    return sum(calc(receipt) for calc in calculations)