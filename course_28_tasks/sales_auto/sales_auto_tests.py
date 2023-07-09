import unittest

from sales_auto import ShopOLAP

class ShopOLAPTest(unittest.TestCase):

    def test_shop_olap(self):
        # Test case 1
        N = 5
        items = ['item1 10', 'item2 5', 'item1 3', 'item3 8', 'item2 2']
        expected_result = ['item1 13', 'item3 8', 'item2 7']
        self.assertEqual(ShopOLAP(N, items), expected_result)

        # Test case 2
        N = 3
        items = ['item1 5', 'item2 10', 'item3 3']
        expected_result = ['item2 10', 'item1 5', 'item3 3']
        self.assertEqual(ShopOLAP(N, items), expected_result)

        # Test case 3 (edge case)
        N = 0
        items = []
        with self.assertRaises(ValueError):
            ShopOLAP(N, items)

if __name__ == '__main__':
    unittest.main()
