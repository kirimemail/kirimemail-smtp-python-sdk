"""
Suppressions API for email suppression management.
"""

from typing import Any

from ..client.smtp_client import SmtpClient


class SuppressionsApi:
    """
    API class for email suppression management.
    """

    def __init__(self, client: SmtpClient) -> None:
        """
        Initialize the Suppressions API.

        Args:
            client: SMTP client instance
        """
        self.client = client

    async def get_suppressions(
        self,
        domain: str,
        limit: Optional[int] = None,
        page: Optional[int] = None,
        type: Optional[str] = None,
    ) -> dict[str, Any]:
        """
        Get suppressions for a domain.

        Args:
            domain: Domain name
            limit: Number of suppressions per page
            page: Page number
            type: Suppression type filter (bounce, unsubscribe, whitelist)

        Returns:
            Suppressions with pagination
        """
        params = {}
        if limit is not None:
            params["limit"] = str(limit)
        if page is not None:
            params["page"] = str(page)
        if type is not None:
            params["type"] = type

        return await self.client.get(f"/api/domains/{domain}/suppressions", params=params)

    async def get_unsubscribe_suppressions(
        self,
        domain: str,
        limit: Optional[int] = None,
        page: Optional[int] = None,
    ) -> dict[str, Any]:
        """
        Get unsubscribe suppressions.

        Args:
            domain: Domain name
            limit: Number of suppressions per page
            page: Page number

        Returns:
            Unsubscribe suppressions with pagination
        """
        params = {}
        if limit is not None:
            params["limit"] = str(limit)
        if page is not None:
            params["page"] = str(page)

        return await self.client.get(f"/api/domains/{domain}/suppressions/unsubscribes", params=params)

    async def get_bounce_suppressions(
        self,
        domain: str,
        limit: Optional[int] = None,
        page: Optional[int] = None,
    ) -> dict[str, Any]:
        """
        Get bounce suppressions.

        Args:
            domain: Domain name
            limit: Number of suppressions per page
            page: Page number

        Returns:
            Bounce suppressions with pagination
        """
        params = {}
        if limit is not None:
            params["limit"] = str(limit)
        if page is not None:
            params["page"] = str(page)

        return await self.client.get(f"/api/domains/{domain}/suppressions/bounces", params=params)

    async def get_whitelist_suppressions(
        self,
        domain: str,
        limit: Optional[int] = None,
        page: Optional[int] = None,
    ) -> dict[str, Any]:
        """
        Get whitelist suppressions.

        Args:
            domain: Domain name
            limit: Number of suppressions per page
            page: Page number

        Returns:
            Whitelist suppressions with pagination
        """
        params = {}
        if limit is not None:
            params["limit"] = str(limit)
        if page is not None:
            params["page"] = str(page)

        return await self.client.get(f"/api/domains/{domain}/suppressions/whitelist", params=params)

    async def get_suppressions_by_type(
        self,
        domain: str,
        type: str,
        limit: Optional[int] = None,
        page: Optional[int] = None,
    ) -> dict[str, Any]:
        """
        Get suppressions by type.

        Args:
            domain: Domain name
            type: Suppression type (bounce, unsubscribe, whitelist)
            limit: Number of suppressions per page
            page: Page number

        Returns:
            Suppressions with pagination
        """
        valid_types = ["bounce", "unsubscribe", "whitelist"]
        if type not in valid_types:
            raise ValueError(f"Invalid suppression type. Must be one of: {', '.join(valid_types)}")

        params = {}
        if limit is not None:
            params["limit"] = str(limit)
        if page is not None:
            params["page"] = str(page)

        return await self.client.get(f"/api/domains/{domain}/suppressions/{type}", params=params)

    async def search_suppressions(
        self,
        domain: str,
        search: str,
        additional_params: Optional[dict[str, Any]] = None,
    ) -> dict[str, Any]:
        """
        Search suppressions.

        Args:
            domain: Domain name
            search: Search term
            additional_params: Additional query parameters

        Returns:
            Search results with pagination
        """
        params = {"search": search}

        if additional_params:
            params.update(additional_params)

        return await self.client.get(f"/api/domains/{domain}/suppressions", params=params)

    async def get_suppressions_paginated(
        self,
        domain: str,
        page: int = 1,
        per_page: int = 10,
        additional_params: Optional[dict[str, Any]] = None,
    ) -> dict[str, Any]:
        """
        Get suppressions with pagination.

        Args:
            domain: Domain name
            page: Page number
            per_page: Items per page
            additional_params: Additional query parameters

        Returns:
            Suppressions with pagination
        """
        params = {
            "page": page,
            "per_page": per_page,
        }

        if additional_params:
            params.update(additional_params)

        return await self.client.get(f"/api/domains/{domain}/suppressions", params=params)

    async def delete_unsubscribe_suppressions(
        self,
        domain: str,
        ids: list[int],
    ) -> dict[str, Any]:
        """
        Delete unsubscribe suppressions by IDs.

        Args:
            domain: Domain name
            ids: Array of suppression IDs to delete

        Returns:
            Deletion response
        """
        data = {"ids": ids}
        return await self.client.delete(f"/api/domains/{domain}/suppressions/unsubscribes", data=data)

    async def delete_bounce_suppressions(
        self,
        domain: str,
        ids: list[int],
    ) -> dict[str, Any]:
        """
        Delete bounce suppressions by IDs.

        Args:
            domain: Domain name
            ids: Array of suppression IDs to delete

        Returns:
            Deletion response
        """
        data = {"ids": ids}
        return await self.client.delete(f"/api/domains/{domain}/suppressions/bounces", data=data)

    async def delete_whitelist_suppressions(
        self,
        domain: str,
        ids: list[int],
    ) -> dict[str, Any]:
        """
        Delete whitelist suppressions by IDs.

        Args:
            domain: Domain name
            ids: Array of suppression IDs to delete

        Returns:
            Deletion response
        """
        data = {"ids": ids}
        return await self.client.delete(f"/api/domains/{domain}/suppressions/whitelist", data=data)

    async def create_whitelist_suppression(
        self,
        domain: str,
        recipient: str,
        recipient_type: str,
        description: Optional[str] = None,
    ) -> dict[str, Any]:
        """
        Create a new whitelist suppression.

        Args:
            domain: Domain name
            recipient: Email or domain to whitelist
            recipient_type: Type of recipient (email or domain)
            description: Optional description

        Returns:
            Created whitelist suppression data

        Raises:
            ValueError: If recipient_type is invalid
        """
        valid_types = ["email", "domain"]
        if recipient_type not in valid_types:
            raise ValueError(f"Invalid recipient type. Must be one of: {', '.join(valid_types)}")

        data = {
            "recipient": recipient,
            "recipient_type": recipient_type,
        }
        if description is not None:
            data["description"] = description

        return await self.client.post(f"/api/domains/{domain}/suppressions/whitelist", data=data)
