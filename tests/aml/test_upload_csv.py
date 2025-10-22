import pytest
from app.aml.upload_csv import validate_csv_records

class DummyFile:
    def __init__(self, content):
        self.content = content
    def read(self):
        return self.content

def test_all_rows_accepted():
    csv_content = "id,name\n1,Alice\n2,Bob"
    result = validate_csv_records(csv_content)
    assert result['accepted'] == 2
    assert result['rejected'] == 0
    assert result['total'] == 2

def test_some_rows_rejected():
    csv_content = "id,name\n1,Alice\n,"
    result = validate_csv_records(csv_content)
    assert result['accepted'] == 1
    assert result['rejected'] == 1
    assert result['total'] == 2

def test_empty_file():
    csv_content = ""
    result = validate_csv_records(csv_content)
    assert result['accepted'] == 0
    assert result['rejected'] == 0
    assert result['total'] == 0

def test_malformed_file():
    csv_content = "id|name\n1"
    result = validate_csv_records(csv_content)
    assert result['accepted'] == 0
    assert result['rejected'] == 0
    assert result['total'] == 0
