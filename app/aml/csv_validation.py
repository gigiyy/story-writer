
import csv
from typing import Dict
from app.aml.validation_rules import rule_transaction_amount_positive, rule_transaction_id_unique

def validate_csv_records(csv_content: str) -> Dict[str, int]:
    accepted = 0
    rejected = 0
    total = 0
    rows = []
    id_counts = {}
    try:
        lines = csv_content.splitlines()
        reader = csv.DictReader(lines)
        # Check for valid header (at least two columns)
        if not reader.fieldnames or len(reader.fieldnames) < 2:
            return {'accepted': 0, 'rejected': 0, 'total': 0}
        # First pass: collect rows and count IDs
        for row in reader:
            total += 1
            rows.append(row)
            rule_transaction_id_unique(row, id_counts)
        # Second pass: apply rules
        for row in rows:
            # All fields must be non-empty
            if not all(row.values()) or set(row.keys()) != set(reader.fieldnames):
                rejected += 1
                continue
            # Rule: TRANSACTION_AMOUNT must be > 0
            if not rule_transaction_amount_positive(row):
                rejected += 1
                continue
            # Rule: TRANSACTION_ID must be unique (all rows with duplicate IDs are rejected)
            txn_id = row.get('TRANSACTION_ID')
            if id_counts.get(txn_id, 0) > 1:
                rejected += 1
                continue
            accepted += 1
    except Exception:
        # Malformed file or parsing error
        return {'accepted': 0, 'rejected': 0, 'total': 0}
    return {'accepted': accepted, 'rejected': rejected, 'total': total}
