'''
parser.py
author: Jernskegg

This module parses raw shipment tracking data into
structured shipment model objects.

It extracts sender, receiver, package, and event details
from the raw API response.
'''

from models import (
    ShipmentTracking,
    Party,
    Package,
    TrackingEvent,
)


def parse_tracking_data(raw_data: dict) -> ShipmentTracking:
    shipment_detail = raw_data.get("shipment_detail", {})
    location = shipment_detail.get("location", {})
    goods = shipment_detail.get("goods", {})
    events = shipment_detail.get("events", [])

    sender_info = location.get("shipperPlace", {})
    receiver_info = location.get("consigneePlace", {})

    return ShipmentTracking(
        reference_number=shipment_detail.get("references", {})
        .get("waybillAndConsignementNumbers", [""])[0],

        sender=Party(
            city=sender_info.get("city"),
            zip_code=sender_info.get("postCode"),
            country=sender_info.get("country"),
        ),

        receiver=Party(
            city=receiver_info.get("city"),
            zip_code=receiver_info.get("postCode"),
            country=receiver_info.get("country"),
        ),

        package=Package(
            weight=goods.get("weight", {}).get("value"),
            piece_count=goods.get("pieces"),
        ),

        tracking_history=[
            TrackingEvent(
                timestamp=event.get("date"),
                status=event.get("comment"),
                location=event.get("location", {}).get("name"),
            )
            for event in events
        ],
    )