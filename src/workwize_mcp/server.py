"""Main MCP server module for Workwize API."""
import asyncio
import logging
from typing import List

from mcp.server import Server
from mcp.tools import Tool

from .config import config
from .tools import (
    # Orders
    GetOrderTool,
    GetOrdersTool,
    GetOrderShipmentsTool,
    # Assets
    GetAssetsTool,
    GetWarehousesTool,
    # Employees
    CreateEmployeeAssetTool,
    # Offices
    GetOfficesTool,
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class WorkwizeMCPServer(Server):
    """MCP server for the Workwize Public API."""

    name = "workwize-mcp"
    description = "MCP server providing access to the Workwize Public API"
    version = "0.1.0"

    def __init__(self):
        """Initialize the server with available tools."""
        super().__init__()
        self.tools = self._get_tools()

    def _get_tools(self) -> List[Tool]:
        """Get the list of available tools.

        Returns:
            List of Tool instances.
        """
        return [
            # Orders
            GetOrdersTool(),
            GetOrderTool(),
            GetOrderShipmentsTool(),

            # Assets
            GetAssetsTool(),
            GetWarehousesTool(),

            # Employees
            CreateEmployeeAssetTool(),

            # Offices
            GetOfficesTool(),
        ]

async def start_server():
    """Start the MCP server."""
    try:
        server = WorkwizeMCPServer()
        await server.start()
    except Exception as e:
        logger.error(f"Failed to start server: {e}")
        raise

def main():
    """Main entry point for the server."""
    try:
        asyncio.run(start_server())
    except KeyboardInterrupt:
        logger.info("Server stopped by user")
    except Exception as e:
        logger.error(f"Server error: {e}")
        raise

if __name__ == "__main__":
    main()
