"""Get order products tool."""

from typing import List, Optional
from datetime import date

from pydantic import BaseModel

from tools.base import BaseTool
from tools.result import ToolResult


class GetOrderProductsInput(BaseModel):
    """Input for GetOrderProductsTool."""
    order_number: Optional[str] = None


class GetOrderProductsTool(BaseTool):
    """Tool for getting order products."""

    @staticmethod
    def name() -> str:
        """The name of the tool."""
        return "get_order_products"

    @staticmethod
    def description() -> str:
        """The description of the tool."""
        return "Get a list of products for a specific order"

    async def execute(self, input_data: GetOrderProductsInput) -> ToolResult:
        """Execute the tool."""
        response = self.client.get(f'/orders/{input_data.order_number}/products')
        return ToolResult(
            data=response,
            error=None
        )
