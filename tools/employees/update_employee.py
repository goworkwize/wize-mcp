"""Update employees tool."""

from typing import List, Optional, Union
from datetime import date

from pydantic import BaseModel

from tools.base import BaseTool
from tools.result import ToolResult


class Address(BaseModel):
    """Address model."""
    additional_address_line: Optional[str] = None
    address_line_1: Optional[str] = None
    address_line_2: Optional[str] = None
    city: Optional[str] = None
    region: Optional[str] = None
    postal_code: Optional[str] = None
    country_code_iso2: Optional[str] = None


class UpdateEmployeeInput(BaseModel):
    """Input for UpdateEmployeeTool."""

    employee_id: Optional[Union[str, int]] = None
    role: Optional[str] = None
    given_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    phone_number: Optional[str] = None
    foreign_id: Optional[str] = None
    employment_start_date: Optional[date] = None
    employment_end_date: Optional[date] = None
    personal_email: Optional[str] = None
    personal_phone_number: Optional[str] = None
    address: Optional[Address] = None


class UpdateEmployeeTool(BaseTool):
    """Tool for updating employees."""

    @staticmethod
    def name() -> str:
        """The name of the tool."""
        return "update_employee"

    @staticmethod
    def description() -> str:
        """The description of the tool."""
        return "Updates an employee with the given data"

    async def execute(self, input_data: UpdateEmployeeInput) -> ToolResult:
        """Execute the tool."""
        employee_id = input_data.employee_id
        del input_data.employee_id

        response = self.client.patch(f"/employees/{employee_id}", data=input_data.model_dump())
        return ToolResult(
            data=response,
            error=None
        )
