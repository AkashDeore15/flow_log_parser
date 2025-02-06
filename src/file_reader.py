import csv

class LookupTable:
    def __init__(self, file_path):
        self.file_path = file_path
        self.lookup_table = self._load_lookup_table()
    
    def _load_lookup_table(self):
        lookup_table = {}
        with open(self.file_path, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                if len(row) == 3:
                    dstport, protocol, tag = row
                    lookup_table[(dstport.strip(), protocol.strip().lower())] = tag.strip()
        return lookup_table
    
    def get_tag(self, dstport, protocol):
        # Ensure case-insensitivity and return appropriate tag
        return self.lookup_table.get((dstport.strip(), protocol.strip().lower()), "Untagged")