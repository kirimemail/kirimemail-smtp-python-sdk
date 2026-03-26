"""
Quota model for user quota information.
"""

from pydantic import BaseModel, Field


class Quota(BaseModel):
    """
    User quota information.
    """
    current_quota: int = Field(..., description="Current available quota (aggregate + update)")
    max_quota: int = Field(..., description="Maximum allowed quota (aggregate limit)")
    usage_percentage: float = Field(..., description="Percentage of quota used ((max - current) / max * 100)", ge=0, le=100)

    @property
    def remaining(self) -> int:
        """Get remaining available quota (same as current_quota)."""
        return self.current_quota

    @property
    def usage(self) -> int:
        """Calculate used quota."""
        return self.max_quota - self.current_quota

    class Config:
        """Pydantic configuration."""
        populate_by_name = True
