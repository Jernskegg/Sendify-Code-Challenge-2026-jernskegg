import asyncio
import json
import os  # noqa: F401
import settings
from pathlib import Path

from playwright.async_api import async_playwright

# REFERENCE_NUMBER = "1806290829"
REFERENCE_NUMBERS = [
    "3476472018",
    "1806264568",  # WILL FAIL - NOT FOUND
    "3476265230",
    "3476265248",
    "3476257542",
    "3476238161",
    "1806258974",  # WILL FAIL - NOT FOUND
    "3476236157",
    "3476230325",
    "3476219849",
    "1806256390",  # WILL FAIL - NOT FOUND
    "3476207869",
    "3476186295",
]


async def save_json(filename: str, data: dict, output_dir: Path):
    filepath = output_dir / filename

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


async def handle_response(response, result):

    url = response.url

    if "tracking-public" not in url:
        return

    try:
        content_type = response.headers.get("content-type", "")

        if "application/json" not in content_type:
            return

        data = await response.json()

        if "shipments?query=" in url:
            result["search_response"] = data

        elif "/trip" in url:
            result["trip_response"] = data

        elif "LandStt:" in url:
            result["shipment_detail"] = data

    except Exception as e:
        print(f"Failed parsing response: {e}")


async def process_reference_number(browser, reference_number):
    result = {
        "search_response": None,
        "trip_response": None,
        "shipment_detail": None,
    }

    tracking_url = settings.TRACKING_URL + reference_number

    context = await browser.new_context()
    page = await context.new_page()

    tasks = []

    # Proper async-safe wrapper
    page.on(
        "response",
        lambda response: tasks.append(
            asyncio.create_task(
                handle_response(response, result))
        ),
    )

    await page.goto(
        tracking_url,
        wait_until="networkidle",
        timeout=settings.REQUEST_TIMEOUT_MS
    )

    await page.wait_for_timeout(10000)
    await asyncio.gather(*tasks)
    await context.close()

    return result


async def process_start(ref_arr):
    results = {}
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=settings.HEADLESS,
            slow_mo=settings.SLOW_MOTION_MS,
        )

        # add enumarate to show progress
        for index, reference_number in enumerate(ref_arr, start=1):
            print(
                f"[{index}/{len(ref_arr)}] "
                f"{index/len(ref_arr)*100:.0f}% "
                f"- Processing {reference_number}"
            )

            results[reference_number] = await process_reference_number(
                browser,
                reference_number,
            )

        await browser.close()

        output_dir = Path("output/")
        output_dir.mkdir(parents=True, exist_ok=True)
        return results


if __name__ == "__main__":
    asyncio.run(process_start(REFERENCE_NUMBERS))
