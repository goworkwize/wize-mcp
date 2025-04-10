"""Update employee address tool."""

from pydantic import BaseModel

from workwize_mcp.tools.base import BaseTool
from workwize_mcp.tools.employees.models import AddressInput, AddressResponse


class UpdateEmployeeAddressInput(BaseModel):
    """Input for UpdateEmployeeAddressTool."""

    employee_id: int
    address: AddressInput


class UpdateEmployeeAddressTool(BaseTool[UpdateEmployeeAddressInput, AddressResponse]):
    """Tool for creating/updating employee address."""

    name = "update_employee_address"
    description = "Create/update employee address"
    input_model = UpdateEmployeeAddressInput
    output_model = AddressResponse

    async def _execute(self, input_data: UpdateEmployeeAddressInput) -> AddressResponse:
        """Execute the tool."""
        response = await self.client.post(
            f"/employees/{input_data.employee_id}/addresses",
            json=input_data.address.model_dump(exclude_none=True),
        )
        return AddressResponse.model_validate(response["data"])
