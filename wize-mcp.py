from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

from tools.self import GetSelfTool

from tools.assets import GetAssetsTool
from tools.assets.get_assets import GetAssetsInput

from tools.categories import GetCategoriesTool

from tools.employees import GetEmployeesTool, CreateEmployeeTool, GetEmployeeUserTool, GetEmployeeAddressesTool, UpdateEmployeeTool, UpdateEmployeeAddressTool, CreateEmployeeAddressTool, CreateEmployeeAssetTool, CreateOrderForEmployeeTool
from tools.employees.get_employees import GetEmployeesInput
from tools.employees.create_employee import CreateEmployeeInput
from tools.employees.get_employee_user import GetEmployeeUserInput
from tools.employees.get_employee_addresses import GetEmployeeAddressesInput
from tools.employees.update_employee import UpdateEmployeeInput
from tools.employees.update_employee_address import UpdateEmployeeAddressInput
from tools.employees.create_employee_address import CreateEmployeeAddressInput
from tools.employees.create_employee_asset import CreateEmployeeAssetInput
from tools.employees.create_order_for_employee import CreateOrderForEmployeeInput

from tools.invites import CreateInviteTool
from tools.invites.create_invite import CreateInviteInput

from tools.offboards import GetOffboardsTool, CreateOffboardTool
from tools.offboards.get_offboards import GetOffboardsInput
from tools.offboards.create_offboard import CreateOffboardInput

from tools.offices import GetOfficesTool, CreateOrderForOfficeTool
from tools.offices.get_offices import GetOfficesInput
from tools.offices.create_order_for_office import CreateOrderForOfficeInput

from tools.orders import GetOrdersTool, GetOrderProductsTool, GetOrderShipmentsTool
from tools.orders.get_orders import GetOrdersInput
from tools.orders.get_order_products import GetOrderProductsInput
from tools.orders.get_order_shipments import GetOrderShipmentsInput

from tools.products import GetProductsTool
from tools.products.get_products import GetProductsInput

from tools.users import CreateUserTool
from tools.users.create_user import CreateUserInput

from tools.warehouses import GetWarehousesTool, CreateOrderForWarehouseTool
from tools.warehouses.create_order_for_warehouse import CreateOrderForWarehouseInput

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

@mcp.tool(
    name=CreateOffboardTool.name(),
    description=CreateOffboardTool.description()
)
async def create_offboard(input_data: CreateOffboardInput):
    result = await CreateOffboardTool().execute(input_data)
    return result.to_response()

@mcp.tool(
    name=CreateUserTool.name(),
    description=CreateUserTool.description()
)
async def create_user(input_data: CreateUserInput):
    result = await CreateUserTool().execute(input_data)
    return result.to_response()

@mcp.tool(
    name=CreateOrderForEmployeeTool.name(),
    description=CreateOrderForEmployeeTool.description()
)
async def create_order_for_employee(input_data: CreateOrderForEmployeeInput):
    result = await CreateOrderForEmployeeTool().execute(input_data)
    return result.to_response()

@mcp.tool(
    name=CreateOrderForOfficeTool.name(),
    description=CreateOrderForOfficeTool.description()
)
async def create_order_for_office(input_data: CreateOrderForOfficeInput):
    result = await CreateOrderForOfficeTool().execute(input_data)
    return result.to_response()

@mcp.tool(
    name=CreateOrderForWarehouseTool.name(),
    description=CreateOrderForWarehouseTool.description()
)
async def create_order_for_warehouse(input_data: CreateOrderForWarehouseInput):
    result = await CreateOrderForWarehouseTool().execute(input_data)
    return result.to_response()

if __name__ == "__main__":
    # response_self = asyncio.run(get_self())
    # if 'id' in response_self:
    #     print('✅ Self fetched successfully')
    # else:
    #     print('❌ Failed to fetch self')

    # response1 = asyncio.run(get_employees(GetEmployeesInput()))
    # if len(response1) > 0:
    #     print('✅ Employees fetched successfully')
    # else:
    #     print('❌ Failed to fetch employees')

    # response2 = asyncio.run(get_offices(GetOfficesInput()))
    # if len(response2) > 0:
    #     print('✅ Offices fetched successfully')
    # else:
    #     print('❌ Failed to fetch offices')

    # response3 = asyncio.run(get_warehouses())
    # if len(response3) > 0:
    #     print('✅ Warehouses fetched successfully')
    # else:
    #     print('❌ Failed to fetch warehouses')

    # response4 = asyncio.run(get_orders(GetOrdersInput()))
    # if len(response4) > 0:
    #     print('✅ Orders fetched successfully')
    # else:
    #     print('❌ Failed to fetch orders')

    # response5 = asyncio.run(get_order_products(GetOrderProductsInput(order_number=response4['data'][0]['number'])))
    # if len(response5) > 0:
    #     print('✅ Order products fetched successfully')
    # else:
    #     print('❌ Failed to fetch order products')

    # response6 = asyncio.run(get_order_shipments(GetOrderShipmentsInput(order_number=response4['data'][0]['number'])))
    # if len(response6) > 0:
    #     print('✅ Order shipments fetched successfully')
    # else:
    #     print('❌ Failed to fetch order shipments')

    # response7 = asyncio.run(get_products(GetProductsInput()))
    # if len(response7) > 0:
    #     print('✅ Products fetched successfully')
    # else:
    #     print('❌ Failed to fetch products')

    # response7 = asyncio.run(get_products(GetProductsInput(search='macbook')))
    # if len(response7) > 0:
    #     print('✅ Products fetched successfully')
    # else:
    #     print('❌ Failed to fetch products')

    # response8 = asyncio.run(get_offboards(GetOffboardsInput()))
    # if len(response8['data']) > 0:
    #     print('✅ Offboards fetched successfully')
    # else:
    #     print('❌ Failed to fetch offboards')

    # response9 = asyncio.run(get_employee_user(GetEmployeeUserInput(employee_id=response1[0]['id'])))
    # if 'id' in response9:
    #     print('✅ Employee user fetched successfully')
    # else:
    #     print('❌ Failed to fetch employee user')

    # response10 = asyncio.run(get_employee_addresses(GetEmployeeAddressesInput(employee_id=response1[0]['id'])))
    # if 'id' in response10['data']:
    #     print('✅ Employee addresses fetched successfully')
    # else:
    #     print('❌ Failed to fetch employee addresses')

    # response11 = asyncio.run(get_assets(GetAssetsInput(employee_id=response1[0]['id'])))
    # if len(response11['data']) > 0:
    #     print('✅ Assets fetched successfully')
    # else:
    #     print('❌ Failed to fetch assets')

    # response12 = asyncio.run(get_categories())
    # if len(response12) > 0:
    #     print('✅ Categories fetched successfully')
    # else:
    #     print('❌ Failed to fetch categories')

    # response13 = asyncio.run(get_offices(GetOfficesInput()))
    # if len(response13) > 0:
    #     print('✅ Offices fetched successfully')
    # else:
    #     print('❌ Failed to fetch offices')


    mcp.run(transport='stdio')
