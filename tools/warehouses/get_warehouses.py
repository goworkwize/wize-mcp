"""Get warehouses tool."""

from typing import List, Optional

from pydantic import BaseModel

from tools.base import BaseTool
from tools.warehouses.models import WarehouseResponse


class GetWarehousesInput(BaseModel):
    """Input for GetWarehousesTool."""

    include: Optional[List[str]] = None


class GetWarehousesTool(BaseTool[GetWarehousesInput, List[WarehouseResponse]]):
    """Tool for getting warehouses."""

    name = "get_warehouses"
    description = "Get a list of available warehouses"
    input_model = GetWarehousesInput
    output_model = List[WarehouseResponse]

    async def _execute(self, input_data: GetWarehousesInput) -> List[WarehouseResponse]:
        """Execute the tool."""
        params = {}
        if input_data.include:
            params["include"] = ",".join(input_data.include)

        response = await self.client.get("/warehouses", params=params)
        return [WarehouseResponse.model_validate(warehouse) for warehouse in response["data"]]
