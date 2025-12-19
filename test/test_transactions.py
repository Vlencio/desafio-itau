import pytest
from datetime import datetime, timezone, timedelta
from controler.controler import app, trService
import json
import time


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

def test_statistics():
    response = client.get('/estatistica')
    expected_empty = {
        "count": 0,
        "sum": 0.0,
        "avg": 0.0,
        "min": 0.0,
        "max": 0.0
    }

    assert json.loads(response.get_json()) == expected_empty

    agora = datetime.now(timezone.utc)
    valores = [10.0, 20.0, 30.0]

    for valor in valores:
        client.post('transacao', json={
            'valor': valor,
            'dataHora': agora.isoformat()
        })

    response = client.get('/estatistica')

    assert response.status_code == 200

    stats = json.loads(response.get_json())

    assert stats['count'] == 3
    assert stats['sum'] == 60.0
    assert stats['avg'] == 20.0
    assert stats['min'] == 10.0
    assert stats['max'] == 30

def test_ignore_old_transactions():
    now = datetime.now(timezone.utc)
    old_time = now - timedelta(minutes=7)

    response = client.post('/transacao', json={
        'valor': 67.67,
        'dataHora': old_time.isoformat()
    })

    assert response.status_code == 201

    time.sleep(1)
    client.post('/transacao', json={
        'valor': 67.69,
        'dataHora': now.isoformat()
    })

    assert response.status_code == 201

    response = client.get('/estatistica')
    estatisticas = json.loads(response.get_json())
    assert response.status_code == 200
    assert estatisticas['count'] == 1
    assert estatisticas['sum'] == 67.69