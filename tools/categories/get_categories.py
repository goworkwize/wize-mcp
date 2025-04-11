"""Get categories tool."""

from typing import List

from pydantic import BaseModel

from tools.base import BaseTool


class GetCategoriesInput(BaseModel):
    """Input for GetCategoriesTool."""

    pass


class GetCategoriesTool(BaseTool[GetCategoriesInput, List[dict]]):
    """Tool for getting a list of all available categories."""

    name: str = "get_categories"
    description: str = "Get a list of all available categories"
    endpoint: str = "/categories"
    method: str = "GET"
