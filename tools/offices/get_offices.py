"""Get offices tool."""

from typing import Optional

from pydantic import BaseModel

from tools.base import BaseTool
from tools.result import ToolResult

class GetOfficesInput(BaseModel):
    """Input for GetOfficesTool."""

    page: Optional[int] = 1
    limit: Optional[int] = 20
    name: Optional[str] = None

class GetOfficesTool(BaseTool):
    """Tool for getting offices."""

    @staticmethod
    def name() -> str:
        """The name of the tool."""
        return "get_offices"

    @staticmethod
    def description() -> str:
        """The description of the tool."""
        return "Get a list of all available offices"

    async def execute(self, input_data: GetOfficesInput) -> ToolResult:
        """Execute the tool."""
        params = {
            "per_page": input_data.per_page,
            "page": input_data.page,
            "filters": {}
        }
        for key, value in input_data.model_dump().items():
            if key in ['per_page', 'page']:
                continue
            params["filters"][key] = value

        response = self.client.get("/offices", params=params)
        return ToolResult(
            data=response,
            error=None
        )
