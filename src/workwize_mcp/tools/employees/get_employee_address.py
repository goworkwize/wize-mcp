"""Get employee address tool."""

from typing import Optional

from pydantic import BaseModel

from workwize_mcp.tools.base import BaseTool
from workwize_mcp.tools.employees.models import AddressResponse


class GetEmployeeAddressInput(BaseModel):
    """Input for GetEmployeeAddressTool."""

    employee_id: int


class GetEmployeeAddressTool(BaseTool[GetEmployeeAddressInput, AddressResponse]):
    """Tool for getting employee address."""

    name = "get_employee_address"
    description = "Get employee address"
    input_model = GetEmployeeAddressInput
    output_model = AddressResponse

    async def _execute(self, input_data: GetEmployeeAddressInput) -> AddressResponse:
        """Execute the tool."""
        response = await self.client.get(f"/employees/{input_data.employee_id}/addresses")
        return AddressResponse.model_validate(response["data"])
