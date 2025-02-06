import unittest
from src.file_reader import LookupTable

class TestLookupTable(unittest.TestCase):
    def setUp(self):
        self.lookup_table = LookupTable("tests/test_lookup.csv")

    def test_get_tag(self):
        self.assertEqual(self.lookup_table.get_tag("25", "tcp"), "sv_P1")
        self.assertEqual(self.lookup_table.get_tag("9999", "tcp"), "Untagged")

if __name__ == '__main__':
    unittest.main()