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


# How to Run
You can use the provided install script
### or


1. Install Python `3.12.10`

2. Clone the repository and move into the project folder

```bash
git clone <repo-url>
```

3. Create a virtual environment

```bash
py -m venv .venv
```

4. Activate the virtual environment

### Windows (PowerShell)

```powershell
.venv\Scripts\Activate.ps1
```

### Windows (CMD)

```cmd
.venv\Scripts\activate.bat
```

### Linux/macOS

```bash
source .venv/bin/activate
```

5. Install dependencies

```bash
pip install -r requirements.txt
```

6. Install Playwright browsers

```bash
playwright install
```

7. Start the MCP development server

```bash
mcp dev mcp_server.py
```

This opens the MCP developer panel in your browser.

8. Press **"Connect to Server"**

9. Open the **Tools** tab

10. Press **"List Tools"**

11. Select the `tracker` tool and enter a reference number from the table above