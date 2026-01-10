from http import HTTPStatus


class ForeignKeyNotFoundError(Exception):
    """Exception raised when a foreign key is not found."""

    def __init__(
        self,
        message="Foreign key not found in related table.",
        status_code=HTTPStatus.NOT_FOUND,
    ):
        self.message = message
        self.status_code = status_code


class InsufficientFundsError(Exception):
    """Exception raised when there are insufficient funds for a transaction."""

    def __init__(
        self,
        message="Insufficient funds for the transaction.",
        status_code=HTTPStatus.UNPROCESSABLE_ENTITY,
    ):
        self.message = message
        self.status_code = status_code
