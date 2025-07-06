import os
from datetime import date
from typing import Any, Callable, List, Literal, Mapping, Optional, Tuple, TypedDict

class ProcessTransactionData():
    """
    Contains a list of methods used for retrieving and processing financial instrument transactions data.
    """

    def __init__(self):
        pass

    def fetch_uploaded_transcation_files():
        # TODO: make this grab all transactions files from the NumiFocus Google Sheets document. Returned as a tuple [acount_owner, account_type, file_ID].

        pass

    def process_retrieved_transactions_files(
            self,
            transaction_files: List[Tuple[str, str, str]],
            date_start: Optional[date] = None,
            date_end: Optional[date] = None,
            accounts: Optional[List[str]] = None
        ) -> None:
        """Processes a list of transaction files, optionally filtering by date and account.

        If no filters are provided, only non-duplicate files (as determined by
        self.is_duplicate) will be processed. If any filter is set, only files
        that match the criteria will be processed, regardless of duplication status.
        """
        use_filters = any([date_start, date_end, accounts])        

        for transaction_file in transaction_files:
            # Skip already processed files unless filters are in use.
            if not use_filters and self._is_duplicate(transaction_file):
                continue

            # Extract values from the transaction file tuple.
            account_owner, account_type, file_ID = transaction_file

            # If filters are active, apply them.
            if use_filters:
                file_date_start, file_date_end = self._get_processed_file_date(transaction_file)
                if date_start and file_date_end < date_start:
                    continue
                if date_end and file_date_start < date_end:
                    continue
                if accounts and account_type not in accounts:
                    continue
                
        # Process the file.
        self.process_file(transaction_file)

    def process_file(transaction_file: Tuple[str, str, str]) -> None:
        # TODO: impletment logic for processing a transaction file.
        # First we need to fetch the data using the GoogleDrive API. Based of the instrument we assign the data to a different TypedDict.
        pass

    def normalize_transaction_data(transaction_file: Tuple[str, str, str], )
                 
    def _is_processed(transaction_file: Tuple[str, str, str]) -> bool:
        # TODO: implement logic for determining if transaction file has already been processed or not.
        pass

    def _get_processed_file_date(transaction_file: Tuple[str, str, str]) -> Tuple[date, date]:
        # TODO: implement logic for retrieving a processed files start and end dates.
        pass 

    def _rename_transaction_files():