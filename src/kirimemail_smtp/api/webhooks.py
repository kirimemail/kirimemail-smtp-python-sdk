"""
Webhooks API for webhook management.
"""

from typing import Any, Optional

from ..client.smtp_client import SmtpClient


class WebhooksApi:
    """
    API class for webhook management.
    """

    VALID_EVENT_TYPES = [
        "queued",
        "send",
        "delivered",
        "bounced",
        "failed",
        "permanent_fail",
        "opened",
        "clicked",
        "unsubscribed",
        "temporary_fail",
        "deferred",
    ]

    def __init__(self, client: SmtpClient) -> None:
        """
        Initialize the Webhooks API.

        Args:
            client: SMTP client instance
        """
        self.client = client

    async def list_webhooks(
        self,
        domain: str,
        webhook_type: Optional[str] = None,
    ) -> dict[str, Any]:
        """
        List webhooks for a domain.

        Args:
            domain: Domain name
            webhook_type: Filter webhooks by event type

        Returns:
            List of webhooks

        Raises:
            ValueError: If webhook_type is invalid
        """
        if webhook_type and webhook_type not in self.VALID_EVENT_TYPES:
            raise ValueError(f"Invalid webhook type. Must be one of: {', '.join(self.VALID_EVENT_TYPES)}")

        params = {}
        if webhook_type is not None:
            params["type"] = webhook_type

        return await self.client.get(f"/api/domains/{domain}/webhooks", params=params)

    async def create_webhook(
        self,
        domain: str,
        webhook_type: str,
        url: str,
    ) -> dict[str, Any]:
        """
        Create a new webhook.

        Args:
            domain: Domain name
            webhook_type: Event type that will trigger this webhook
            url: URL endpoint where webhook events will be sent

        Returns:
            Created webhook data

        Raises:
            ValueError: If webhook_type is invalid
        """
        if webhook_type not in self.VALID_EVENT_TYPES:
            raise ValueError(f"Invalid webhook type. Must be one of: {', '.join(self.VALID_EVENT_TYPES)}")

        data = {
            "type": webhook_type,
            "url": url,
        }
        return await self.client.post(f"/api/domains/{domain}/webhooks", data=data)

    async def get_webhook(
        self,
        domain: str,
        webhook_guid: str,
    ) -> dict[str, Any]:
        """
        Get a specific webhook.

        Args:
            domain: Domain name
            webhook_guid: Unique identifier (GUID) of webhook

        Returns:
            Webhook data
        """
        return await self.client.get(f"/api/domains/{domain}/webhooks/{webhook_guid}")

    async def update_webhook(
        self,
        domain: str,
        webhook_guid: str,
        webhook_type: Optional[str] = None,
        url: Optional[str] = None,
    ) -> dict[str, Any]:
        """
        Update a webhook.

        Args:
            domain: Domain name
            webhook_guid: Unique identifier (GUID) of webhook to update
            webhook_type: New event type
            url: New URL endpoint

        Returns:
            Updated webhook data

        Raises:
            ValueError: If webhook_type is invalid
            ValueError: If no fields provided to update
        """
        if webhook_type is not None and webhook_type not in self.VALID_EVENT_TYPES:
            raise ValueError(f"Invalid webhook type. Must be one of: {', '.join(self.VALID_EVENT_TYPES)}")

        if webhook_type is None and url is None:
            raise ValueError("At least one of 'webhook_type' or 'url' must be provided")

        data = {}
        if webhook_type is not None:
            data["type"] = webhook_type
        if url is not None:
            data["url"] = url

        return await self.client.put(f"/api/domains/{domain}/webhooks/{webhook_guid}", data=data)

    async def delete_webhook(
        self,
        domain: str,
        webhook_guid: str,
    ) -> dict[str, Any]:
        """
        Delete a webhook.

        Args:
            domain: Domain name
            webhook_guid: Unique identifier (GUID) of webhook to delete

        Returns:
            Deletion response
        """
        return await self.client.delete(f"/api/domains/{domain}/webhooks/{webhook_guid}")

    async def test_webhook(
        self,
        domain: str,
        url: str,
        event_type: str,
    ) -> dict[str, Any]:
        """
        Test a webhook URL.

        Args:
            domain: Domain name
            url: URL endpoint to test
            event_type: Event type to use for test

        Returns:
            Test result

        Raises:
            ValueError: If event_type is invalid
        """
        if event_type not in self.VALID_EVENT_TYPES:
            raise ValueError(f"Invalid event type. Must be one of: {', '.join(self.VALID_EVENT_TYPES)}")

        data = {
            "url": url,
            "event_type": event_type,
        }
        return await self.client.post(f"/api/domains/{domain}/webhooks/test", data=data)
