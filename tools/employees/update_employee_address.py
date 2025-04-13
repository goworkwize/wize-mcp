"""Update employees address tool."""

from typing import List, Optional, Union
from datetime import date

from pydantic import BaseModel

from tools.base import BaseTool
from tools.result import ToolResult


class UpdateEmployeeAddressInput(BaseModel):
    """Address model."""

    employee_id: int
    address_id: int
    company_name: Optional[str] = None
    address_line_1: Optional[str] = None
    address_line_2: Optional[str] = None
    additional_address_line: Optional[str] = None
    city: Optional[str] = None
    region: Optional[str] = None
    postal_code: Optional[str] = None
    country_id: Optional[int] = None
    phone_number: Optional[str] = None
    email: Optional[str] = None


class UpdateEmployeeAddressTool(BaseTool):
    """Tool for updating employees address."""

    @staticmethod
    def name() -> str:
        """The name of the tool."""
        return "update_employee_address"

    @staticmethod
    def description() -> str:
        """The description of the tool."""
        return "Updates an employee address with the given data"

    async def execute(self, input_data: UpdateEmployeeAddressInput) -> ToolResult:
        """Execute the tool."""
        employee_id = input_data.employee_id
        address_id = input_data.address_id
        del input_data.employee_id
        del input_data.address_id

        response = self.client.patch(f"/employees/{employee_id}/addresses/{address_id}", data=input_data.model_dump())
        return ToolResult(
            data=response,
            error=None
        )
