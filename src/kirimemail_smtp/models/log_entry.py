"""
Log entry model for email logs.
"""

from datetime import datetime
from typing import Any, ClassVar, Optional

from pydantic import BaseModel, Field


class LogEntry(BaseModel):
    """
    Email log entry model.
    """

    SMTP_EVENT_QUEUED: ClassVar[str] = "queued"
    SMTP_EVENT_SEND: ClassVar[str] = "send"
    SMTP_EVENT_DELIVERED: ClassVar[str] = "delivered"
    SMTP_EVENT_BOUNCED: ClassVar[str] = "bounced"
    SMTP_EVENT_FAILED: ClassVar[str] = "failed"
    SMTP_EVENT_PERMANENT_FAIL: ClassVar[str] = "permanent_fail"
    SMTP_EVENT_OPENED: ClassVar[str] = "opened"
    SMTP_EVENT_CLICKED: ClassVar[str] = "clicked"
    SMTP_EVENT_UNSUBSCRIBED: ClassVar[str] = "unsubscribed"
    SMTP_EVENT_TEMP_FAILURE: ClassVar[str] = "temp_fail"
    SMTP_EVENT_DEFERRED: ClassVar[str] = "deferred"

    VALID_EVENT_TYPES: ClassVar[list[str]] = [
        "queued",
        "send",
        "delivered",
        "bounced",
        "failed",
        "permanent_fail",
        "opened",
        "clicked",
        "unsubscribed",
        "temp_fail",
        "deferred",
    ]

    id: Optional[str] = Field(None, description="Log entry ID")
    message_id: Optional[str] = Field(None, description="Message ID")
    domain: Optional[str] = Field(None, description="Domain name")
    sender: Optional[str] = Field(None, description="Sender email address")
    recipient: Optional[str] = Field(None, description="Recipient email address")
    subject: Optional[str] = Field(None, description="Email subject")
    status: Optional[str] = Field(None, description="Email status")
    event_type: Optional[str] = Field(None, description="Event type")
    response_message: Optional[str] = Field(None, description="Response message")
    ip_address: Optional[str] = Field(None, description="IP address")
    user_agent: Optional[str] = Field(None, description="User agent")
    created_at: Optional[datetime] = Field(None, description="Creation timestamp")
    updated_at: Optional[datetime] = Field(None, description="Last update timestamp")
    metadata: Optional[dict[str, Any]] = Field(None, description="Additional metadata")
    tags: Optional[list[str]] = Field(None, description="Tags")

    class Config:
        """Pydantic configuration."""
        populate_by_name = True
