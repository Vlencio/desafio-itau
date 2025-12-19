from flask import Flask, jsonify, request
from datetime import datetime, timezone, timedelta
from services.transactionService import TransactionService
from typing import Dict, Any

app = Flask(__name__)

trService = TransactionService()

def validate_transaction(transaction: Dict[str, Any]) -> bool:
    """
    Validates the transaction. It must have 'valor' and 'dataHora', and valor cannot be less than 0.

    Args:
        transaction: Dict{str: any}
    """
    valor = transaction.get('valor')
    dataHora = transaction.get('dataHora')

    if not valor or not dataHora or valor < 0:
        return False
    
    now = datetime.now(timezone.utc)
    dataObj = datetime.fromisoformat(dataHora)
    dif = now - dataObj

    if dif < timedelta(0):
        return False
    
    return True

@app.route('/transacao', methods=['POST'])
def post_transactions():
    data = request.get_json()

    if not data:
        return "", 400
    
    validation = validate_transaction(data)

    if not validation:
        return "", 422
    
    try:
        trService.save_transaction(data)
        return "", 201

    except Exception as e:
        print(e)
        return "", 500

@app.route('/transacao', methods=['DELETE'])
def delete_transactions():
    try:
        trService.clear_transactions()
        return "", 200
    
    except Exception as e:
        print(e)
        return "", 500

if __name__ == '__main__':
    app.run()