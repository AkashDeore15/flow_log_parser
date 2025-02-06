from collections import defaultdict

class FlowLogParser:
    def __init__(self, file_path, lookup_table):
        self.file_path = file_path
        self.lookup_table = lookup_table
        self.protocol_map = {"6": "tcp", "17": "udp", "1": "icmp"}
    
    def parse_logs(self):
        tag_counts = defaultdict(int)
        port_protocol_counts = defaultdict(int)
        
        with open(self.file_path, 'r') as file:
            for line in file:
                parts = line.strip().split()
                if len(parts) < 10:
                    continue  # Skip malformed lines
                
                # Ensure correct extraction of dstport and protocol
                try:
                    dstport = parts[5].strip()
                    protocol_num = parts[6].strip()
                    protocol = self.protocol_map.get(protocol_num, "unknown").lower()
                except IndexError:
                    continue  # Skip if parsing fails
                
                tag = self.lookup_table.get_tag(dstport, protocol)
                tag_counts[tag] += 1
                port_protocol_counts[(dstport, protocol)] += 1
        
        return tag_counts, port_protocol_counts