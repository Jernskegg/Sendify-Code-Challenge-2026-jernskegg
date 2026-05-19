@echo off

echo Creating virtual environment...
py -m venv .venv

echo Activating virtual environment...
call .venv\Scripts\activate.bat

echo Installing requirements...
pip install -r requirements.txt

echo Installing Playwright browsers...
playwright install

echo Starting MCP server...
mcp dev mcp_server.py

pause