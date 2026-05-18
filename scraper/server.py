'''
server.py
author: Jernskegg

This module defines the server-side logic for
retrieving and processing shipment tracking information.

It includes an asynchronous function to fetch raw tracking data,
parse it, and return a structured ShipmentTracking object.

The main block demonstrates how to use this function with
a sample reference number.
'''
from models import (
    ShipmentTracking,
    Party,
    Package,
)
from parser import parse_tracking_data
from scraper import process_start
import asyncio


async def get_shipment(reference_number: str) -> ShipmentTracking:
    raw_data = await process_start([reference_number])

    if not raw_data:
        return ShipmentTracking(
            reference_number=reference_number,
            sender=Party(),
            receiver=Party(),
            package=Package(),
            tracking_history=[],
        )

    shipment_data = raw_data.get(reference_number)

    if not shipment_data:
        return ShipmentTracking(
            reference_number=reference_number,
            sender=Party(),
            receiver=Party(),
            package=Package(),
            tracking_history=[],
        )

    return parse_tracking_data(shipment_data)


if __name__ == "__main__":
    ref_number = "1806290829"

    shipment_info = asyncio.run(get_shipment(ref_number))

    print(shipment_info.model_dump_json(indent=2))