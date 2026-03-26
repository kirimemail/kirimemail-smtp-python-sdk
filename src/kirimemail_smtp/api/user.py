"""
User API for user management.
"""

from typing import Any

from ..client.smtp_client import SmtpClient


class UserApi:
    """
    API class for user management.
    """

    def __init__(self, client: SmtpClient) -> None:
        """
        Initialize the User API.

        Args:
            client: SMTP client instance
        """
        self.client = client

    async def get_quota(self) -> dict[str, Any]:
        """
        Get user quota information.

        Returns:
            Quota information including current usage and limits
        """
        return await self.client.get("/api/quota")
