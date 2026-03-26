"""
Data models for Kirim.Email SMTP API.
"""

from .credential import Credential
from .domain import Domain
from .email_validation_batch_result import EmailValidationBatchResult
from .email_validation_result import EmailValidationResult
from .log_entry import LogEntry
from .pagination import Pagination
from .quota import Quota
from .suppression import Suppression
from .webhook import Webhook

__all__ = [
    "Credential",
    "Domain",
    "EmailValidationBatchResult",
    "EmailValidationResult",
    "LogEntry",
    "Pagination",
    "Quota",
    "Suppression",
    "Webhook",
]
