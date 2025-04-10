"""Tool for retrieving all orders."""
from typing import Any, Dict, Optional

from mcp.tools import Tool, ToolCall, ToolResult

from ...api.client import OrderFilter, WorkwizeClient, WorkwizeAPIError

class GetOrdersTool(Tool):
    """Tool for retrieving orders from the Workwize API."""

    name = "get_orders"
    description = "Get all orders with optional filters for employee foreign ID or order number"
    parameters = {
        "type": "object",
        "properties": {
            "employee_foreign_id": {
                "type": "string",
                "description": "Filter orders by employee's foreign ID"
            },
            "order_number": {
                "type": "string",
                "description": "Filter orders by order number"
            },
            "per_page": {
                "type": "integer",
                "description": "Number of orders per page"
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
            filters = OrderFilter(
                employee_foreign_id=call.parameters.get("employee_foreign_id"),
                number=call.parameters.get("order_number"),
                per_page=call.parameters.get("per_page")
            )

            with WorkwizeClient() as client:
                result = client.get_orders(filters)

            return ToolResult(
                call,
                result=result,
                display="Orders retrieved successfully"
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
