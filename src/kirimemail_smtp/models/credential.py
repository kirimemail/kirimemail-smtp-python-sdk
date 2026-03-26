"""
Credential model for SMTP credentials.
"""

from pydantic import BaseModel, Field


class Credential(BaseModel):
    """
    SMTP credential model.
    """
    id: int = Field(..., description="Database auto-increment ID (internal use only)")
    user_smtp_guid: str = Field(..., description="Unique credential GUID used for API operations")
    username: str = Field(..., description="SMTP username for authentication. Must be unique within domain")
    domain: str = Field(..., description="Domain name")
    created_at: int = Field(..., description="Unix timestamp when credential was created")
    modified_at: int = Field(..., description="Unix timestamp when credential was last modified")

    class Config:
        """Pydantic configuration."""
        populate_by_name = True
