from mcp.server.fastmcp import FastMCP

from tracker_tool.server import get_shipment

mcp = FastMCP("Sendify Tracking Server")


@mcp.tool()
async def track_shipment(reference_number: str) -> dict:
    """
    Retrieve shipment tracking information from a DB Schenker reference number.
    """

    shipment = await get_shipment(reference_number)

    return shipment.model_dump()


if __name__ == "__main__":
    mcp.run()
