"""Get products tool."""

from typing import List, Optional
from enum import Enum

from pydantic import BaseModel

from tools.base import BaseTool
from tools.result import ToolResult

class PossibleStatuses(str, Enum):
    """Possible statuses for the products."""
    ADDED = 'added'
    REMOVED = 'removed'

class PossibleIncludes(str, Enum):
    """Possible includes for the products."""
    CATALOG = 'catalog'
    CATEGORY = 'category'
    SUPPLIER = 'supplier'
    SUPPLIER_WAREHOUSE = 'supplier.warehouse'


class GetProductsInput(BaseModel):
    """Input for GetProductsTool."""

    per_page: Optional[int] = 25
    page: Optional[int] = 1
    department_id: Optional[int] = None
    status: Optional[PossibleStatuses] = None
    country_ids: Optional[List[int]] = None
    search: Optional[str] = None
    category_ids: Optional[List[int]] = None
    second_hand: Optional[bool] = None
    includes: Optional[List[PossibleIncludes]] = ['category', 'supplier', 'countries']

class GetProductsTool(BaseTool):
    """Tool for getting products."""

    @staticmethod
    def name() -> str:
        """The name of the tool."""
        return "get_products"

    @staticmethod
    def description() -> str:
        """The description of the tool."""
        return """
Get a list of products available for the current company with filtering options.

You can filter by:
- department_id: the id of the department
- status: the status of the product
- country_ids: the ids of the countries
- search: a search query to search for a specific product (for example, the name)
- category_ids: the ids of the categories
- second_hand: whether the product is second hand
"""

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
