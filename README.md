# Workwize MCP Server

An MCP server implementation for the Workwize Public API.

## Features

- Access to Workwize Public API through MCP tools
- Secure API token handling
- Error handling and logging
- Easy to extend with new tools

## Setup

1. Install the package:
```bash
pip install .
```

2. Create a `.env` file with your Workwize API token:
```bash
WORKWIZE_API_TOKEN=your_token_here
```

## Usage

Start the server:
```bash
workwize-mcp
```

The server provides the following tools:

### Orders

#### get_orders
Get orders from Workwize with optional filters:
- `employee_foreign_id`: Filter orders by employee's foreign ID
- `order_number`: Filter orders by order number
- `per_page`: Number of orders per page

#### get_order
Get a specific order by its ID:
- `order_id`: The ID of the order to retrieve

#### get_order_shipments
Get shipments for a specific order:
- `order_id`: The ID of the order to get shipments for

### Assets

#### get_assets
Get assets with optional filters:
- `employee_id`: Filter assets by employee ID
- `employee_email`: Filter assets by employee email
- `country_availability`: Filter assets by country ISO2 codes (comma-separated)
- `per_page`: Number of assets per page (default: 200)
- `page`: Page number for pagination

#### get_warehouses
Get warehouses with optional country information:
- `include_countries`: Whether to include country information for each warehouse

### Employees

#### create_employee_asset
Create an asset for a specific employee:
- `employee_id`: The ID of the employee
- `name`: The name of the asset
- `type`: Whether the asset is purchased or rented ("Buy" or "Rent")
- `category_id`: The ID of the asset category
- `budget_deduction`: The amount deducted from the budget
- `date_ordered`: The date when the asset was ordered (YYYY-MM-DD)
- `currency`: The currency code (e.g., EUR, USD)
- `depreciation_months`: Required if type is Buy. Number of months for depreciation
- `invoice_price`: The price listed on the invoice
- `rent_end_date`: Required if type is Rent. The rental period end date (YYYY-MM-DD)
- `note`: Additional comments or notes
- `tags`: List of tag IDs
- `serial_code`: The serial number
- `image`: Array of image URLs
- `warehouse_status`: Current inventory status ("Available", "Reserved", "Sold")

### Offices

#### get_offices
Get all offices (no parameters required)

## Development

1. Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

2. Install development dependencies:
```bash
pip install -e ".[dev]"
```

## Adding New Tools

1. Create a new tool class in `src/workwize_mcp/tools/`
2. Add the tool to the `_get_tools()` method in `src/workwize_mcp/server.py`
3. Update the API client in `src/workwize_mcp/api/client.py` if needed

## License

MIT
