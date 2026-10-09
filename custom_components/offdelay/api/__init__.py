"""
API package for offdelay.

Exception hierarchy:
    OffdelayApiClientError (base)
    ├── OffdelayApiClientCommunicationError (network/timeout)
    └── OffdelayApiClientAuthenticationError (401/403)

The coordinator maps them onto ConfigEntryAuthFailed and UpdateFailed; nothing else
in the integration imports this package.
"""

from .client import (
    FAN_SPEEDS,
    OffdelayApiClient,
    OffdelayApiClientAuthenticationError,
    OffdelayApiClientCommunicationError,
    OffdelayApiClientError,
)

__all__ = [
    "FAN_SPEEDS",
    "OffdelayApiClient",
    "OffdelayApiClientAuthenticationError",
    "OffdelayApiClientCommunicationError",
    "OffdelayApiClientError",
]
