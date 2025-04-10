"""Tool for retrieving warehouses."""
from typing import Any, Dict

from mcp.tools import Tool, ToolCall, ToolResult

from ...api.client import WorkwizeClient, WorkwizeAPIError

class GetWarehousesTool(Tool):
    """Tool for retrieving warehouses from the Workwize API."""

    name = "get_warehouses"
    description = "Get all warehouses with optional country information"
    parameters = {
        "type": "object",
        "properties": {
            "include_countries": {
                "type": "boolean",
                "description": "Whether to include country information for each warehouse",
                "default": False
            }
        }
    }

    async def __call__(self, call: ToolCall) -> ToolResult:
        """Execute the tool.

        Args:
            call: The tool call containing parameters.

        Returns:
            The tool execution result.
        """
        try:
            include_countries = call.parameters.get("include_countries", False)

            with WorkwizeClient() as client:
                result = client.get_warehouses(include_countries)

            return ToolResult(
                call,
                result=result,
                display="Warehouses retrieved successfully"
            )

        except WorkwizeAPIError as e:
            return ToolResult(
                call,
                error=str(e)
            )
        except Exception as e:
            return ToolResult(
                call,
                error=f"Unexpected error: {str(e)}"
            )
