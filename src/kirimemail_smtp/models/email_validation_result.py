"""
Email validation result model.
"""

from typing import Optional

from pydantic import BaseModel, Field


class EmailValidationResult(BaseModel):
    """
    Email validation result with comprehensive checks.
    """
    email: str = Field(..., description="The validated email address")
    is_valid: bool = Field(..., description="Whether email passed all validation checks")
    error: Optional[str] = Field(None, description="Error message if validation failed", nullable=True)
    warnings: list[str] = Field(default_factory=list, description="Array of validation warnings")
    cached: bool = Field(..., description="Whether result was served from cache")
    validated_at: str = Field(..., description="ISO timestamp of validation")
    is_spamtrap: bool = Field(..., description="Whether email is identified as likely spamtrap")
    spamtrap_score: Optional[float] = Field(None, description="Spamtrap probability score (0.0-1.0)", ge=0, le=1)

    class Config:
        """Pydantic configuration."""
        populate_by_name = True
