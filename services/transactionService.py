import threading
from typing import List, Dict, Any

class TransactionService:
    def __init__(self):
        self._transactions: List[Dict[str, Any]] = []

        self._lock = threading.Lock()
    
    def save_transaction(self, transaction: Dict[str, Any]) -> bool:
        """
        Save a transaction.

        Args:
            transaction: Dictionary[str: Any]
        """

        try:
            with self._lock:
                self._transactions.append(transaction)
                return True
        
        except Exception as e:
            print(e)
            return False
    
    def clear_transactions(self) -> bool:
        """
        Clear all transactions from the memory.
        """
        
        try:
            with self._lock:
                self._transactions.clear()
                return True
        
        except Exception as e:
            print(e)
            return False
