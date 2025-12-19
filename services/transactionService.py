import threading
from typing import List, Dict, Any
from datetime import datetime, timedelta, timezone

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
        self._free_memory()

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

    def _free_memory(self):
        now = datetime.now(timezone.utc)
        limit = now - timedelta(seconds=60)

        with self._lock:
            self._transactions = [
                t for t in self._transactions
                if datetime.fromisoformat(t['dataHora']) > limit
            ]
    
    def get_statistics(self) -> Dict[str, Any]:
        """
        Return the count, sum, avg, min, max of all the transactions that ocurred within the last 60 seconds.
        """
        
        self._free_memory()

        if len(self._transactions) <= 0:
            statistics = {
                "count": 0,
                "sum": 0.0,
                "avg": 0.0,
                "min": 0.0,
                "max": 0.0
            }
        
        else:
            #import ipdb; ipdb.set_trace()
            items = [item['valor'] for item in self._transactions]
            total = len(items)
            summ = sum(items)

            statistics = {
                "count": total,
                "sum": summ,
                "avg": summ / total,
                "min": min(items),
                "max": max(items)
            }
        
        return statistics