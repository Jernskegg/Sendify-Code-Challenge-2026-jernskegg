'''
parser.py
author: Jernskegg

This module parses raw shipment tracking data into
structured shipment model objects.

It extracts sender, receiver, package, and event details
from the raw API response.
'''

from tracker_tool.models import (
    ShipmentTracking,
    Party,
    Measurement,
    ShipmentPackage,
    TrackingEvent,
    PackageTracking,
)
import datetime


def parse_tracking_data(raw_data: dict) -> ShipmentTracking:
    shipment_detail = raw_data.get("shipment_detail", {})

    location = shipment_detail.get("location", {})
    goods = shipment_detail.get("goods", {})
    events = shipment_detail.get("events", [])

    sender_info = location.get("shipperPlace", {})
    receiver_info = location.get("consigneePlace", {})

    references = (
        shipment_detail.get("references", {})
        .get("waybillAndConsignementNumbers", [])
    )

    package_tracking = []

    for pkg in shipment_detail.get("packages", []):
        events_list = []
        for event in pkg.get("events", []):
            raw_ts = event.get("date")
            ts = None
            if raw_ts:
                try:
                    ts = datetime.datetime.fromisoformat(
                        raw_ts.replace("Z", "+00:00")
                    ).date()
                except Exception:
                    ts = None

            # location may be an object or a string
            loc = event.get("location")
            if isinstance(loc, dict):
                loc = loc.get("name")

            events_list.append(
                TrackingEvent(
                    timestamp=ts,
                    status=event.get("code"),
                    location=loc,
                )
            )

        package_tracking.append(
            PackageTracking(
                id=pkg.get("id", ""),
                tracking_history=events_list,
            )
        )

    # The raw payload's "dimensions" is always empty; use loadingMeters instead
    loading = goods.get("loadingMeters", {})
    dims_measurement = None
    if isinstance(loading, dict):
        val = loading.get("value")
        unit = loading.get("unit")
        if val is not None or unit is not None:
            dims_measurement = Measurement(value=val, unit=unit)

    # Build parsed tracking history with date objects
    tracking_history_list = []
    for event in events:
        raw_ts = event.get("date")
        ts = None
        if raw_ts:
            try:
                ts = datetime.datetime.fromisoformat(
                    raw_ts.replace("Z", "+00:00")
                ).date()
            except Exception:
                ts = None

        loc = event.get("location")
        if isinstance(loc, dict):
            loc = loc.get("name")

        tracking_history_list.append(
            TrackingEvent(
                timestamp=ts,
                status=event.get("comment"),
                location=loc,
                event_code=event.get("code"),
            )
        )

    return ShipmentTracking(
        reference_number=references[0] if references else "",

        status=shipment_detail.get("progressBar", {}).get("activeStep"),

        progress_percentage=shipment_detail.get("percentageProgress"),

        estimated_delivery=shipment_detail.get(
            "deliveryDate", {}).get("estimated"
                                    ),

        sender=Party(
            city=sender_info.get("city"),
            postal_code=sender_info.get("postCode"),
            country=sender_info.get("country"),
        ),

        receiver=Party(
            city=receiver_info.get("city"),
            postal_code=receiver_info.get("postCode"),
            country=receiver_info.get("country"),
        ),

        package=ShipmentPackage(
            weight=Measurement(
                value=goods.get("weight", {}).get("value"),
                unit=goods.get("weight", {}).get("unit"),
            ),
            volume=Measurement(
                value=goods.get("volume", {}).get("value"),
                unit=goods.get("volume", {}).get("unit"),
            ),
            piece_count=goods.get("pieces"),
            dimensions=dims_measurement,
        ),

        tracking_history=tracking_history_list,

        packages=package_tracking,
    )
