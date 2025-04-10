"""Tool for retrieving shipments for a specific order."""
from typing import Any, Dict

from mcp.tools import Tool, ToolCall, ToolResult

from ...api.client import WorkwizeClient, WorkwizeAPIError

class GetOrderShipmentsTool(Tool):
    """Tool for retrieving shipments for a specific order from the Workwize API."""

    name = "get_order_shipments"
    description = "Get all shipments for a specific order"
    parameters = {
        "type": "object",
        "required": ["order_id"],
        "properties": {
            "order_id": {
                "type": "string",
                "description": "The ID of the order to get shipments for"
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
            order_id = call.parameters["order_id"]

            with WorkwizeClient() as client:
                result = client.get_order_shipments(order_id)

            return ToolResult(
                call,
                result=result,
                display=f"Shipments for order {order_id} retrieved successfully"
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
