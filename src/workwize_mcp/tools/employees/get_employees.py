"""Get employees tool."""

from typing import List, Optional
from datetime import date

from pydantic import BaseModel, EmailStr

from workwize_mcp.tools.base import BaseTool
from workwize_mcp.tools.employees.models import EmployeeResponse


class GetEmployeesInput(BaseModel):
    """Input for GetEmployeesTool."""

    page: Optional[int] = 1
    per_page: Optional[int] = 20
    email: Optional[EmailStr] = None
    department: Optional[str] = None
    office_id: Optional[int] = None
    manager_id: Optional[int] = None
    start_date_from: Optional[date] = None
    start_date_to: Optional[date] = None
    include: Optional[List[str]] = None


class GetEmployeesTool(BaseTool[GetEmployeesInput, List[EmployeeResponse]]):
    """Tool for getting employees."""

    name = "get_employees"
    description = "Get a list of employees with filtering options"
    input_model = GetEmployeesInput
    output_model = List[EmployeeResponse]

    async def _execute(self, input_data: GetEmployeesInput) -> List[EmployeeResponse]:
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

        response = await self.client.get("/employees", params=params)
        return [EmployeeResponse.model_validate(employee) for employee in response["data"]]
