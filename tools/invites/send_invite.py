"""Send invite tool."""

from pydantic import BaseModel, Field

from tools.base import BaseTool


class SendInviteInput(BaseModel):
    """Input for SendInviteTool."""

    email: str = Field(..., description="The email address to send the invite to")


class SendInviteTool(BaseTool[SendInviteInput, dict]):
    """Tool for sending invites to employees."""

    name: str = "send_invite"
    description: str = "Send invites to employees that are already created in the platform"
    endpoint: str = "/invites"
    method: str = "POST"

    def _prepare_body(self, input_data: SendInviteInput) -> dict:
        """Prepare the request body."""
        return input_data.model_dump()
