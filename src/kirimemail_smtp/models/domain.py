"""
Domain model for domain management.
"""

from typing import Optional

from pydantic import BaseModel, Field


class Domain(BaseModel):
    """
    Domain model for domain management.
    """
    id: int = Field(..., description="Unique identifier for domain")
    domain: str = Field(..., description="Domain name used for sending emails")
    tracklink_domain: Optional[str] = Field("", description="Custom tracking domain for click and open tracking")
    tracklink_domain_is_verified: bool = Field(False, description="Whether tracking domain has been verified")
    auth_domain_is_verified: bool = Field(False, description="Whether authentication domain has been verified")
    dns_selector: Optional[str] = Field(None, description="DKIM selector used for DNS verification")
    dns_record: Optional[str] = Field(None, description="DKIM public key record that should be configured in DNS")
    click_track: bool = Field(False, description="Whether click tracking is enabled for emails sent from this domain")
    open_track: bool = Field(False, description="Whether open tracking is enabled for emails sent from this domain")
    unsub_track: bool = Field(False, description="Whether unsubscribe tracking is enabled for emails sent from this domain")
    is_verified: bool = Field(False, description="Whether domain has been verified for email sending")
    status: bool = Field(True, description="Domain status (active/inactive)")
    spf_record: Optional[str] = Field(None, description="Expected SPF record value that should be configured in DNS")
    created_at: int = Field(..., description="Unix timestamp when domain was created")
    modified_at: int = Field(..., description="Unix timestamp when domain was last modified")
    dkim_key_length: Optional[int] = Field(None, description="DKIM key length")

    class Config:
        """Pydantic configuration."""
        populate_by_name = True
