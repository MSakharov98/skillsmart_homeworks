from selection_and_bubble import SelectionSortStep, BubbleSortStep
from unittest import TestCase


class SimpleSortTest(TestCase):

    def test_sort1(self):
        a = [4, 3, 1, 2]
        SelectionSortStep(a, 0)
        self.assertEqual([1, 3, 4, 2], a)

        SelectionSortStep(a, 1)
        self.assertEqual([1, 2, 4, 3], a)

    def test_sort2(self):
        b = [4, 3, 1, 2]
        self.assertFalse(BubbleSortStep(b))
        self.assertFalse(BubbleSortStep(b))
        self.assertTrue(BubbleSortStep(b))
        self.assertTrue(BubbleSortStep(b))
