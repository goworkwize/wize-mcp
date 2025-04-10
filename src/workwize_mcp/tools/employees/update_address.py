"""Update employee address tool."""

from typing import Optional

from pydantic import BaseModel, Field

from workwize_mcp.tools.base import BaseTool


class UpdateEmployeeAddressInput(BaseModel):
    """Input for UpdateEmployeeAddressTool."""

    employee_id: int = Field(..., description="The ID of the employee")
    address_id: int = Field(..., description="The ID of the address to update")
    address_line_1: Optional[str] = Field(None, description="The first line of the address")
    address_line_2: Optional[str] = Field(None, description="The second line of the address")
    postal_code: Optional[str] = Field(None, description="The postal code")
    city: Optional[str] = Field(None, description="The city")
    region: Optional[str] = Field(None, description="The region/state")
    country_id: Optional[int] = Field(None, description="The ID of the country")


class UpdateEmployeeAddressTool(BaseTool[UpdateEmployeeAddressInput, dict]):
    """Tool for updating an employee's address."""

    name: str = "update_employee_address"
    description: str = "Update an employee's address information"
    endpoint: str = "/employees/{employee_id}/addresses/{address_id}"
    method: str = "PATCH"

    def _prepare_url(self, input_data: UpdateEmployeeAddressInput) -> str:
        """Prepare the URL for the request."""
        return self.endpoint.format(
            employee_id=input_data.employee_id,
            address_id=input_data.address_id,
        )

    def _prepare_body(self, input_data: UpdateEmployeeAddressInput) -> dict:
        """Prepare the request body."""
        return input_data.model_dump(exclude={"employee_id", "address_id"}, exclude_none=True)
