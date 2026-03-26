"""
Pagination model for API responses.
"""

from typing import Optional

from pydantic import BaseModel, Field


class Pagination(BaseModel):
    """
    Pagination metadata for API responses.
    """
    total: int = Field(..., description="Total number of items available across all pages")
    page: int = Field(..., description="Current page number (1-based)")
    limit: int = Field(..., description="Maximum number of items per page")
    offset: int = Field(..., description="Number of items skipped from beginning (0-based)")

    @property
    def has_next(self) -> bool:
        """Check if there's a next page."""
        return (self.offset + self.limit) < self.total

    @property
    def has_previous(self) -> bool:
        """Check if there's a previous page."""
        return self.offset > 0

    @property
    def next_offset(self) -> Optional[int]:
        """Get the next offset value."""
        return self.offset + self.limit if self.has_next else None

    @property
    def previous_offset(self) -> Optional[int]:
        """Get the previous offset value."""
        return self.offset - self.limit if self.has_previous else None

    class Config:
        """Pydantic configuration."""
        populate_by_name = True
