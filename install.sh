#!/bin/bash

echo "Creating virtual environment..."
python3 -m venv .venv

echo "Activating virtual environment..."
source .venv/bin/activate

echo "Installing requirements..."
pip install -r requirements.txt

echo "Installing Playwright browsers..."
playwright install

echo "Starting MCP server..."
mcp dev mcp_server.py