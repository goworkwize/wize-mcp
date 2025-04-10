"""Workwize API client module."""
from typing import Any, Dict, Optional
from datetime import date

import httpx
from pydantic import BaseModel

from ..config import config

class WorkwizeAPIError(Exception):
    """Custom exception for Workwize API errors."""
    pass

class OrderFilter(BaseModel):
    """Model for order filter parameters."""
    employee_foreign_id: Optional[str] = None
    number: Optional[str] = None
    per_page: Optional[int] = None

class AssetFilter(BaseModel):
    """Model for asset filter parameters."""
    employee_id: Optional[str] = None
    employee_email: Optional[str] = None
    country_availability: Optional[str] = None
    per_page: Optional[int] = 200
    page: Optional[int] = None

class CreateAssetData(BaseModel):
    """Model for creating an asset."""
    name: str
    type: str  # "Buy" or "Rent"
    category_id: int
    budget_deduction: float
    date_ordered: date
    currency: str
    depreciation_months: Optional[int] = None
    invoice_price: Optional[float] = None
    rent_end_date: Optional[date] = None
    note: Optional[str] = None
    tags: Optional[list[int]] = None
    serial_code: Optional[str] = None
    image: Optional[list[str]] = None
    warehouse_status: Optional[str] = None

class CreateAddressData(BaseModel):
    """Model for creating an address."""
    city: str
    postal_code: str
    country_id: int
    address_line_1: Optional[str] = None
    address_line_2: Optional[str] = None
    additional_address_line: Optional[str] = None
    region: Optional[str] = None
    phone_number: Optional[str] = None

class WorkwizeClient:
    """Client for interacting with the Workwize Public API."""

    def __init__(self, api_token: Optional[str] = None):
        """Initialize the client.

        Args:
            api_token: Optional API token. If not provided, uses the one from config.
        """
        self.api_token = api_token or config.api_token
        self.base_url = config.api_base_url
        self.client = httpx.Client(
            base_url=self.base_url,
            headers={
                "Authorization": f"Bearer {self.api_token}",
                "Accept": "application/json",
            },
            timeout=30.0
        )

    def _handle_response(self, response: httpx.Response) -> Dict[str, Any]:
        """Handle API response and errors.

        Args:
            response: The API response to handle.

        Returns:
            The JSON response data.

        Raises:
            WorkwizeAPIError: If the API returns an error.
        """
        try:
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            error_data = e.response.json() if e.response.content else {}
            raise WorkwizeAPIError(
                f"API request failed: {e.response.status_code} - {error_data}"
            ) from e
        except Exception as e:
            raise WorkwizeAPIError(f"Unexpected error: {str(e)}") from e

    # Orders
    def get_orders(self, filters: Optional[OrderFilter] = None) -> Dict[str, Any]:
        """Get all orders with optional filters.

        Args:
            filters: Optional filters for the orders query.

        Returns:
            The orders data.
        """
        params = {}
        if filters:
            if filters.employee_foreign_id:
                params["filter[employee_foreign_id]"] = filters.employee_foreign_id
            if filters.number:
                params["filter[number]"] = filters.number
            if filters.per_page:
                params["per_page"] = filters.per_page

        response = self.client.get("/orders", params=params)
        return self._handle_response(response)

    def get_order(self, order_id: str) -> Dict[str, Any]:
        """Get a specific order by ID.

        Args:
            order_id: The ID of the order to retrieve.

        Returns:
            The order data.
        """
        response = self.client.get(f"/orders/{order_id}")
        return self._handle_response(response)

    def get_order_shipments(self, order_id: str) -> Dict[str, Any]:
        """Get shipments for a specific order.

        Args:
            order_id: The ID of the order to get shipments for.

        Returns:
            The order shipments data.
        """
        response = self.client.get(f"/orders/{order_id}/shipments")
        return self._handle_response(response)

    # Assets
    def get_assets(self, filters: Optional[AssetFilter] = None) -> Dict[str, Any]:
        """Get all assets with optional filters.

        Args:
            filters: Optional filters for the assets query.

        Returns:
            The assets data.
        """
        params = {}
        if filters:
            if filters.employee_id:
                params["filter[employeeId]"] = filters.employee_id
            if filters.employee_email:
                params["filter[employeeEmail]"] = filters.employee_email
            if filters.country_availability:
                params["filter[country_availability]"] = filters.country_availability
            if filters.per_page:
                params["per_page"] = filters.per_page
            if filters.page:
                params["page"] = filters.page

        response = self.client.get("/assets", params=params)
        return self._handle_response(response)

    def create_employee_asset(self, employee_id: str, data: CreateAssetData) -> Dict[str, Any]:
        """Create an asset for an employee.

        Args:
            employee_id: The ID of the employee.
            data: The asset data.

        Returns:
            The created asset data.
        """
        response = self.client.post(
            f"/employees/{employee_id}/assets",
            json={
                "name": data.name,
                "type": data.type,
                "category_id": data.category_id,
                "budget_deduction": data.budget_deduction,
                "date_ordered": data.date_ordered.isoformat(),
                "currency": data.currency,
                "depreciation_months": data.depreciation_months,
                "invoice_price": data.invoice_price,
                "rent_end_date": data.rent_end_date.isoformat() if data.rent_end_date else None,
                "note": data.note,
                "tags": data.tags,
                "serial_code": data.serial_code,
                "image": data.image,
                "warehouse_status": data.warehouse_status,
            }
        )
        return self._handle_response(response)

    def get_warehouses(self, include_countries: bool = False) -> Dict[str, Any]:
        """Get all warehouses.

        Args:
            include_countries: Whether to include country information.

        Returns:
            The warehouses data.
        """
        params = {"include": "countries"} if include_countries else {}
        response = self.client.get("/warehouses", params=params)
        return self._handle_response(response)

    def get_offices(self) -> Dict[str, Any]:
        """Get all offices.

        Returns:
            The offices data.
        """
        response = self.client.get("/offices")
        return self._handle_response(response)

    # Self
    def get_self(self) -> Dict[str, Any]:
        """Get authenticated user information.

        Returns:
            The authenticated user data.
        """
        response = self.client.get("/self")
        return self._handle_response(response)

    # Addresses
    def get_employee_addresses(self, employee_id: str) -> Dict[str, Any]:
        """Get addresses for an employee.

        Args:
            employee_id: The ID of the employee.

        Returns:
            The employee addresses data.
        """
        response = self.client.get(f"/employees/{employee_id}/addresses")
        return self._handle_response(response)

    def create_employee_address(self, employee_id: str, data: CreateAddressData) -> Dict[str, Any]:
        """Create an address for an employee.

        Args:
            employee_id: The ID of the employee.
            data: The address data.

        Returns:
            The created address data.
        """
        response = self.client.post(
            f"/employees/{employee_id}/addresses",
            json={
                "city": data.city,
                "postal_code": data.postal_code,
                "country_id": data.country_id,
                "address_line_1": data.address_line_1,
                "address_line_2": data.address_line_2,
                "additional_address_line": data.additional_address_line,
                "region": data.region,
                "phone_number": data.phone_number,
            }
        )
        return self._handle_response(response)

    def __enter__(self):
        """Context manager entry."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.client.close()
