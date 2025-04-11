"""Get employees tool."""

from typing import List, Optional
from datetime import date

from pydantic import BaseModel

from tools.base import BaseTool
from tools.result import ToolResult


class GetOrdersInput(BaseModel):
    """Input for GetOrdersTool."""

    page: Optional[int] = 1
    per_page: Optional[int] = 20
    employee_foreign_id: Optional[str] = None
    number: Optional[str] = None


class GetOrdersTool(BaseTool):
    """Tool for getting orders."""

    @staticmethod
    def name() -> str:
        """The name of the tool."""
        return "get_orders"

    @staticmethod
    def description() -> str:
        """The description of the tool."""
        return "Get a list of orders with filtering options"

    async def execute(self, input_data: GetOrdersInput) -> ToolResult:
        """Execute the tool."""
        params = {
            "page": input_data.page,
            "per_page": input_data.per_page,
        }

        if input_data.employee_foreign_id:
            params["employee_foreign_id"] = input_data.employee_foreign_id
        if input_data.number:
            params["number"] = input_data.number

        response = self.client.get("/orders", params=params)
        return ToolResult(
            data=response,
            error=None
        )
