"""
API classes for Kirim.Email SMTP SDK.
"""

from .credentials import CredentialsApi
from .domains import DomainsApi
from .email_validation import EmailValidationApi
from .logs import LogsApi
from .messages import MessagesApi
from .suppressions import SuppressionsApi
from .user import UserApi
from .webhooks import WebhooksApi

__all__ = [
    "MessagesApi",
    "DomainsApi",
    "CredentialsApi",
    "LogsApi",
    "SuppressionsApi",
    "EmailValidationApi",
    "UserApi",
    "WebhooksApi",
]
