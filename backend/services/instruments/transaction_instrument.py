from typing import Callable, Literal, Mapping, Optional, Tuple

from normalized_transaction_instrument import NormalizedTransactionInstrument
from backend.models.instruments import ACCOUNT_UPLOAD_KEY, NormalizedTransactionSchema, TransactionSchema

TRANSFORM_FUNC = Callable[[TransactionSchema], NormalizedTransactionSchema]

class TransactionInstrument:
    """Represents a financial transaction instrument with customizable data normalization."""
    
    @staticmethod
    def normalize(
        data: TransactionSchema,
        transform_func: TRANSFORM_FUNC,
    ) -> NormalizedTransactionSchema:
        """
        Normalizes transaction data into a standard format by applying a transform function,
        followed optionally by a post-processing step.

        Args:
            data: Raw transaction data as defined by a concrete implementation of TransactionSchema.
            transform_func: Function to convert raw data to normalized structure.

        Returns:
            NormalizedTransactionSchema: The normalized transaction data.
        """
        return transform_func(data)
