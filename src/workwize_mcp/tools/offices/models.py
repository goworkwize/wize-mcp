"""Models for offices package."""

from typing import List, Optional

from pydantic import BaseModel


class OfficeResponse(BaseModel):
    """Office response model."""

    id: int
    name: str
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = None
    postal_code: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    website: Optional[str] = None
    created_at: str
    updated_at: str
