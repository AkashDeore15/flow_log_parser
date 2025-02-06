import unittest
from src.log_parser import FlowLogParser
from src.file_reader import LookupTable

class TestFlowLogParser(unittest.TestCase):
    def setUp(self):
        self.lookup_table = LookupTable("tests/test_lookup.csv")
        self.parser = FlowLogParser("tests/test_flow_log.txt", self.lookup_table)

    def test_parse_logs(self):
        tag_counts, port_protocol_counts = self.parser.parse_logs()
        self.assertGreater(len(tag_counts), 0)
        self.assertGreater(len(port_protocol_counts), 0)
  
    def test_specific_protocol_mapping(self):
        tag_counts, _ = self.parser.parse_logs()
        # Test protocol number mapping
        self.assertEqual(self.parser.protocol_map["6"], "tcp")
        self.assertEqual(self.parser.protocol_map["17"], "udp")
        self.assertEqual(self.parser.protocol_map["1"], "icmp")

    def test_malformed_line_handling(self):
        # Create test file with malformed line
        with open("tests/malformed_test.txt", "w") as f:
            f.write("invalid line\n")
        parser = FlowLogParser("tests/malformed_test.txt", self.lookup_table)
        tag_counts, port_counts = parser.parse_logs()
        self.assertEqual(len(tag_counts), 0)

if __name__ == '__main__':
    unittest.main()