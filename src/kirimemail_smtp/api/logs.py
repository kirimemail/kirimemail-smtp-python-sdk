"""
Logs API for email log retrieval and streaming.
"""

from collections.abc import AsyncGenerator
from datetime import datetime
from typing import Any, Optional

from ..client.smtp_client import SmtpClient
from ..models.log_entry import LogEntry


class LogsApi:
    """
    API class for email log retrieval and streaming.
    """

    def __init__(self, client: SmtpClient) -> None:
        """
        Initialize the Logs API.

        Args:
            client: SMTP client instance
        """
        self.client = client

    async def get_logs(
        self,
        domain: str,
        limit: Optional[int] = None,
        page: Optional[int] = None,
        start: Optional[datetime] = None,
        end: Optional[datetime] = None,
        sender: Optional[str] = None,
        recipient: Optional[str] = None,
        subject: Optional[str] = None,
        event_type: Optional[str] = None,
        tags: Optional[str] = None,
    ) -> dict[str, Any]:
        """
        Get email logs for a domain.

        Args:
            domain: Domain name
            limit: Number of logs per page
            page: Page number
            start: Start date filter
            end: End date filter
            sender: Sender email filter
            recipient: Recipient email filter
            subject: Subject filter (partial match)
            event_type: Event type filter (queued, delivered, bounced, failed, opened, clicked, etc.)
            tags: Tags filter (partial match)

        Returns:
            Log entries with pagination

        Raises:
            ApiException: If event_type is invalid
        """
        if event_type is not None and event_type not in LogEntry.VALID_EVENT_TYPES:
            from ..exceptions.api_exception import ApiException
            raise ApiException(
                f"Invalid event_type '{event_type}'. Valid values are: {', '.join(LogEntry.VALID_EVENT_TYPES)}"
            )

        params = {}
        if limit is not None:
            params["limit"] = str(limit)
        if page is not None:
            params["page"] = str(page)
        if start is not None:
            params["start"] = start.isoformat()
        if end is not None:
            params["end"] = end.isoformat()
        if sender is not None:
            params["sender"] = sender
        if recipient is not None:
            params["recipient"] = recipient
        if subject is not None:
            params["subject"] = subject
        if event_type is not None:
            params["event_type"] = event_type
        if tags is not None:
            params["tags"] = tags

        return await self.client.get(f"/api/domains/{domain}/log", params=params)

    async def get_message_logs(
        self,
        domain: str,
        message_guid: str,
    ) -> dict[str, Any]:
        """
        Get logs for a specific message.

        Args:
            domain: Domain name
            message_guid: Message GUID

        Returns:
            Message log entries
        """
        return await self.client.get(f"/api/domains/{domain}/log/{message_guid}")

    async def stream_logs(
        self,
        domain: str,
        limit: Optional[int] = None,
        start: Optional[datetime] = None,
        end: Optional[datetime] = None,
        sender: Optional[str] = None,
        recipient: Optional[str] = None,
        subject: Optional[str] = None,
        event_type: Optional[str] = None,
        tags: Optional[str] = None,
    ) -> AsyncGenerator[dict[str, Any], None]:
        """
        Stream email logs for a domain.

        Args:
            domain: Domain name
            limit: Number of logs per page
            start: Start date filter
            end: End date filter
            sender: Sender email filter
            recipient: Recipient email filter
            subject: Subject filter (partial match)
            event_type: Event type filter (queued, delivered, bounced, failed, opened, clicked, etc.)
            tags: Tags filter (partial match)

        Yields:
            Log entries
        """
        if event_type is not None and event_type not in LogEntry.VALID_EVENT_TYPES:
            from ..exceptions.api_exception import ApiException
            raise ApiException(
                f"Invalid event_type '{event_type}'. Valid values are: {', '.join(LogEntry.VALID_EVENT_TYPES)}"
            )

        params = {}
        if limit is not None:
            params["limit"] = str(limit)
        if start is not None:
            params["start"] = start.isoformat()
        if end is not None:
            params["end"] = end.isoformat()
        if sender is not None:
            params["sender"] = sender
        if recipient is not None:
            params["recipient"] = recipient
        if subject is not None:
            params["subject"] = subject
        if event_type is not None:
            params["event_type"] = event_type
        if tags is not None:
            params["tags"] = tags

        async for log_entry in self.client.stream(f"/api/domains/{domain}/log", params=params):
            yield log_entry

    async def get_logs_by_date_range(
        self,
        domain: str,
        start_date: datetime,
        end_date: datetime,
        limit: Optional[int] = None,
        page: Optional[int] = None,
        sender: Optional[str] = None,
        recipient: Optional[str] = None,
        subject: Optional[str] = None,
        event_type: Optional[str] = None,
        tags: Optional[str] = None,
    ) -> dict[str, Any]:
        """
        Get logs within a date range.

        Args:
            domain: Domain name
            start_date: Start date
            end_date: End date
            limit: Number of logs per page
            page: Page number
            sender: Sender email filter
            recipient: Recipient email filter
            subject: Subject filter (partial match)
            event_type: Event type filter
            tags: Tags filter (partial match)

        Returns:
            Log entries with pagination
        """
        return await self.get_logs(
            domain=domain,
            limit=limit,
            page=page,
            start=start_date,
            end=end_date,
            sender=sender,
            recipient=recipient,
            subject=subject,
            event_type=event_type,
            tags=tags,
        )

    async def get_logs_by_event_type(
        self,
        domain: str,
        event_type: str,
        limit: Optional[int] = None,
        page: Optional[int] = None,
        start: Optional[datetime] = None,
        end: Optional[datetime] = None,
        sender: Optional[str] = None,
        recipient: Optional[str] = None,
        subject: Optional[str] = None,
        tags: Optional[str] = None,
    ) -> dict[str, Any]:
        """
        Get logs filtered by event type.

        Args:
            domain: Domain name
            event_type: Event type to filter by (use LogEntry.SMTP_EVENT_* constants)
            limit: Number of logs per page
            page: Page number
            start: Start date filter
            end: End date filter
            sender: Sender email filter
            recipient: Recipient email filter
            subject: Subject filter (partial match)
            tags: Tags filter (partial match)

        Returns:
            Log entries with pagination

        Raises:
            ApiException: If event_type is invalid

        Example:
            >>> logs = await logs_api.get_logs_by_event_type("example.com", LogEntry.SMTP_EVENT_DELIVERED)
        """
        return await self.get_logs(
            domain=domain,
            limit=limit,
            page=page,
            start=start,
            end=end,
            sender=sender,
            recipient=recipient,
            subject=subject,
            event_type=event_type,
            tags=tags,
        )

    async def get_logs_by_tags(
        self,
        domain: str,
        tags: str,
        limit: Optional[int] = None,
        page: Optional[int] = None,
        start: Optional[datetime] = None,
        end: Optional[datetime] = None,
        sender: Optional[str] = None,
        recipient: Optional[str] = None,
        subject: Optional[str] = None,
        event_type: Optional[str] = None,
    ) -> dict[str, Any]:
        """
        Get logs filtered by tags.

        Args:
            domain: Domain name
            tags: Tags to filter by (partial match)
            limit: Number of logs per page
            page: Page number
            start: Start date filter
            end: End date filter
            sender: Sender email filter
            recipient: Recipient email filter
            subject: Subject filter (partial match)
            event_type: Event type filter

        Returns:
            Log entries with pagination

        Example:
            >>> logs = await logs_api.get_logs_by_tags("example.com", "newsletter")
        """
        return await self.get_logs(
            domain=domain,
            limit=limit,
            page=page,
            start=start,
            end=end,
            sender=sender,
            recipient=recipient,
            subject=subject,
            event_type=event_type,
            tags=tags,
        )


