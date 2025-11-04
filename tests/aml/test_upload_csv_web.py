import io
import re

import pytest

from app import create_app


def test_upload_csv_web(client):
    # Test valid upload
    data = {
        "file": (
            io.BytesIO(b"TRANSACTION_ID,TRANSACTION_AMOUNT\n1,100\n2,50"),
            "test.csv",
        )
    }
    response = client.post("/aml/upload", data=data, content_type="multipart/form-data")
    assert response.status_code == 200
    html = response.data.decode()

    # Check table headers
    assert "<th>Accepted</th>" in html
    assert "<th>Rejected</th>" in html
    assert "<th>Total</th>" in html
    # Check table row values in order, allowing whitespace
    assert re.search(r"<tr>\s*<td>2</td>\s*<td>0</td>\s*<td>2</td>\s*</tr>", html)

    # Test duplicate IDs (all rows with duplicate ID rejected)
    data = {
        "file": (
            io.BytesIO(b"TRANSACTION_ID,TRANSACTION_AMOUNT\n1,100\n1,50\n2,10"),
            "test.csv",
        )
    }
    response = client.post("/aml/upload", data=data, content_type="multipart/form-data")
    assert response.status_code == 200
    html = response.data.decode()

    assert "<th>Accepted</th>" in html
    assert "<th>Rejected</th>" in html
    assert "<th>Total</th>" in html
    assert re.search(r"<tr>\s*<td>1</td>\s*<td>2</td>\s*<td>3</td>\s*</tr>", html)

    # Test negative and zero amounts
    data = {
        "file": (
            io.BytesIO(b"TRANSACTION_ID,TRANSACTION_AMOUNT\n1,0\n2,-5\n3,10"),
            "test.csv",
        )
    }
    response = client.post("/aml/upload", data=data, content_type="multipart/form-data")
    assert response.status_code == 200
    html = response.data.decode()

    assert "<th>Accepted</th>" in html
    assert "<th>Rejected</th>" in html
    assert "<th>Total</th>" in html
    assert re.search(r"<tr>\s*<td>1</td>\s*<td>2</td>\s*<td>3</td>\s*</tr>", html)


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client
