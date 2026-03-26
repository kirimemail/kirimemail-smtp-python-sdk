"""
Webhook model for email event notifications.
"""

from typing import Optional

from pydantic import BaseModel, Field


class Webhook(BaseModel):
    """
    Webhook configuration for email event notifications.
    """
    webhook_guid: str = Field(..., description="Unique identifier for webhook")
    user_guid: str = Field(..., description="GUID of user who owns webhook")
    user_domain_guid: str = Field(..., description="GUID of domain associated with webhook")
    user_smtp_guid: Optional[str] = Field(None, description="GUID of SMTP configuration")
    type: str = Field(
        ...,
        description="Event type that triggers webhook",
        pattern="^(queued|send|delivered|bounced|failed|permanent_fail|opened|clicked|unsubscribed|temporary_fail|deferred)$"
    )
    url: str = Field(..., description="URL endpoint where webhook events will be sent")
    is_deleted: bool = Field(False, description="Whether webhook has been deleted")
    created_at: int = Field(..., description="Unix timestamp when webhook was created")
    modified_at: int = Field(..., description="Unix timestamp when webhook was last modified")

    class Config:
        """Pydantic configuration."""
        populate_by_name = True
