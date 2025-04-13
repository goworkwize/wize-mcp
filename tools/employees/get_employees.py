"""Get employees tool."""

from typing import List, Optional
from enum import Enum
from pydantic import BaseModel

from tools.base import BaseTool
from tools.result import ToolResult

class PossibleIncludes(str, Enum):
    """Possible includes for the get employees tool."""
    USER = 'user'
    ASSETS = 'assets'
    DEPARTMENT = 'department'
    ORDERS = 'orders'

class GetEmployeesInput(BaseModel):
    """Input for GetEmployeesTool."""

    page: Optional[int] = 1
    per_page: Optional[int] = 20
    email: Optional[str] = None
    include: Optional[List[PossibleIncludes]] = None


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
        }

        if input_data.email:
            params["filter[user.email]"] = input_data.email
        if input_data.include:
            params["include"] = ",".join(input_data.include)

        print(params)
        response = self.client.get("/employees", params=params)
        return ToolResult(
            data=response,
            error=None
        )
