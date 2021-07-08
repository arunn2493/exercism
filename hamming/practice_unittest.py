import unittest
from hamming import distance


class HammingTest(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(distance("", ""), 0)

    def test_strings_with_unequal_lengths(self):
        with self.assertRaisesWithMessage(ValueError):
            distance("AAA", "AB")

    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")


if __name__ == "__main__":
    unittest.main()
