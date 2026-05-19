Write-Host "Creating virtual environment..."
py -m venv .venv

Write-Host "Activating virtual environment..."
& ".\.venv\Scripts\Activate.ps1"

Write-Host "Installing requirements..."
pip install -r requirements.txt

Write-Host "Installing Playwright browsers..."
playwright install

Write-Host "Starting MCP server..."
mcp dev mcp_server.py