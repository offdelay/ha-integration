"""
Runtime data types for offdelay.

Access pattern: entry.runtime_data.client / entry.runtime_data.coordinator
"""

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from homeassistant.config_entries import ConfigEntry
    from homeassistant.loader import Integration

    from .api import OffdelayApiClient
    from .coordinator import OffdelayDataUpdateCoordinator


type OffdelayConfigEntry = ConfigEntry[OffdelayData]


@dataclass
class OffdelayData:
    """Runtime data stored on the config entry after a successful setup."""

    client: OffdelayApiClient
    coordinator: OffdelayDataUpdateCoordinator
    integration: Integration
