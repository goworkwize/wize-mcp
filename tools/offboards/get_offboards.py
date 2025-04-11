"""Get offboards tool."""

from typing import List, Optional

from pydantic import BaseModel, Field

from tools.base import BaseTool


class GetOffboardsInput(BaseModel):
    """Input for GetOffboardsTool."""

    employee_foreign_id: Optional[str] = Field(None, description="Filter by employee's HRIS foreign ID")
    employee_id: Optional[int] = Field(None, description="Filter by employee's ID")
    status: Optional[str] = Field(None, description="Filter by status (comma-separated for multiple)")
    search: Optional[str] = Field(None, description="Search term for employee name, company name or ID")


class GetOffboardsTool(BaseTool[GetOffboardsInput, List[dict]]):
    """Tool for getting offboarding requests."""

    name: str = "get_offboards"
    description: str = "Get a list of offboarding requests with optional filters"
    endpoint: str = "/offboards"
    method: str = "GET"

    def _prepare_query_params(self, input_data: GetOffboardsInput) -> dict:
        """Prepare the query parameters for the request."""
        params = {}
        if input_data.employee_foreign_id:
            params["filter[employee_foreign_id]"] = input_data.employee_foreign_id
        if input_data.employee_id:
            params["filter[employee_id]"] = str(input_data.employee_id)
        if input_data.status:
            params["filter[status]"] = input_data.status
        if input_data.search:
            params["filter[search]"] = input_data.search
        return params
