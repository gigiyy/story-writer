import io
import pytest
from app import create_app

def test_upload_csv_web(client):
    # Test valid upload
    data = {
        'file': (io.BytesIO(b'TRANSACTION_ID,TRANSACTION_AMOUNT\n1,100\n2,50'), 'test.csv')
    }
    response = client.post('/aml/upload_csv', data=data, content_type='multipart/form-data', headers={'Accept': 'application/json'})
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['accepted'] == 2
    assert json_data['rejected'] == 0
    assert json_data['total'] == 2

    # Test duplicate IDs (all rows with duplicate ID rejected)
    data = {
        'file': (io.BytesIO(b'TRANSACTION_ID,TRANSACTION_AMOUNT\n1,100\n1,50\n2,10'), 'test.csv')
    }
    response = client.post('/aml/upload_csv', data=data, content_type='multipart/form-data', headers={'Accept': 'application/json'})
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['accepted'] == 1
    assert json_data['rejected'] == 2
    assert json_data['total'] == 3

    # Test negative and zero amounts
    data = {
        'file': (io.BytesIO(b'TRANSACTION_ID,TRANSACTION_AMOUNT\n1,0\n2,-5\n3,10'), 'test.csv')
    }
    response = client.post('/aml/upload_csv', data=data, content_type='multipart/form-data', headers={'Accept': 'application/json'})
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['accepted'] == 1
    assert json_data['rejected'] == 2
    assert json_data['total'] == 3

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client
