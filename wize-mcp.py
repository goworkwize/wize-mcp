from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

from tools.self import GetSelfTool

from tools.categories import GetCategoriesTool

from tools.offices import GetOfficesTool
from tools.offices.get_offices import GetOfficesInput

from tools.employees import GetEmployeesTool, CreateEmployeeTool, GetEmployeeUserTool
from tools.employees.get_employees import GetEmployeesInput
from tools.employees.create_employee import CreateEmployeeInput
from tools.employees.get_employee_user import GetEmployeeUserInput

from tools.orders import GetOrdersTool, GetOrderProductsTool, GetOrderShipmentsTool
from tools.orders.get_orders import GetOrdersInput
from tools.orders.get_order_products import GetOrderProductsInput
from tools.orders.get_order_shipments import GetOrderShipmentsInput

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

if __name__ == "__main__":
    mcp.run(transport='stdio')
