"""Get offboards tool."""

from typing import List, Optional, Literal

from pydantic import BaseModel

from tools.base import BaseTool
from tools.result import ToolResult


class GetOffboardsInput(BaseModel):
    """Input for GetOffboardsTool."""

    per_page: Optional[int] = 25
    page: Optional[int] = 1
    search: Optional[str] = None
    status: Optional[Literal['request_received','request_being_processed','pending_employee_response','pending_pick_up_date_choosen','pick_up_in_progress','pick_up_drop_off_in_progress','pick_up_failed','offboard_cancelled','offboard_completed','offboard_failed_pickup_failed','offboard_failed_no_answer','postponed_by_user','pending_employee_response1','pending_employee_response2','pending_employee_response3','pending_employee_response4','details_confirmed','in_transit_to_warehouse','manual_snippet_sent','manual_snippet_sent2','scheduled','being_stocked_at_warehouse']] = None
    employee_id: Optional[int] = None
    employee_foreign_id: Optional[str] = None

class GetOffboardsTool(BaseTool):
    """Tool for getting offboards."""

    @staticmethod
    def name() -> str:
        """The name of the tool."""
        return "get_offboards"

    @staticmethod
    def description() -> str:
        """The description of the tool."""
        return "Get a list of offboards with filtering options"

    async def execute(self, input_data: GetOffboardsInput) -> ToolResult:
        """Execute the tool."""
        params = {
            "status": input_data.status,
            "employee_id": input_data.employee_id,
            "employee_foreign_id": input_data.employee_foreign_id,
            "search": input_data.search,
            "page": input_data.page,
            "per_page": input_data.per_page,
        }

        response = self.client.get("/offboards", params=params)
        return ToolResult(
            data=response,
            error=None
        )
