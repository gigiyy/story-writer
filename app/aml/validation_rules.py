def rule_transaction_amount_positive(row):
    try:
        amount = float(row.get('TRANSACTION_AMOUNT', ''))
        return amount > 0
    except (ValueError, TypeError):
        return False

def rule_transaction_id_unique(row, id_counts):
    txn_id = row.get('TRANSACTION_ID')
    if not txn_id:
        return False
    id_counts[txn_id] = id_counts.get(txn_id, 0) + 1
    return True
