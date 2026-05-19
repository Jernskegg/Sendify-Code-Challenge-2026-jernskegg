'''
models.py
author: Jernskegg

This module defines the data models used to represent
shipment tracking information.

It includes structured classes for parties, packages,
tracking events, and the full shipment response.
'''

from pydantic import BaseModel
import datetime


class Party(BaseModel):
    city: str | None = None
    postal_code: str | None = None
    country: str | None = None


class Measurement(BaseModel):
    value: float | None = None
    unit: str | None = None


class TrackingEvent(BaseModel):
    timestamp: datetime.date | None = None
    status: str | None = None
    location: str | None = None
    event_code: str | None = None


class ShipmentPackage(BaseModel):
    piece_count: int | None = None
    weight: Measurement | None = None
    volume: Measurement | None = None
    dimensions: Measurement | None = None


class PackageTracking(BaseModel):
    id: str
    tracking_history: list[TrackingEvent] = []


class ShipmentTracking(BaseModel):
    reference_number: str

    status: str | None = None
    progress_percentage: int | None = None
    estimated_delivery: str | None = None

    sender: Party
    receiver: Party

    package: ShipmentPackage

    tracking_history: list[TrackingEvent] = []

    packages: list[PackageTracking] = []
