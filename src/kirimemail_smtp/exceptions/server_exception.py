"""
Exception raised for server errors (5xx).
"""

from typing import Any, Dict, Optional

from .api_exception import ApiException


class ServerException(ApiException):
    """
    Exception raised for server-side errors.

    Typically raised when the API returns 5xx status codes.
    """

    def __init__(
        self,
        message: str = "Server error",
        status_code: Optional[int] = None,
        errors: Optional[Dict[str, Any]] = None,
        response: Optional[Dict[str, Any]] = None
    ) -> None:
        super().__init__(message, status_code or 500, errors, response)
        self.name = "ServerException"
