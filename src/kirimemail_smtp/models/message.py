"""
Message send response models for email sending endpoints.
"""

from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class MessageRecipient(BaseModel):
    """
    Per-recipient delivery identifier returned when an email is accepted
    for sending. The same GUID is also sent as the X-Message-Guid header
    on each email for delivery tracking and log correlation.
    """

    to: str = Field(..., description="Recipient email address")
    message_guid: str = Field(..., description="Unique GUID for the queued message")

    class Config:
        """Pydantic configuration."""
        populate_by_name = True


class SendMessageResponse(BaseModel):
    """
    Response for sending a transactional email.
    """

    success: bool = Field(..., description="Request processing success status")
    message: Optional[str] = Field(
        default=None,
        description="Detailed success message including recipient count, "
        "job batching information, and attachment count",
    )
    messages: Optional[List[MessageRecipient]] = Field(
        default=None,
        description="Per-recipient message GUIDs, also sent as the "
        "X-Message-Guid header on each email for delivery tracking "
        "and log correlation",
    )
    data: Optional[Dict[str, Any]] = Field(default=None, description="Additional response data")

    class Config:
        """Pydantic configuration."""
        populate_by_name = True


class SendTemplateMessageResponse(BaseModel):
    """
    Response for sending a template-based email.
    """

    success: bool = Field(..., description="Request processing success status")
    message: Optional[str] = Field(default=None, description="Detailed success message")
    template_guid: Optional[str] = Field(default=None, description="UUID of the template used")
    template_name: Optional[str] = Field(default=None, description="Name of the template used")
    messages: Optional[List[MessageRecipient]] = Field(
        default=None,
        description="Per-recipient message GUIDs, also sent as the "
        "X-Message-Guid header on each email for delivery tracking "
        "and log correlation",
    )
    data: Optional[Dict[str, Any]] = Field(default=None, description="Additional response data")

    class Config:
        """Pydantic configuration."""
        populate_by_name = True
