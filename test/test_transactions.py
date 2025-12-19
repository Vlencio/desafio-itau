import pytest
from datetime import datetime, timezone
from controler.controler import app
from services.transactionService import TransactionService

trService = TransactionService()

client = app.test_client()

@pytest.fixture(autouse=True)
def setup_teardown():
    trService.clear_transactions()
    yield
    trService.clear_transactions()

def test_valid_transaction():
    data_atual = datetime.now(timezone.utc).isoformat()

    payload = {
        "valor": 67.67,
        "dataHora": data_atual
    }

    response = client.post('/transacao', json=payload)

    assert response.status_code == 201
    assert response.data == b""

def test_invalid_datetime():
    data = datetime(2026, 1, 1, tzinfo=timezone.utc).isoformat()

    payload = {
        "valor": 67.67,
        "dataHora": data
    }

    response = client.post('/transacao', json=payload)

    assert response.status_code == 422
    assert response.data == b""

def test_invalid_amount():
    data = datetime.now().isoformat()

    payload = {
        "valor": -67.67,
        "dataHora": data
    }

    response = client.post('/transacao', json=payload)

    assert response.status_code == 422
    assert response.data == b""

def test_clear():
    response = client.delete('/transacao')

    assert response.status_code == 200
    assert response.data == b""

