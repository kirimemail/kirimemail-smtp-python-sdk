"""
Email validation batch result model.
"""

from pydantic import BaseModel, Field

from .email_validation_result import EmailValidationResult


class EmailValidationBatchSummary(BaseModel):
    """
    Batch validation summary.
    """
    total: int = Field(..., description="Total number of emails validated")
    valid: int = Field(..., description="Number of valid emails")
    invalid: int = Field(..., description="Number of invalid emails")
    cached: int = Field(..., description="Number of results served from cache")
    validated: int = Field(..., description="Number of emails freshly validated")

    class Config:
        """Pydantic configuration."""
        populate_by_name = True


class EmailValidationBatchResult(BaseModel):
    """
    Batch email validation results with summary.
    """
    results: list[EmailValidationResult] = Field(..., description="Array of individual validation results")
    summary: EmailValidationBatchSummary = Field(..., description="Summary statistics")

    class Config:
        """Pydantic configuration."""
        populate_by_name = True
