"""Get assets tool."""

from typing import List, Optional, Literal

from pydantic import BaseModel

from tools.base import BaseTool
from tools.result import ToolResult


class GetAssetsInput(BaseModel):
    """Input for GetAssetsTool."""

    per_page: Optional[int] = 25
    page: Optional[int] = 1
    id: Optional[int] = None
    serial_code: Optional[str] = None
    categories: Optional[List[int]] = None
    employee_id: Optional[int] = None
    employee_email: Optional[str] = None
    external_reference: Optional[str] = None
    search: Optional[str] = None

class GetAssetsTool(BaseTool):
    """Tool for getting assets."""

    @staticmethod
    def name() -> str:
        """The name of the tool."""
        return "get_assets"

    @staticmethod
    def description() -> str:
        """The description of the tool."""
        return "Get a list of assets with filtering options"

    async def execute(self, input_data: GetAssetsInput) -> ToolResult:
        """Execute the tool."""
        input_params = input_data.model_dump(exclude_none=True)
        params = {
            "per_page": input_data.per_page,
            "page": input_data.page,
            "filters": {}
        }
        for key, value in input_params.items():
            if key in ['id', 'per_page', 'page']:
                continue
            params["filters"][key] = value

        response = self.client.get("/assets", params=params)
        return ToolResult(
            data=response,
            error=None
        )
