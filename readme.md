# Flow Log Parser

## Overview
This project is a **Flow Log Parser** that processes AWS VPC Flow Logs and maps each row to a tag based on a provided lookup table. The lookup table is defined in a CSV file, and it associates **destination ports and protocols** with specific tags. The program processes flow logs dynamically, extracts relevant information, and generates reports.

## Features
✅ Supports **default AWS VPC Flow Log format (version 2)**  
✅ Maps **destination ports and protocols** to predefined tags  
✅ **Handles large datasets** efficiently (flow log files up to **10MB**, lookup table up to **10,000 entries**)  
✅ Generates **two output reports**:
   - **Tag Counts** (`tag_counts.csv`): Number of occurrences of each tag.
   - **Port/Protocol Combination Counts** (`port_protocol_counts.csv`): Number of times each port/protocol appears.

---

## Assumptions & Limitations

### ✅ Assumptions
1. **Only AWS VPC Flow Logs (Version 2) are supported.** Custom formats are **not** handled.
2. The **flow log format must follow AWS standards** (`version account-id eni srcaddr dstaddr srcport dstport protocol packets bytes start end action log-status`).
3. **Protocol numbers are mapped to their standard names**:
   - `6 → tcp`
   - `17 → udp`
   - `1 → icmp`
4. **Unmatched entries** (ports/protocols not in the lookup table) are tagged as **"Untagged"**.
5. The program assumes **well-formed CSV files** for lookup tables (i.e., no missing values or extra columns).
6. The **output directory is specified by the user** (defaults to `output/`).

### ❌ Limitations
1. **No support for AWS VPC Flow Log Version 1 or custom log formats.**
2. **The script does not modify input logs.** It only extracts information from them.
3. **Duplicate entries in the lookup table** may cause unexpected behavior.
4. **Performance considerations:** Large input files are processed **line-by-line** for memory efficiency, but performance may be affected by extremely large files.

---

## Installation & Usage

### ✅ Prerequisites
- **Python 3.x** installed on your machine
- Required libraries (pre-installed in most environments):
  ```bash
  pip install argparse csv
  ```

### ✅ Running the Program
To execute the Flow Log Parser, use the following command:
```bash
python flow_log_parser.py flow_log.txt lookup_table.csv --output_dir output/
```
Where:
- `flow_log.txt` = Input AWS flow log file
- `lookup_table.csv` = CSV file mapping `dstport,protocol` to `tag`
- `--output_dir output/` = (Optional) Output directory (default is `output/`)

### ✅ Example
```bash
python flow_log_parser.py sample_flow_log.txt sample_lookup_table.csv --output_dir output/
```
**Expected Output Files:**
- `output/tag_counts.csv` → Count of matches for each tag
- `output/port_protocol_counts.csv` → Count of matches for each port/protocol combination

---

## Testing

### ✅ Unit Tests
This repository includes **unit tests** to validate:
- **Flow log parsing correctness**
- **Lookup table mapping accuracy**
- **Output file generation integrity**

To run tests:
```bash
python -m unittest discover tests/
```

### ✅ Manual Testing
1. **Small dataset test** → Verified correct tagging and counting with a small set of logs.
2. **Large dataset test** → Successfully processed logs up to 10MB with 10,000+ lookup entries.
3. **Edge cases handled:**
   - Missing columns in logs (ignored)
   - Ports/protocols not in lookup table (tagged as **"Untagged"**)
   - Unexpected log lines (skipped gracefully)

---

## Analysis & Performance
✅ **Optimized for large files** → The program **processes logs line-by-line** to reduce memory usage.  
✅ **Sorting applied** → Output files are sorted **by tags and port numbers** for easy analysis.  
✅ **Minimal dependencies** → Uses only built-in Python libraries, making it easy to run without additional installations.

---

## Future Improvements
🚀 **Enhancements that can be added:**
1. **Support for AWS Flow Log Version 1**
2. **Support for custom log formats** (user-defined column mappings)
3. **Parallel processing** for faster handling of massive datasets
4. **Configurable logging system** for debugging & monitoring

---

## Contributors
👨‍💻 **Akash Deore** - [GitHub](https://github.com/AkashDeore15)

For any issues or contributions, feel free to create a **GitHub Issue or Pull Request**! 🚀

