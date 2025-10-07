"""
Basic usage example for the Kirim.Email SMTP Python SDK.
"""

import asyncio
from kirimemail_smtp import SmtpClient, MessagesApi


async def send_basic_email():
    """Send a basic email using the SDK."""
    # Initialize the client
    client = SmtpClient(
        username="your-username",
        token="your-token"
    )
    
    # Create the messages API
    messages_api = MessagesApi(client)
    
    # Prepare the email message
    message = {
        "from": "sender@example.com",
        "from_name": "Company Name",
        "to": "recipient@example.com",
        "subject": "Hello from Python SDK",
        "text": "This is a test email sent using the Kirim.Email Python SDK.",
        "html": "<p>This is a test email sent using the <strong>Kirim.Email Python SDK</strong>.</p>"
    }
    
    try:
        # Send the email
        result = await messages_api.send_message("example.com", message)
        print("Email sent successfully!")
        print(f"Result: {result}")
    
    except Exception as e:
        print(f"Failed to send email: {e}")
    
    finally:
        # Clean up the client
        await client.close()


async def send_template_email():
    """Send a template email using the SDK."""
    client = SmtpClient(
        username="your-username",
        token="your-token"
    )
    
    messages_api = MessagesApi(client)
    
    template = {
        "template_guid": "your-template-uuid",
        "from": "sender@example.com",
        "from_name": "Company Name",
        "to": "recipient@example.com",
        "variables": {
            "name": "John Doe",
            "product": "Premium Plan",
            "company": "Your Company"
        }
    }
    
    try:
        result = await messages_api.send_template_message("example.com", template)
        print("Template email sent successfully!")
        print(f"Result: {result}")
    
    except Exception as e:
        print(f"Failed to send template email: {e}")
    
    finally:
        await client.close()


async def send_email_with_attachments():
    """Send an email with attachments using the SDK."""
    client = SmtpClient(
        username="your-username",
        token="your-token"
    )
    
    messages_api = MessagesApi(client)
    
    message = {
        "from": "sender@example.com",
        "from_name": "Company Name",
        "to": "recipient@example.com",
        "subject": "Email with attachments",
        "text": "Please find the attached files."
    }
    
    files = [
        {
            "field": "attachment",
            "filename": "document.txt",
            "content": b"This is a test document.",
            "content_type": "text/plain"
        },
        {
            "field": "attachment",
            "filename": "report.pdf",
            "content": b"PDF content here",
            "content_type": "application/pdf"
        }
    ]
    
    try:
        result = await messages_api.send_message_with_attachments(
            "example.com", message, files
        )
        print("Email with attachments sent successfully!")
        print(f"Result: {result}")
    
    except Exception as e:
        print(f"Failed to send email with attachments: {e}")
    
    finally:
        await client.close()


async def main():
    """Run all examples."""
    print("=== Basic Email Example ===")
    await send_basic_email()
    
    print("\n=== Template Email Example ===")
    await send_template_email()
    
    print("\n=== Email with Attachments Example ===")
    await send_email_with_attachments()


if __name__ == "__main__":
    asyncio.run(main())