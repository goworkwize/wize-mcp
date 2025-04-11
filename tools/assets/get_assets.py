"""Get assets tool."""

from typing import List, Optional

from pydantic import BaseModel

from tools.base import BaseTool
from tools.assets.models import AssetResponse


class GetAssetsInput(BaseModel):
    """Input for GetAssetsTool."""

    page: Optional[int] = 1
    per_page: Optional[int] = 20
    status: Optional[str] = None
    type: Optional[str] = None
    employee_id: Optional[int] = None
    warehouse_id: Optional[int] = None
    include: Optional[List[str]] = None


class GetAssetsTool(BaseTool[GetAssetsInput, List[AssetResponse]]):
    """Tool for getting assets."""

    name = "get_assets"
    description = "Get a paginated list of all assets with filtering options"
    input_model = GetAssetsInput
    output_model = List[AssetResponse]

    async def _execute(self, input_data: GetAssetsInput) -> List[AssetResponse]:
        """Execute the tool."""
        params = {
            "page": input_data.page,
            "per_page": input_data.per_page,
        }

        if input_data.status:
            params["status"] = input_data.status
        if input_data.type:
            params["type"] = input_data.type
        if input_data.employee_id:
            params["employee_id"] = input_data.employee_id
        if input_data.warehouse_id:
            params["warehouse_id"] = input_data.warehouse_id
        if input_data.include:
            params["include"] = ",".join(input_data.include)

        response = await self.client.get("/assets", params=params)
        return [AssetResponse.model_validate(asset) for asset in response["data"]]
