"""Models for employees package."""

from typing import List, Optional
from datetime import date

from pydantic import BaseModel, EmailStr


class AddressInput(BaseModel):
    """Input for creating/updating an address."""

    street: str
    city: str
    state: Optional[str] = None
    country: str
    postal_code: str


class AddressResponse(BaseModel):
    """Address response model."""

    id: int
    street: str
    city: str
    state: Optional[str] = None
    country: str
    postal_code: str
    created_at: str
    updated_at: str


class CreateEmployeeInput(BaseModel):
    """Input for creating an employee."""

    first_name: str
    last_name: str
    email: EmailStr
    phone: Optional[str] = None
    job_title: Optional[str] = None
    department: Optional[str] = None
    start_date: Optional[date] = None
    office_id: Optional[int] = None
    manager_id: Optional[int] = None


class EmployeeResponse(BaseModel):
    """Employee response model."""

    id: int
    first_name: str
    last_name: str
    email: EmailStr
    phone: Optional[str] = None
    job_title: Optional[str] = None
    department: Optional[str] = None
    start_date: Optional[date] = None
    office_id: Optional[int] = None
    manager_id: Optional[int] = None
    created_at: str
    updated_at: str
