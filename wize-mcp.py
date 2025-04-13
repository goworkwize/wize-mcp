from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

from tools.self import GetSelfTool

from tools.assets import GetAssetsTool
from tools.assets.get_assets import GetAssetsInput

from tools.categories import GetCategoriesTool

from tools.offices import GetOfficesTool
from tools.offices.get_offices import GetOfficesInput

from tools.employees import GetEmployeesTool, CreateEmployeeTool, GetEmployeeUserTool, GetEmployeeAddressesTool, UpdateEmployeeTool, UpdateEmployeeAddressTool, CreateEmployeeAddressTool, CreateEmployeeAssetTool
from tools.employees.get_employees import GetEmployeesInput
from tools.employees.create_employee import CreateEmployeeInput
from tools.employees.get_employee_user import GetEmployeeUserInput
from tools.employees.get_employee_addresses import GetEmployeeAddressesInput
from tools.employees.update_employee import UpdateEmployeeInput
from tools.employees.update_employee_address import UpdateEmployeeAddressInput
from tools.employees.create_employee_address import CreateEmployeeAddressInput
from tools.employees.create_employee_asset import CreateEmployeeAssetInput

from tools.invites import CreateInviteTool
from tools.invites.create_invite import CreateInviteInput

from tools.offboards import GetOffboardsTool
from tools.offboards.get_offboards import GetOffboardsInput

from tools.orders import GetOrdersTool, GetOrderProductsTool, GetOrderShipmentsTool
from tools.orders.get_orders import GetOrdersInput
from tools.orders.get_order_products import GetOrderProductsInput
from tools.orders.get_order_shipments import GetOrderShipmentsInput

from tools.products import GetProductsTool
from tools.products.get_products import GetProductsInput

from tools.warehouses import GetWarehousesTool

import dotenv
import asyncio

dotenv.load_dotenv()

# Initialize FastMCP server
mcp = FastMCP("wize-mcp")

@mcp.tool(
    name=GetSelfTool.name(),
    description=GetSelfTool.description()
)
async def get_self():
    result = await GetSelfTool().execute()
    return result.to_response()

@mcp.tool(
    name=GetEmployeesTool.name(),
    description=GetEmployeesTool.description()
)
async def get_employees(input_data: GetEmployeesInput):
    result = await GetEmployeesTool().execute(input_data)
    return result.to_response()

@mcp.tool(
    name=GetOrdersTool.name(),
    description=GetOrdersTool.description()
)
async def get_orders(input_data: GetOrdersInput):
    result = await GetOrdersTool().execute(input_data)
    return result.to_response()

@mcp.tool(
    name=GetOrderProductsTool.name(),
    description=GetOrderProductsTool.description()
)
async def get_order_products(input_data: GetOrderProductsInput):
    result = await GetOrderProductsTool().execute(input_data)
    return result.to_response()

@mcp.tool(
    name=GetOrderShipmentsTool.name(),
    description=GetOrderShipmentsTool.description()
)
async def get_order_shipments(input_data: GetOrderShipmentsInput):
    result = await GetOrderShipmentsTool().execute(input_data)
    return result.to_response()

@mcp.tool(
    name=CreateEmployeeTool.name(),
    description=CreateEmployeeTool.description()
)
async def create_employee(input_data: CreateEmployeeInput):
    result = await CreateEmployeeTool().execute(input_data)
    return result.to_response()

@mcp.tool(
    name=GetEmployeeUserTool.name(),
    description=GetEmployeeUserTool.description()
)
async def get_employee_user(input_data: GetEmployeeUserInput):
    result = await GetEmployeeUserTool().execute(input_data)
    return result.to_response()

@mcp.tool(
    name=GetCategoriesTool.name(),
    description=GetCategoriesTool.description()
)
async def get_categories():
    result = await GetCategoriesTool().execute()
    return result.to_response()

@mcp.tool(
    name=GetOfficesTool.name(),
    description=GetOfficesTool.description()
)
async def get_offices(input_data: GetOfficesInput):
    result = await GetOfficesTool().execute(input_data)
    return result.to_response()

@mcp.tool(
    name=GetWarehousesTool.name(),
    description=GetWarehousesTool.description()
)
async def get_warehouses():
    result = await GetWarehousesTool().execute()
    return result.to_response()

@mcp.tool(
    name=GetProductsTool.name(),
    description=GetProductsTool.description()
)
async def get_products(input_data: GetProductsInput):
    result = await GetProductsTool().execute(input_data)
    return result.to_response()

@mcp.tool(
    name=GetOffboardsTool.name(),
    description=GetOffboardsTool.description()
)
async def get_offboards(input_data: GetOffboardsInput):
    result = await GetOffboardsTool().execute(input_data)
    return result.to_response()

@mcp.tool(
    name=GetAssetsTool.name(),
    description=GetAssetsTool.description()
)
async def get_assets(input_data: GetAssetsInput):
    result = await GetAssetsTool().execute(input_data)
    return result.to_response()

@mcp.tool(
    name=GetEmployeeAddressesTool.name(),
    description=GetEmployeeAddressesTool.description()
)
async def get_employee_addresses(input_data: GetEmployeeAddressesInput):
    result = await GetEmployeeAddressesTool().execute(input_data)
    return result.to_response()

@mcp.tool(
    name=UpdateEmployeeTool.name(),
    description=UpdateEmployeeTool.description()
)
async def update_employee(input_data: UpdateEmployeeInput):
    result = await UpdateEmployeeTool().execute(input_data)
    return result.to_response()

@mcp.tool(
    name=UpdateEmployeeAddressTool.name(),
    description=UpdateEmployeeAddressTool.description()
)
async def update_employee_address(input_data: UpdateEmployeeAddressInput):
    result = await UpdateEmployeeAddressTool().execute(input_data)
    return result.to_response()

@mcp.tool(
    name=CreateEmployeeAddressTool.name(),
    description=CreateEmployeeAddressTool.description()
)
async def create_employee_address(input_data: CreateEmployeeAddressInput):
    result = await CreateEmployeeAddressTool().execute(input_data)
    return result.to_response()

@mcp.tool(
    name=CreateEmployeeAssetTool.name(),
    description=CreateEmployeeAssetTool.description()
)
async def create_employee_asset(input_data: CreateEmployeeAssetInput):
    result = await CreateEmployeeAssetTool().execute(input_data)
    return result.to_response()

@mcp.tool(
    name=CreateInviteTool.name(),
    description=CreateInviteTool.description()
)
async def create_invite(input_data: CreateInviteInput):
    result = await CreateInviteTool().execute(input_data)
    return result.to_response()

if __name__ == "__main__":
    mcp.run(transport='stdio')
