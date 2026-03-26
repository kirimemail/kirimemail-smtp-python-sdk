"""
Suppression model for email suppressions.
"""

from typing import Optional

from pydantic import BaseModel, Field


class Suppression(BaseModel):
    """
    Email suppression model.
    """
    id: int = Field(..., description="Suppression ID")
    type: str = Field(..., description="Suppression type (unsubscribe, bounce, whitelist)", pattern="^(unsubscribe|bounce|whitelist)$")
    recipient_type: str = Field(..., description="Type of recipient (email or domain)", pattern="^(email|domain)$")
    recipient: str = Field(..., description="Email or domain that is suppressed")
    tags: Optional[str] = Field(None, description="Tags for the suppression")
    description: Optional[str] = Field(None, description="Optional description")
    source: Optional[str] = Field(None, description="Source of suppression")
    created_at: int = Field(..., description="Unix timestamp when suppression was created")

    class Config:
        """Pydantic configuration."""
        populate_by_name = True
