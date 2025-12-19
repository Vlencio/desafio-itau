from controler.controler import app
from datetime import datetime, timezone
import random, time

client = app.test_client()

for i in range(3):
    payload = {
        'valor': random.randint(0, 1000),
        'dataHora': datetime.now(timezone.utc).isoformat()
    }
    response = client.post('/transacao', json=payload)
    time.sleep(1)

response = client.get('/estatistica')

print(response.get_json())