"""Get employees tool."""

from typing import List, Optional, Literal

from pydantic import BaseModel

from tools.base import BaseTool
from tools.result import ToolResult

class GetEmployeesInput(BaseModel):
    """Input for GetEmployeesTool."""

    page: Optional[int] = 1
    per_page: Optional[int] = 20
    email: Optional[str] = None
    include: Optional[List[Literal['user', 'assets', 'department', 'orders']]] = None


class GetEmployeesTool(BaseTool):
    """Tool for getting employees."""

    @staticmethod
    def name() -> str:
        """The name of the tool."""
        return "get_employees"

    @staticmethod
    def description() -> str:
        """The description of the tool."""
        return "Get a list of employees with filtering options"

    async def execute(self, input_data: GetEmployeesInput) -> ToolResult:
        """Execute the tool."""
        params = {
            "page": input_data.page,
            "per_page": input_data.per_page,
            "filters": {}
        }

        if input_data.email:
            params["filters"]["user.email"] = input_data.email
        if input_data.include:
            params["include"] = ",".join(input_data.include)

        response = self.client.get("/employees", params=params)
        return ToolResult(
            data=response,
            error=None
        )
