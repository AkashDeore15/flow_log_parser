import unittest
import os
from src.file_writer import OutputWriter

class TestOutputWriter(unittest.TestCase):
    def setUp(self):
        self.writer = OutputWriter("tests/output")

    def test_write_files(self):
        tag_counts = {"sv_P1": 2, "email": 3}
        port_protocol_counts = {("25", "tcp"): 2, ("110", "tcp"): 3}
        self.writer.write_tag_counts(tag_counts)
        self.writer.write_port_protocol_counts(port_protocol_counts)
        self.assertTrue(os.path.exists("tests/output/tag_counts.csv"))
        self.assertTrue(os.path.exists("tests/output/port_protocol_counts.csv"))

if __name__ == '__main__':
    unittest.main()