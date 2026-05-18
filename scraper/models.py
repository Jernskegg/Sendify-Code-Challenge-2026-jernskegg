'''
models.py
author: Jernskegg

This module defines the data models used to represent
shipment tracking information.

It includes structured classes for parties, packages,
tracking events, and the full shipment response.
'''

from pydantic import BaseModel


class Party(BaseModel):
    address: str | None = None
    city: str | None = None
    zip_code: str | None = None
    country: str | None = None


class TrackingEvent(BaseModel):
    timestamp: str | None = None
    status: str | None = None
    location: str | None = None


class Package(BaseModel):
    weight: float | None = None
    piece_count: int | None = None


class ShipmentTracking(BaseModel):
    reference_number: str
    sender: Party
    receiver: Party
    package: Package
    tracking_history: list[TrackingEvent]
