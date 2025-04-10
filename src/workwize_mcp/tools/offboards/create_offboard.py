"""Create offboard tool."""

from typing import List

from pydantic import BaseModel, Field

from workwize_mcp.tools.base import BaseTool


class CreateOffboardInput(BaseModel):
    """Input for CreateOffboardTool."""

    employee_id: int = Field(..., description="The ID of the employee being offboarded")
    destination_type: str = Field(..., description="The type of destination (warehouse or office)")
    destination_code: str = Field(..., description="The code of the destination (warehouse code or office ID)")
    assets: List[int] = Field(..., description="List of asset IDs to be included in the offboarding")


class CreateOffboardTool(BaseTool[CreateOffboardInput, dict]):
    """Tool for creating a new offboarding request."""

    name: str = "create_offboard"
    description: str = "Create a new offboarding request"
    endpoint: str = "/requests/offboards"
    method: str = "POST"

    def _prepare_body(self, input_data: CreateOffboardInput) -> dict:
        """Prepare the request body."""
        return input_data.model_dump()
