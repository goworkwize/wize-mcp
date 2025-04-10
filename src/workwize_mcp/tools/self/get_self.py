"""Get self tool."""

from typing import Any, Dict, Optional

from pydantic import BaseModel, Field

from workwize_mcp.tools.base import BaseTool
from workwize_mcp.tools.self.models import SelfResponse


class GetSelfInput(BaseModel):
    """Input for GetSelfTool."""

    pass


class GetSelfTool(BaseTool[GetSelfInput, SelfResponse]):
    """Tool for getting self information."""

    name: str = "get_self"
    description: str = "Get information about the authenticated user"
    input_model: type[GetSelfInput] = GetSelfInput

    def _execute(self, input_data: GetSelfInput) -> SelfResponse:
        """Execute the tool.

        Args:
            input_data: The input data for the tool.

        Returns:
            The response from the tool.
        """
        response = self.client.get("/self")
        return SelfResponse.model_validate(response.json())
