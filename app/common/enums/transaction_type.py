import enum

FinancialTransactionTypeEnum = enum.Enum(
    "FinancialTransactionTypeEnum",
    {
        "CREDIT": "credit",
        "DEBIT": "debit",
    },
)
