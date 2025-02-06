import os

class OutputWriter:
    def __init__(self, output_dir):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)
    
    def write_tag_counts(self, tag_counts):
        with open(os.path.join(self.output_dir, "tag_counts.csv"), "w") as file:
            file.write("Tag,Count\n")
            for tag, count in sorted(tag_counts.items()):
                file.write(f"{tag},{count}\n")
    
    def write_port_protocol_counts(self, port_protocol_counts):
        with open(os.path.join(self.output_dir, "port_protocol_counts.csv"), "w") as file:
            file.write("Port,Protocol,Count\n")
            sorted_items = sorted(port_protocol_counts.items(), key=lambda x: int(x[0][0]))
            for (port, protocol), count in sorted_items:
                file.write(f"{port},{protocol},{count}\n")