"""Get categories tool."""

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
        response = self.client.get("/offices", params=input_data.model_dump())
        return ToolResult(
            data=response,
            error=None
        )
