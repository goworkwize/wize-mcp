"""Models for assets package."""

from typing import List, Optional

from pydantic import BaseModel


class AssetResponse(BaseModel):
    """Asset response model."""

    id: int
    name: str
    type: str
    status: str
    serial_number: Optional[str] = None
    employee_id: Optional[int] = None
    warehouse_id: Optional[int] = None
    created_at: str
    updated_at: str


class CreateAssetInput(BaseModel):
    """Input for creating an asset."""

    name: str
    type: str
    serial_number: Optional[str] = None
    warehouse_id: Optional[int] = None
