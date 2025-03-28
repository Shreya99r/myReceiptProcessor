import unittest

from utils import (
    calculate_retailer_points,
    calculate_purchase_day_points,
    calculate_purchase_time_points,
    calculate_total_multiples_points,
    calculate_round_dollar_points,
    calculate_item_pair_points,
    calculate_description_points,
    calculate_total_points
)


class TestUtils(unittest.TestCase):
    def setUp(self):
        self.receipt_sample = {
            "retailer": "Target",
            "purchaseDate": "2022-01-01",
            "purchaseTime": "13:01",
            "items": [
                {"shortDescription": "Mountain Dew 12PK", "price": "6.49"},
                {"shortDescription": "Emils Cheese Pizza", "price": "12.25"},
                {"shortDescription": "Knorr Creamy Chicken", "price": "1.26"},
                {"shortDescription": "Doritos Nacho Cheese", "price": "3.35"},
                {"shortDescription": "Klarbrunn 12-PK 12 FL OZ", "price": "12.00"}
            ],
            "total": "35.35"
        }

    def test_calculate_retailer_points(self):
        result = calculate_retailer_points(self.receipt_sample)
        self.assertEqual(result, 6, "Should give 6 points for 'Target'")

    def test_calculate_purchase_day_points(self):
        result = calculate_purchase_day_points(self.receipt_sample)
        self.assertEqual(result, 6, "Should give 6 points for an odd purchase day")

    def test_calculate_purchase_time_points(self):
        result = calculate_purchase_time_points(self.receipt_sample)
        self.assertEqual(result, 0, "Should give 0 points; purchase time not in 2:00pm-4:00pm range")

    def test_calculate_total_multiples_points(self):
        result = calculate_total_multiples_points(self.receipt_sample)
        self.assertEqual(result, 0, "Should give 0 points; total is not a multiple of 0.25")

    def test_calculate_round_dollar_points(self):
        self.receipt_sample["total"] = "36.00"
        result = calculate_round_dollar_points(self.receipt_sample)
        self.assertEqual(result, 50, "Should give 50 points; total is a round dollar amount")

    def test_calculate_item_pair_points(self):
        result = calculate_item_pair_points(self.receipt_sample)
        self.assertEqual(result, 10, "Should give 10 points for 2 pairs of items")

    def test_calculate_description_points(self):
        result = calculate_description_points(self.receipt_sample)
        self.assertEqual(result, 6, "Should give 6 points for one item with a description length divisible by 3")

    def test_calculate_total_points(self):
        result = calculate_total_points(self.receipt_sample)
        self.assertEqual(result, 28, "Should give a total of 28 points based on all criteria")


if __name__ == "__main__":
    unittest.main()