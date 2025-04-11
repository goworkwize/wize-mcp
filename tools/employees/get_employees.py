"""Get employees tool."""

from typing import List, Optional
from datetime import date

from pydantic import BaseModel

from tools.base import BaseTool
from tools.result import ToolResult


class GetEmployeesInput(BaseModel):
    """Input for GetEmployeesTool."""

    page: Optional[int] = 1
    per_page: Optional[int] = 20
    email: Optional[str] = None
    department: Optional[str] = None
    office_id: Optional[int] = None
    manager_id: Optional[int] = None
    start_date_from: Optional[date] = None
    start_date_to: Optional[date] = None
    include: Optional[List[str]] = None


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
            params["email"] = input_data.email
        if input_data.department:
            params["department"] = input_data.department
        if input_data.office_id:
            params["office_id"] = input_data.office_id
        if input_data.manager_id:
            params["manager_id"] = input_data.manager_id
        if input_data.start_date_from:
            params["start_date_from"] = input_data.start_date_from.isoformat()
        if input_data.start_date_to:
            params["start_date_to"] = input_data.start_date_to.isoformat()
        if input_data.include:
            params["include"] = ",".join(input_data.include)

        response = self.client.get("/employees", params=params)
        return ToolResult(
            data=response,
            error=None
        )
