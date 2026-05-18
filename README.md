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
| 1806290829 LAND  |
| 3476472018       |
| 3476265230       |
| 3476265248       |
| 3476257542       |
| 3476238161       |
| 3476236157       |
| 3476230325       |
| 3476219849       |
| 3476207869       |
| 3476186295       |

| Failing Numbers  |
|------------------|
| 1806264568       |
| 1806258974       |
| 1806256390       |