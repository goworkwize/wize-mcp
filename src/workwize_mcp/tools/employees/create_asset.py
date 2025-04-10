"""Tool for creating employee assets."""
from datetime import datetime
from typing import Any, Dict, List, Optional

from mcp.tools import Tool, ToolCall, ToolResult

from ...api.client import CreateAssetData, WorkwizeClient, WorkwizeAPIError

class CreateEmployeeAssetTool(Tool):
    """Tool for creating an asset for an employee in the Workwize API."""

    name = "create_employee_asset"
    description = "Create an asset for a specific employee"
    parameters = {
        "type": "object",
        "required": [
            "employee_id",
            "name",
            "type",
            "category_id",
            "budget_deduction",
            "date_ordered",
            "currency"
        ],
        "properties": {
            "employee_id": {
                "type": "string",
                "description": "The ID of the employee"
            },
            "name": {
                "type": "string",
                "description": "The name of the asset"
            },
            "type": {
                "type": "string",
                "enum": ["Buy", "Rent"],
                "description": "Whether the asset is purchased or rented"
            },
            "category_id": {
                "type": "integer",
                "description": "The ID of the asset category"
            },
            "budget_deduction": {
                "type": "number",
                "description": "The amount deducted from the budget for this asset"
            },
            "date_ordered": {
                "type": "string",
                "format": "date",
                "description": "The date when the asset was ordered (YYYY-MM-DD)"
            },
            "currency": {
                "type": "string",
                "description": "The currency code (e.g., EUR, USD)"
            },
            "depreciation_months": {
                "type": "integer",
                "description": "Required if type is Buy. Number of months for depreciation"
            },
            "invoice_price": {
                "type": "number",
                "description": "The price listed on the invoice"
            },
            "rent_end_date": {
                "type": "string",
                "format": "date",
                "description": "Required if type is Rent. The date when the rental period ends (YYYY-MM-DD)"
            },
            "note": {
                "type": "string",
                "description": "Additional comments or notes about the asset"
            },
            "tags": {
                "type": "array",
                "items": {"type": "integer"},
                "description": "List of tag IDs associated with the asset"
            },
            "serial_code": {
                "type": "string",
                "description": "The serial number of the asset"
            },
            "image": {
                "type": "array",
                "items": {"type": "string"},
                "description": "Array of URLs for the asset images"
            },
            "warehouse_status": {
                "type": "string",
                "enum": ["Available", "Reserved", "Sold"],
                "description": "The current status of the asset in inventory"
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
            # Parse dates
            date_ordered = datetime.strptime(call.parameters["date_ordered"], "%Y-%m-%d").date()
            rent_end_date = None
            if "rent_end_date" in call.parameters:
                rent_end_date = datetime.strptime(call.parameters["rent_end_date"], "%Y-%m-%d").date()

            # Create asset data
            data = CreateAssetData(
                name=call.parameters["name"],
                type=call.parameters["type"],
                category_id=call.parameters["category_id"],
                budget_deduction=call.parameters["budget_deduction"],
                date_ordered=date_ordered,
                currency=call.parameters["currency"],
                depreciation_months=call.parameters.get("depreciation_months"),
                invoice_price=call.parameters.get("invoice_price"),
                rent_end_date=rent_end_date,
                note=call.parameters.get("note"),
                tags=call.parameters.get("tags"),
                serial_code=call.parameters.get("serial_code"),
                image=call.parameters.get("image"),
                warehouse_status=call.parameters.get("warehouse_status")
            )

            with WorkwizeClient() as client:
                result = client.create_employee_asset(
                    employee_id=call.parameters["employee_id"],
                    data=data
                )

            return ToolResult(
                call,
                result=result,
                display=f"Asset created successfully for employee {call.parameters['employee_id']}"
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
