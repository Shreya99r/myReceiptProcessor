import re


class ValidationResult:
    def __init__(self, is_valid, message=""):
        self.is_valid = is_valid
        self.message = message


def validate_receipt(receipt):
    """
    Validates the receipt dictionary based on required keys and their data types.

    Args:
        receipt (dict): The receipt data to be validated.

    Returns:
        ValidationResult: Object containing validation status and error message if invalid.
    """
    if not isinstance(receipt, dict):
        return ValidationResult(False, "Invalid receipt format. Expected a dictionary.")

    required_keys = ["retailer", "purchaseDate", "purchaseTime", "total", "items"]

    for key in required_keys:
        if key not in receipt:
            return ValidationResult(False, f"Missing required field: {key}")

    if not isinstance(receipt["retailer"], str) or not receipt["retailer"].strip():
        return ValidationResult(False, "Invalid retailer name.")

    if not is_valid_date(receipt["purchaseDate"]):
        return ValidationResult(False, "Invalid purchase date format. Use YYYY-MM-DD.")

    if not is_valid_time(receipt["purchaseTime"]):
        return ValidationResult(False, "Invalid purchase time format. Use HH:MM (24-hour).")

    if not is_valid_total(receipt["total"]):
        return ValidationResult(False, "Invalid total amount. Ensure it has two decimal places.")

    if not isinstance(receipt["items"], list) or len(receipt["items"]) == 0:
        return ValidationResult(False, "Items should be a non-empty list.")

    if not all(is_valid_item(item) for item in receipt["items"]):
        return ValidationResult(False, "Invalid item details in receipt.")

    return ValidationResult(True)


def is_valid_date(date_str):
    return bool(re.match(r"^\d{4}-\d{2}-\d{2}$", date_str))


def is_valid_time(time_str):
    return bool(re.match(r"^(?:[01]\d|2[0-3]):[0-5]\d$", time_str))


def is_valid_total(total_str):
    return bool(re.match(r"^\d+\.\d{2}$", total_str))


def is_valid_item(item):
    if not isinstance(item, dict):
        return False
    if "shortDescription" not in item or "price" not in item:
        return False
    if not isinstance(item["shortDescription"], str) or not item["shortDescription"].strip():
        return False
    if not isinstance(item["price"], str) or not is_valid_total(item["price"]):
        return False
    return True