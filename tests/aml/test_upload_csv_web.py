import io
import pytest
from app import create_app

def test_upload_csv_web(client):
    data = {
        'file': (io.BytesIO(b'id,name\n1,Alice\n2,Bob'), 'test.csv')
    }
    response = client.post('/aml/upload_csv', data=data, content_type='multipart/form-data')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['accepted'] == 2
    assert json_data['rejected'] == 0
    assert json_data['total'] == 2

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client
