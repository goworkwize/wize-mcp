"""Get products tool."""

from typing import List, Optional, Literal

from pydantic import BaseModel

from tools.base import BaseTool
from tools.result import ToolResult


class GetProductsInput(BaseModel):
    """Input for GetProductsTool."""

    per_page: Optional[int] = 25
    page: Optional[int] = 1
    department_id: Optional[int] = None
    status: Optional[Literal['added', 'removed']] = None
    country_ids: Optional[List[int]] = None
    search: Optional[str] = None
    category_ids: Optional[List[int]] = None
    second_hand: Optional[bool] = None
    includes: Optional[List[Literal['catalog', 'category', 'supplier', 'supplier.warehouse', 'departments', 'color', 'otherprices', 'oldVariants', 'oldVariants.color', 'oldVariants.otherprices', 'parent', 'children', 'children.otherprices', 'children.color', 'countries', 'children.catalog', 'children.catalog.employers', 'productEmployer', 'variants', 'variants.color', 'budgets', 'variants.countries']]] = ['category', 'supplier', 'countries']

class GetProductsTool(BaseTool):
    """Tool for getting products."""

    @staticmethod
    def name() -> str:
        """The name of the tool."""
        return "get_products"

    @staticmethod
    def description() -> str:
        """The description of the tool."""
        return "Get a list of products with filtering options"

    async def execute(self, input_data: GetProductsInput) -> ToolResult:
        """Execute the tool."""
        params = {
            "includes": input_data.includes,
            "page": input_data.page,
            "per_page": input_data.per_page,
        }
        for key, value in input_data.model_dump().items():
            if key in ['per_page', 'page', 'includes']:
                continue
            params[f"filter[{key}]"] = value

        response = self.client.get("/products", params=params)
        return ToolResult(
            data=response,
            error=None
        )
