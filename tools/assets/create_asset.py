"""Create asset tool."""

from typing import Optional

from pydantic import BaseModel

from tools.base import BaseTool
from tools.assets.models import AssetResponse, CreateAssetInput


class CreateAssetForEmployeeInput(BaseModel):
    """Input for CreateAssetTool."""

    employee_id: int
    asset: CreateAssetInput


class CreateAssetTool(BaseTool[CreateAssetForEmployeeInput, AssetResponse]):
    """Tool for creating an asset for an employee."""

    name = "create_asset"
    description = "Create an asset for an employee"
    input_model = CreateAssetForEmployeeInput
    output_model = AssetResponse

    async def _execute(self, input_data: CreateAssetForEmployeeInput) -> AssetResponse:
        """Execute the tool."""
        response = await self.client.post(
            f"/employees/{input_data.employee_id}/assets",
            json=input_data.asset.model_dump(exclude_none=True),
        )
        return AssetResponse.model_validate(response["data"])
