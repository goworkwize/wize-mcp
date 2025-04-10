"""Self models."""

from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field


class Role(BaseModel):
    """Role model."""

    id: int
    created_at: datetime
    updated_at: datetime
    name: str
    pivot: dict


class Invite(BaseModel):
    """Invite model."""

    id: int
    email: str
    token: str
    status: str
    invited_by: int
    department_id: Optional[int] = None
    invitee_role_id: int
    created_at: datetime
    updated_at: datetime
    queue_status: int


class SelfResponse(BaseModel):
    """Self response model."""

    id: int
    name: str
    last_name: str
    gender: str
    first_login: int
    email: str
    personal_email: Optional[str] = None
    phone_number: str
    personal_phone_number: Optional[str] = None
    email_verified_at: Optional[datetime] = None
    created_at: datetime
    updated_at: datetime
    sub: Optional[str] = None
    read_privacy: int
    prefix: Optional[str] = None
    deleted_at: Optional[datetime] = None
    deactivated_at: Optional[datetime] = None
    invite: Invite
    roles: List[Role]
