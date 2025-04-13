"""Create employees address tool."""

from typing import Optional

from pydantic import BaseModel, Field

from tools.base import BaseTool
from tools.result import ToolResult


class CreateEmployeeAddressInput(BaseModel):
    """Address model."""

    employee_id: int
    company_name: Optional[str] = None
    address_line_1: str = Field(..., max_length=255)
    address_line_2: Optional[str] = None
    additional_address_line: Optional[str] = Field(None, max_length=255)
    city: str = Field(..., max_length=255)
    region: Optional[str] = None
    postal_code: str = Field(..., max_length=20)
    country_id: int
    phone_number: Optional[str] = None
    email: Optional[str] = None
    name: Optional[str] = None
    last_name: Optional[str] = None
    postcode: Optional[str] = None
    country_code: Optional[str] = None
    country: Optional[int] = None


class CreateEmployeeAddressTool(BaseTool):
    """Tool for creating employees address."""

    @staticmethod
    def name() -> str:
        """The name of the tool."""
        return "create_employee_address"

    @staticmethod
    def description() -> str:
        """The description of the tool."""
        return "Creates an employee address with the given data"

    async def execute(self, input_data: CreateEmployeeAddressInput) -> ToolResult:
        """Execute the tool."""
        employee_id = input_data.employee_id
        del input_data.employee_id

        response = self.client.post(f"/employees/{employee_id}/addresses", data=input_data.model_dump())
        return ToolResult(
            data=response,
            error=None
        )
