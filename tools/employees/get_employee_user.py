"""Get employees tool."""

from typing import Union

from pydantic import BaseModel

from tools.base import BaseTool
from tools.result import ToolResult


class GetEmployeeUserInput(BaseModel):
    """Input for GetEmployeeUserTool."""

    employee_id: Union[int, str]


class GetEmployeeUserTool(BaseTool):
    """Tool for getting employee user."""

    @staticmethod
    def name() -> str:
        """The name of the tool."""
        return "get_employee_user"

    @staticmethod
    def description() -> str:
        """The description of the tool."""
        return "Get the user associated with the employee"

    async def execute(self, input_data: GetEmployeeUserInput) -> ToolResult:
        """Execute the tool."""
        response = self.client.get(f"/employees/{input_data.employee_id}")
        return ToolResult(
            data=response,
            error=None
        )
