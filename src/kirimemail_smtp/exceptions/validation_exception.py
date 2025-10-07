"""
Exception raised for validation errors (400, 422).
"""

from typing import Any, Dict, Optional

from .api_exception import ApiException


class ValidationException(ApiException):
    """
    Exception raised for validation errors.

    Typically raised when the API returns 400 (Bad Request) or 422 (Unprocessable Entity).
    Contains detailed field-specific validation errors.
    """

    def __init__(
        self,
        message: str = "Validation failed",
        status_code: Optional[int] = None,
        errors: Optional[Dict[str, Any]] = None,
        response: Optional[Dict[str, Any]] = None
    ) -> None:
        super().__init__(message, status_code or 400, errors, response)
        self.name = "ValidationException"
