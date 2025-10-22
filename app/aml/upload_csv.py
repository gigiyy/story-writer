import csv
from typing import Dict

def validate_csv_records(csv_content: str) -> Dict[str, int]:
    accepted = 0
    rejected = 0
    total = 0
    try:
        lines = csv_content.splitlines()
        reader = csv.DictReader(lines)
        # Check for valid header (at least two columns)
        if not reader.fieldnames or len(reader.fieldnames) < 2:
            return {'accepted': 0, 'rejected': 0, 'total': 0}
        for row in reader:
            total += 1
            # Example rule: all fields must be non-empty
            if all(row.values()) and set(row.keys()) == set(reader.fieldnames):
                accepted += 1
            else:
                rejected += 1
    except Exception:
        # Malformed file or parsing error
        return {'accepted': 0, 'rejected': 0, 'total': 0}
    return {'accepted': accepted, 'rejected': rejected, 'total': total}
