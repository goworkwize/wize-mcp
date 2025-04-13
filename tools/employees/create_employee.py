"""Create employee tool."""

from typing import Optional
from datetime import date

from pydantic import BaseModel

from tools.base import BaseTool
from tools.result import ToolResult


class CreateEmployeeInput(BaseModel):
    """Input for CreateEmployeeTool."""

    role: str
    given_name: str
    last_name: str
    email: str
    phone_number: str
    is_notified: bool = False
    employment_start_date: Optional[date] = None
    employment_end_date: Optional[date] = None
    personal_email: Optional[str] = None
    personal_phone_number: Optional[str] = None


class CreateEmployeeTool(BaseTool):
    """Tool for creating employees."""

    @staticmethod
    def name() -> str:
        """The name of the tool."""
        return "create_employee"

    @staticmethod
    def description() -> str:
        """The description of the tool."""
        return "Creates an employee with the given data"

    async def execute(self, input_data: CreateEmployeeInput) -> ToolResult:
        """Execute the tool."""
        response = self.client.post("/employees", data=input_data.model_dump())
        return ToolResult(
            data=response,
            error=None
        )
