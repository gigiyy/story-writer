from app.aml.upload_csv import validate_csv_records

def test_transaction_amount_positive():
    csv_content = "TRANSACTION_ID,TRANSACTION_AMOUNT\n1,100\n2,50\n3,0\n4,-10"
    result = validate_csv_records(csv_content)
    # Only rows with amount > 0 are accepted
    assert result['accepted'] == 2
    assert result['rejected'] == 2
    assert result['total'] == 4

def test_transaction_id_unique():
    csv_content = "TRANSACTION_ID,TRANSACTION_AMOUNT\n1,100\n1,50\n2,10"
    result = validate_csv_records(csv_content)
    # Only first occurrence of each TRANSACTION_ID is accepted
    assert result['accepted'] == 1
    assert result['rejected'] == 2
    assert result['total'] == 3

def test_both_rules():
    csv_content = "TRANSACTION_ID,TRANSACTION_AMOUNT\n1,100\n1,-5\n2,0\n3,10"
    result = validate_csv_records(csv_content)
    # Only first row and last row are accepted
    assert result['accepted'] == 1
    assert result['rejected'] == 3
    assert result['total'] == 4
