"""
Tests for Pydantic models.
"""

import pytest
from datetime import datetime
from pydantic import ValidationError

from kirimemail_smtp.models import (
    Credential,
    Domain,
    EmailValidationResult,
    EmailValidationBatchResult,
    LogEntry,
    Pagination,
    Quota,
    Suppression,
    Webhook,
)


class TestCredential:
    """Test cases for Credential model."""

    def test_credential_creation(self):
        """Test creating a valid credential."""
        data = {
            "id": 1,
            "user_smtp_guid": "550e8400-e29b-41d4-a716-446655440000",
            "username": "test@example.com",
            "domain": "example.com",
            "created_at": 1672531200,
            "modified_at": 1672531200
        }

        credential = Credential(**data)

        assert credential.id == 1
        assert credential.user_smtp_guid == "550e8400-e29b-41d4-a716-446655440000"
        assert credential.username == "test@example.com"
        assert credential.domain == "example.com"
        assert credential.created_at == 1672531200
        assert credential.modified_at == 1672531200


class TestDomain:
    """Test cases for Domain model."""

    def test_domain_creation(self):
        """Test creating a valid domain."""
        data = {
            "id": 1,
            "domain": "example.com",
            "dns_selector": "kirim",
            "dns_record": "v=DKIM1; k=rsa; p=...",
            "click_track": True,
            "open_track": True,
            "unsub_track": True,
            "is_verified": True,
            "status": True,
            "tracklink_domain": "track.example.com",
            "tracklink_domain_is_verified": True,
            "auth_domain_is_verified": False,
            "spf_record": "v=spf1 mx include:spf.kirim.email ~all",
            "created_at": 1672531200,
            "modified_at": 1672531200,
            "dkim_key_length": 2048
        }

        domain = Domain(**data)

        assert domain.id == 1
        assert domain.domain == "example.com"
        assert domain.dns_selector == "kirim"
        assert domain.dns_record == "v=DKIM1; k=rsa; p=..."
        assert domain.click_track is True
        assert domain.open_track is True
        assert domain.unsub_track is True
        assert domain.is_verified is True
        assert domain.status is True
        assert domain.tracklink_domain == "track.example.com"
        assert domain.tracklink_domain_is_verified is True
        assert domain.auth_domain_is_verified is False

    def test_domain_minimal(self):
        """Test domain with minimal required fields."""
        data = {
            "id": 1,
            "domain": "example.com",
            "dns_selector": "k1",
            "dns_record": "v=DKIM1; k=rsa; p=...",
            "click_track": False,
            "open_track": False,
            "unsub_track": False,
            "is_verified": False,
            "status": True,
            "tracklink_domain": "",
            "tracklink_domain_is_verified": False,
            "auth_domain_is_verified": False,
            "spf_record": None,
            "created_at": 1672531200,
            "modified_at": 1672531200
        }

        domain = Domain(**data)

        assert domain.domain == "example.com"
        assert domain.dns_selector == "k1"
        assert domain.dns_record == "v=DKIM1; k=rsa; p=..."
        assert domain.is_verified is False
        assert domain.status is True


class TestEmailValidationResult:
    """Test cases for EmailValidationResult model."""

    def test_email_validation_result_creation(self):
        """Test creating a valid email validation result."""
        data = {
            "email": "user@example.com",
            "is_valid": True,
            "error": None,
            "warnings": [],
            "cached": False,
            "validated_at": "2023-01-01T12:00:00Z",
            "is_spamtrap": False,
            "spamtrap_score": 0.1
        }

        result = EmailValidationResult(**data)

        assert result.email == "user@example.com"
        assert result.is_valid is True
        assert result.error is None
        assert result.warnings == []
        assert result.cached is False
        assert result.is_spamtrap is False
        assert result.spamtrap_score == 0.1

    def test_email_validation_result_invalid(self):
        """Test invalid email validation result."""
        data = {
            "email": "invalid-email",
            "is_valid": False,
            "error": "Invalid email format",
            "warnings": ["Email looks suspicious"],
            "cached": True,
            "validated_at": "2023-01-01T12:00:00Z",
            "is_spamtrap": True,
            "spamtrap_score": 0.9
        }

        result = EmailValidationResult(**data)

        assert result.is_valid is False
        assert result.error == "Invalid email format"
        assert result.is_spamtrap is True
        assert result.spamtrap_score == 0.9


class TestEmailValidationBatchResult:
    """Test cases for EmailValidationBatchResult model."""

    def test_email_validation_batch_result_creation(self):
        """Test creating a valid batch validation result."""
        data = {
            "results": [
                {
                    "email": "user1@example.com",
                    "is_valid": True,
                    "error": None,
                    "warnings": [],
                    "cached": False,
                    "validated_at": "2023-01-01T12:00:00Z",
                    "is_spamtrap": False,
                    "spamtrap_score": 0.1
                },
                {
                    "email": "user2@example.com",
                    "is_valid": False,
                    "error": "Bounced",
                    "warnings": [],
                    "cached": True,
                    "validated_at": "2023-01-01T12:00:00Z",
                    "is_spamtrap": False,
                    "spamtrap_score": 0.0
                }
            ],
            "summary": {
                "total": 2,
                "valid": 1,
                "invalid": 1,
                "cached": 1,
                "validated": 1
            }
        }

        result = EmailValidationBatchResult(**data)

        assert len(result.results) == 2
        assert result.summary.total == 2
        assert result.summary.valid == 1
        assert result.summary.invalid == 1
        assert result.summary.cached == 1
        assert result.summary.validated == 1


class TestWebhook:
    """Test cases for Webhook model."""

    def test_webhook_creation(self):
        """Test creating a valid webhook."""
        data = {
            "webhook_guid": "550e8400-e29b-41d4-a716-446655440001",
            "user_guid": "user-guid-123",
            "user_domain_guid": "domain-guid-456",
            "user_smtp_guid": "smtp-guid-789",
            "type": "delivered",
            "url": "https://example.com/webhook",
            "is_deleted": False,
            "created_at": 1672531200,
            "modified_at": 1672531200
        }

        webhook = Webhook(**data)

        assert webhook.webhook_guid == "550e8400-e29b-41d4-a716-446655440001"
        assert webhook.user_guid == "user-guid-123"
        assert webhook.user_domain_guid == "domain-guid-456"
        assert webhook.user_smtp_guid == "smtp-guid-789"
        assert webhook.type == "delivered"
        assert webhook.url == "https://example.com/webhook"
        assert webhook.is_deleted is False

    def test_webhook_minimal(self):
        """Test webhook with minimal required fields (user_smtp_guid is optional)."""
        data = {
            "webhook_guid": "550e8400-e29b-41d4-a716-446655440001",
            "user_guid": "user-guid-123",
            "user_domain_guid": "domain-guid-456",
            "user_smtp_guid": None,
            "type": "opened",
            "url": "https://example.com/webhook",
            "is_deleted": False,
            "created_at": 1672531200,
            "modified_at": 1672531200
        }

        webhook = Webhook(**data)

        assert webhook.user_smtp_guid is None


class TestQuota:
    """Test cases for Quota model."""

    def test_quota_creation(self):
        """Test creating a valid quota."""
        data = {
            "current_quota": 50000,
            "max_quota": 100000,
            "usage_percentage": 50.0
        }

        quota = Quota(**data)

        assert quota.current_quota == 50000
        assert quota.max_quota == 100000
        assert quota.remaining == 50000
        assert quota.usage == 50000
        assert quota.usage_percentage == 50.0

    def test_quota_full(self):
        """Test quota when full."""
        data = {
            "current_quota": 0,
            "max_quota": 100000,
            "usage_percentage": 100.0
        }

        quota = Quota(**data)

        assert quota.remaining == 0
        assert quota.usage == 100000
        assert quota.usage_percentage == 100.0


class TestLogEntry:
    """Test cases for LogEntry model."""

    def test_log_entry_creation(self):
        """Test creating a valid log entry."""
        data = {
            "id": "log-123",
            "message_id": "msg-123",
            "event_type": "sent",
            "recipient": "user@example.com",
            "response_message": "250 OK",
            "created_at": datetime(2023, 1, 1, 0, 0, 0)
        }

        log_entry = LogEntry(**data)

        assert log_entry.id == "log-123"
        assert log_entry.message_id == "msg-123"
        assert log_entry.event_type == "sent"
        assert log_entry.recipient == "user@example.com"
        assert log_entry.response_message == "250 OK"

    def test_log_entry_optional_fields(self):
        """Test log entry with optional fields."""
        log_entry = LogEntry(
            id="log-123",
            message_id="msg-123",
            event_type="delivered",
            created_at=datetime(2023, 1, 1, 0, 0, 0)
        )

        assert log_entry.id == "log-123"
        assert log_entry.message_id == "msg-123"
        assert log_entry.event_type == "delivered"
        assert log_entry.recipient is None
        assert log_entry.response_message is None


class TestPagination:
    """Test cases for Pagination model."""

    def test_pagination_creation(self):
        """Test creating a valid pagination."""
        data = {
            "total": 100,
            "page": 1,
            "limit": 10,
            "offset": 0
        }

        pagination = Pagination(**data)

        assert pagination.total == 100
        assert pagination.page == 1
        assert pagination.limit == 10
        assert pagination.offset == 0

    def test_pagination_calculation(self):
        """Test pagination with calculated fields."""
        pagination = Pagination(total=100, limit=25, page=2, offset=25)

        assert pagination.total == 100
        assert pagination.page == 2
        assert pagination.limit == 25
        assert pagination.offset == 25
        assert pagination.has_next is True
        assert pagination.has_previous is True
        assert pagination.next_offset == 50
        assert pagination.previous_offset == 0

    def test_pagination_first_page(self):
        """Test pagination on first page."""
        pagination = Pagination(total=100, limit=25, page=1, offset=0)

        assert pagination.has_next is True
        assert pagination.has_previous is False
        assert pagination.next_offset == 25
        assert pagination.previous_offset is None

    def test_pagination_last_page(self):
        """Test pagination on last page."""
        pagination = Pagination(total=75, limit=25, page=3, offset=50)

        assert pagination.has_next is False
        assert pagination.has_previous is True
        assert pagination.next_offset is None
        assert pagination.previous_offset == 25


class TestSuppression:
    """Test cases for Suppression model."""

    def test_suppression_creation(self):
        """Test creating a valid suppression."""
        data = {
            "id": 1,
            "type": "bounce",
            "recipient_type": "email",
            "recipient": "user@example.com",
            "tags": "marketing",
            "description": "Hard bounce",
            "source": "smtp",
            "created_at": 1672531200
        }

        suppression = Suppression(**data)

        assert suppression.id == 1
        assert suppression.type == "bounce"
        assert suppression.recipient_type == "email"
        assert suppression.recipient == "user@example.com"
        assert suppression.tags == "marketing"
        assert suppression.description == "Hard bounce"
        assert suppression.source == "smtp"

    def test_suppression_minimal(self):
        """Test suppression with minimal required fields."""
        data = {
            "id": 1,
            "type": "unsubscribe",
            "recipient_type": "email",
            "recipient": "user@example.com",
            "tags": None,
            "description": None,
            "source": None,
            "created_at": 1672531200
        }

        suppression = Suppression(**data)

        assert suppression.recipient == "user@example.com"
        assert suppression.type == "unsubscribe"
        assert suppression.tags is None
        assert suppression.description is None
        assert suppression.source is None

    def test_suppression_whitelist(self):
        """Test whitelist suppression."""
        data = {
            "id": 1,
            "type": "whitelist",
            "recipient_type": "domain",
            "recipient": "example.com",
            "description": "Trusted domain",
            "created_at": 1672531200
        }

        suppression = Suppression(**data)

        assert suppression.type == "whitelist"
        assert suppression.recipient_type == "domain"
        assert suppression.recipient == "example.com"

    def test_suppression_invalid_type(self):
        """Test suppression with invalid type."""
        with pytest.raises(ValidationError):
            Suppression(
                id=1,
                type="invalid_type",
                recipient_type="email",
                recipient="user@example.com",
                created_at=1672531200
            )

    def test_suppression_invalid_recipient_type(self):
        """Test suppression with invalid recipient_type."""
        with pytest.raises(ValidationError):
            Suppression(
                id=1,
                type="bounce",
                recipient_type="invalid",
                recipient="user@example.com",
                created_at=1672531200
            )
