from datetime import date
from typing import Literal, Optional, Tuple, TypedDict

### Google Sheets uploaded instrument data literals ####
ACCOUNT_OWNERS = Literal['Foster', 'Natalia', 'shared']
ACCOUNT_TYPES = Literal['checking', 'credit', 'crypto', 'investing', 'IRA', 'savings']
INSTRUMENT_TYPES = Literal[
    'chase_credit',
    'discover_checking',
    'discover_credit',
    'discover_savings',
    'robinhood_crypto',
    'robinhood_investing',
    'robinhood_IRA',
    'UCCU_checking',
    'UCCU_credit',
    'UCCU_savings',
    'USAA_checking',
    'USAA_credit',
    'USAA_savings'
]
ACCOUNT_UPLOAD_KEY = Tuple[ACCOUNT_OWNERS, ACCOUNT_TYPES, str]

#### All financial instrument transaction data schemas. ####
class TransactionSchema(TypedDict):
    """Abstract base class for financial transaction instruments."""

    pass

class NormalizedTransactionSchema(TransactionSchema):
    """Abstract base class for normalized financial transaction instrument schemas."""
    
    pass

#### Normalized transaction schemas. ####
class CheckingData(NormalizedTransactionSchema):
    """Normalized schema for checking account transactions.

    Includes all core fields expected after processing the raw uploaded data
    from Google Forms or financial exports. This structure is used for internal
    data validation and storage.
    """

    transaction_id: str
    activity_date: date
    account: Literal["foster_checking", "natalia_checking", "shared_checking"]
    credit: Optional[float]
    debit:Optional[float]
    classification: Literal[
        "Households & Services",
        "Food & Drinks",
        "Transport",
        "Shopping",
        "Leisure",
        "Health & Beauty",
        "Other"
    ]
    subclassification: Optional[str]
    old_classification: Optional[str]
    description: str
    old_description: Optional[str]
    posted: bool

class CreditData(NormalizedTransactionSchema):
    """Normalized schema for credit account transactions.

    Includes all core fields expected after processing the raw uploaded data
    from Google Forms or financial exports. This structure is used for internal
    data validation and storage.
    """

    transaction_id: str
    activity_date: date
    account: Literal["foster_credit_chase", "foster_credit_UCCU", "natalia_credit", "shared_credit"]
    credit: Optional[float]
    debit: Optional[float]
    classification: Literal[
        "Households & Services",
        "Food & Drinks",
        "Transport",
        "Shopping",
        "Leisure",
        "Health & Beauty",
        "Other"
    ]
    subclassification: Optional[str]
    old_classification: Optional[str]
    description: str
    old_description: Optional[str]
    posted: bool

class SavingsData(NormalizedTransactionSchema):
    """Normalized schema for savings account transactions.

    Includes all core fields expected after processing the raw uploaded data
    from Google Forms or financial exports. This structure is used for internal
    data validation and storage.
    """

    transaction_id: str
    activity_date: date
    account: Literal["foster_savings", "natalia_savings", "shared_savings"]
    credit: Optional[float]
    debit: Optional[float]
    classification: Literal[
        "Households & Services",
        "Food & Drinks",
        "Transport",
        "Shopping",
        "Leisure",
        "Health & Beauty",
        "Other"]
    subclassification: Optional[str]
    old_classification: Optional[str]
    description: str
    old_description: Optional[str]
    posted: bool

class CryptoData(NormalizedTransactionSchema):
    """Normalized schema for crypto account transactions.

    Includes all core fields expected after processing the raw uploaded data
    from Google Forms or financial exports. This structure is used for internal
    data validation and storage.
    """

    transaction_id: str
    activity_date: date
    account: Literal["foster_crypto", "natalia_crypto"]
    description: Optional[str]
    ticker: str
    credit_quantity: Optional[float]
    debit_quantity: Optional[float]
    price: float
    amount: float
    fee: Optional[float]

class InvestingData(NormalizedTransactionSchema):
    """Normalized schema for investing account transactions.

    Includes all core fields expected after processing the raw uploaded data
    from Google Forms or financial exports. This structure is used for internal
    data validation and storage.
    """

    transaction_id: str
    activity_date: date
    account: Literal["foster_investing", "natalia_investing", "shared_investing"]
    process_date: date
    settle_date: date
    ticker: Optional[str]
    description: str
    trans_code: Literal["ACH", "CDIV", "BUY", "SELL"]
    quantity: Optional[float]
    price: Optional[float]
    credit: Optional[float]
    debit: Optional[float]

class IRAData(NormalizedTransactionSchema):
    """Normalized schema for Roth/Traditional IRA account transactions.

    Includes all core fields expected after processing the raw uploaded data
    from Google Forms or financial exports. This structure is used for internal
    data validation and storage.
    """

    transaction_id: str
    activity_date: date
    account: Literal["foster_rothIRA", "foster_traditionalIRA", "natalia_rothIRA", "natalia_traditionalIRA"]
    process_date: date
    settle_date: date
    ticker: Optional[str]
    description: str
    trans_code: Literal["ACH", "CDIV", "BUY", "SELL"]
    quantity: float
    price: float
    credit: float
    debit: float

#### Instrument specific transaction schemas. ####
# Chase.
class ChaseCredit(TransactionSchema):
    # TODO: complete this once there are transactions on the Prime Visa card.
    pass

# Discover.
class DiscoverChecking(TransactionSchema):
    transaction_date: date
    transaction_description: str
    transaction_type: str
    debit: Optional[float]
    credit: Optional[float]

class DiscoverCredit(TransactionSchema):
    transaction_date: date
    transaction_description: str
    transaction_type: str
    debit: Optional[float]
    credit: Optional[float]

class DiscoverSavings(TransactionSchema):
    transaction_date: date
    transaction_description: str
    transaction_type: str
    debit: Optional[float]
    credit: Optional[float]

# RobinHood.
class RobinHoodCrypto(TransactionSchema):
    date: date
    transaction_type: str
    # Values for debit and credit include ticker information.
    debit: Optional[float]
    credit: Optional[float]
    price: float
    value: float
    fee: Optional[float]

class RobinHoodInvesting(TransactionSchema):
    description: str
    symbol: Optional[str]
    acct_type: Literal["Cash", "Margin"]
    transaction: Literal["AHC", "CDIV", "Buy", "Sell"]
    date: date
    qty: Optional[float]
    price: Optional[float]
    debit: Optional[float]
    credit: Optional[float]

class RobinHoodIRA(TransactionSchema):
    description: str
    symbol: Optional[str]
    acct_type: Literal["Cash", "Margin"]
    transaction: Literal["AHC", "CDIV", "Buy", "Sell"]
    date: date
    qty: Optional[float]
    price: Optional[float]
    debit: Optional[float]
    credit: Optional[float]

# UCCU.
class UCCUChecking(TransactionSchema):
    account_number: int
    post_date: date
    check: str
    description: str
    debit: Optional[float]
    credit: Optional[float]
    status: str
    balance: float
    classification: str

class UCCUCredit(TransactionSchema):
    account_number: int
    post_date: date
    check: str
    description: str
    debit: Optional[float]
    credit: Optional[float]
    status: str
    balance: float
    classification: str

class UCCUSavings(TransactionSchema):
    account_number: int
    post_date: date
    check: str
    description: str
    debit: Optional[float]
    credit: Optional[float]
    status: str
    balance: float
    classification: str

# USAA.
class USAAChecking(TransactionSchema):
    date: date
    description: str
    original_description: Optional[str]
    category: str
    amount: float
    status: str

class USAACredit(TransactionSchema):
    date: date
    description: str
    original_description: Optional[str]
    category: str
    amount: float
    status: str

class USAASavings(TransactionSchema):
    date: date
    description: str
    original_description: Optional[str]
    category: str
    amount: float
    status: str
