'''
settings.py
author: Jernskegg

This module defines configuration values used by the
shipment tracking scraper.

It reads environment variables for the tracking URL,
headless mode, motion settings, and request timeout.
'''

import os


TRACKING_URL_DOMAIN = os.getenv(
    "TRACKING_URL_DOMAIN",
    "https://mydsv.dsv.com/"
)

TRACKING_URL_PATH = os.getenv(
    "TRACKING_URL_PATH",
    "app/tracking-public/?refNumber="
)

TRACKING_URL = (
    TRACKING_URL_DOMAIN +
    TRACKING_URL_PATH
)

HEADLESS = os.getenv(
    "HEADLESS",
    "true"
).lower() == "true"

SLOW_MOTION_MS = int(
    os.getenv(
        "SLOW_MOTION_MS",
        "300"
    )
)

REQUEST_TIMEOUT_MS = int(
    os.getenv(
        "REQUEST_TIMEOUT_MS",
        "30000"
    )
)
