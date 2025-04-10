"""Tools package for the Workwize MCP server."""
from .assets import *
from .employees import *
from .offices import *
from .orders import *
from .self import *
from .warehouses import *

from workwize_mcp.tools.categories import GetCategoriesTool
from workwize_mcp.tools.employees import GetEmployeeTool, UpdateEmployeeAddressTool
from workwize_mcp.tools.invites import SendInviteTool
from workwize_mcp.tools.offboards import CreateOffboardTool, GetOffboardsTool
from workwize_mcp.tools.self import GetSelfTool

__all__ = (
    assets.__all__ +  # type: ignore
    employees.__all__ +  # type: ignore
    offices.__all__ +  # type: ignore
    orders.__all__ +  # type: ignore
    self.__all__ +  # type: ignore
    warehouses.__all__  # type: ignore
)

__all__ += [
    "GetCategoriesTool",
    "GetEmployeeTool",
    "UpdateEmployeeAddressTool",
    "SendInviteTool",
    "CreateOffboardTool",
    "GetOffboardsTool",
    "GetSelfTool",
]
