"""
Email Validation API for email address validation.
"""

from typing import Any

from ..client.smtp_client import SmtpClient


class EmailValidationApi:
    """
    API class for email validation.
    """

    def __init__(self, client: SmtpClient) -> None:
        """
        Initialize the Email Validation API.

        Args:
            client: SMTP client instance
        """
        self.client = client

    async def validate_email(
        self,
        email: str,
    ) -> dict[str, Any]:
        """
        Validate a single email address.

        Args:
            email: Email address to validate

        Returns:
            Validation result
        """
        data = {"email": email}
        return await self.client.post("/api/email/validate", data=data)

    async def validate_email_strict(
        self,
        email: str,
    ) -> dict[str, Any]:
        """
        Validate a single email address with strict mode.

        Args:
            email: Email address to validate

        Returns:
            Strict validation result
        """
        data = {"email": email}
        return await self.client.post("/api/email/validate/strict", data=data)

    async def validate_bulk(
        self,
        emails: list[str],
    ) -> dict[str, Any]:
        """
        Validate multiple email addresses.

        Args:
            emails: List of email addresses to validate (max 100)

        Returns:
            Batch validation results

        Raises:
            ValueError: If more than 100 emails are provided
        """
        if len(emails) > 100:
            raise ValueError("Maximum 100 emails allowed per bulk validation request")

        if len(emails) == 0:
            raise ValueError("At least one email is required for bulk validation")

        data = {"emails": emails}
        return await self.client.post("/api/email/validate/bulk", data=data)

    async def validate_bulk_strict(
        self,
        emails: list[str],
    ) -> dict[str, Any]:
        """
        Validate multiple email addresses with strict mode.

        Args:
            emails: List of email addresses to validate (max 100)

        Returns:
            Strict batch validation results

        Raises:
            ValueError: If more than 100 emails are provided
        """
        if len(emails) > 100:
            raise ValueError("Maximum 100 emails allowed per bulk validation request")

        if len(emails) == 0:
            raise ValueError("At least one email is required for bulk validation")

        data = {"emails": emails}
        return await self.client.post("/api/email/validate/bulk/strict", data=data)
