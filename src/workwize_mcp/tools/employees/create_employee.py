"""Create employee tool."""

from workwize_mcp.tools.base import BaseTool
from workwize_mcp.tools.employees.models import CreateEmployeeInput, EmployeeResponse


class CreateEmployeeTool(BaseTool[CreateEmployeeInput, EmployeeResponse]):
    """Tool for creating a new employee."""

    name = "create_employee"
    description = "Create a new employee with detailed information"
    input_model = CreateEmployeeInput
    output_model = EmployeeResponse

    async def _execute(self, input_data: CreateEmployeeInput) -> EmployeeResponse:
        """Execute the tool."""
        response = await self.client.post(
            "/employees",
            json=input_data.model_dump(exclude_none=True),
        )
        return EmployeeResponse.model_validate(response["data"])
