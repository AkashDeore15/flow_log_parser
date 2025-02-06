import argparse
from file_reader import LookupTable
from log_parser import FlowLogParser
from file_writer import OutputWriter

class FlowLogProcessor:
    def __init__(self, flow_file, lookup_file, output_dir="output"):
        self.lookup_table = LookupTable(lookup_file)
        self.parser = FlowLogParser(flow_file, self.lookup_table)
        self.writer = OutputWriter(output_dir)
    
    def process(self):
        tag_counts, port_protocol_counts = self.parser.parse_logs()
        self.writer.write_tag_counts(tag_counts)
        self.writer.write_port_protocol_counts(port_protocol_counts)
        print("Processing complete. Output saved in", self.writer.output_dir)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Flow Log Parser")
    parser.add_argument("flow_file", help="Path to flow log file")
    parser.add_argument("lookup_file", help="Path to lookup table CSV file")
    parser.add_argument("--output_dir", default="output", help="Directory to save output files")
    args = parser.parse_args()
    
    processor = FlowLogProcessor(args.flow_file, args.lookup_file, args.output_dir)
    processor.process()