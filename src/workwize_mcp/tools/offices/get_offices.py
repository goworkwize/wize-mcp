"""Get offices tool."""

from typing import List, Optional

from pydantic import BaseModel

from workwize_mcp.tools.base import BaseTool
from workwize_mcp.tools.offices.models import OfficeResponse


class GetOfficesInput(BaseModel):
    """Input for GetOfficesTool."""

    include: Optional[List[str]] = None


class GetOfficesTool(BaseTool[GetOfficesInput, List[OfficeResponse]]):
    """Tool for getting offices."""

    name = "get_offices"
    description = "Get a list of all offices"
    input_model = GetOfficesInput
    output_model = List[OfficeResponse]

    async def _execute(self, input_data: GetOfficesInput) -> List[OfficeResponse]:
        """Execute the tool."""
        params = {}
        if input_data.include:
            params["include"] = ",".join(input_data.include)

        response = await self.client.get("/offices", params=params)
        return [OfficeResponse.model_validate(office) for office in response["data"]]
