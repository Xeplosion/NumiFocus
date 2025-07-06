from abc import ABC, abstractmethod
from datetime import date
from typing import Any, Mapping, Optional 

from backend.models.instruments import ACCOUNT_UPLOAD_KEY, NormalizedTransactionSchema

class NormalizedTransactionInstrument(ABC):
    """Abstract base class for normalized financial transaction instruments."""
    
    def __init__(self, data: NormalizedTransactionSchema):
        self.data = data
    
    @abstractmethod
    def sync_transaction_data(self) -> None:
        """Syncs instance specific transaction data with locally stored transaction data."""

    @classmethod
    @abstractmethod
    def load_existing_transaction_data(cls, date_start: Optional[date] = None, date_end: Optional[date] = None) -> 'NormalizedTransactionInstrument':
        """Loads existing locally stored financial instrument transaction data."""

    @classmethod
    @abstractmethod
    def merge_transaction_data(
        cls,
        instance1: 'NormalizedTransactionInstrument',
        instance2: 'NormalizedTransactionInstrument'
    ) -> 'NormalizedTransactionInstrument':
        """Merges transaction data from two instances of the NormalizedTransactionInstrument class"""

    @abstractmethod
    def dedupe(self) -> None:
        """Removes duplicate transaction data."""

    @staticmethod
    @abstractmethod
    def validate(data: Mapping[str, Any]) -> bool:
        """Checks whether or not the normalized transaction data is valid."""


    def delete_from_transaction_id(transaction_id: str) -> None:
        """Deletes transaction data from a transaction ID."""

    def delete_from_file_id(account_upload_tuple: ACCOUNT_UPLOAD_KEY) -> None:
        """Deletes transaction data from an uploaded transaction file."""
