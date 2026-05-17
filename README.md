# Sendify Code Challenge: DB Schenker Shipment Tracker MCP Server

## The Task

Build an MCP (Model Context Protocol) server with a tool that tracks DB Schenker shipments.

### Requirements

Your MCP server must expose a tool that:

1. **Accepts** a DB Schenker tracking reference number as input
2. **Returns** structured shipment information including:
   - Sender information (name, address)
   - Receiver information (name, address)
   - Package details (weight, dimensions, piece count, etc.)
   - Complete tracking history for the shipment
   - **Bonus:** Individual tracking events per package

### Data Source

Use the public DB Schenker tracking website:
```
https://www.dbschenker.com/app/tracking-public/
```

### Example Reference Numbers

Use these reference numbers for testing:

| Reference Number |
|------------------|
| 1806203236       |
| 1806290829       |
| 1806273700       |
| 1806272330       |
| 1806271886       |
| 1806270433       |
| 1806268072       |
| 1806267579       |
| 1806264568       |
| 1806258974       |
| 1806256390       |