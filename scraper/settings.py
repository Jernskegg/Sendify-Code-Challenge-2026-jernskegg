'''
settings.py
Author: Jernskegg
Date: 2026-05-17

This file is for setting environment variables used in the code.
You can also use it to set other configuration options if needed.
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
