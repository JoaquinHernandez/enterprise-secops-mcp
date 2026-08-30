from fastmcp import FastMCP
from secops_mcp.tools import (
    register_aiaura_tools,
    register_cloud_tools,
    register_security_tools,
    register_network_tools,
    register_system_tools,
    register_operation_tools,
)

# Initialize MCP Server
mcp = FastMCP(
    name="Enterprise-SecOps-Unified-MCP",
    dependencies=["httpx", "boto3", "paramiko"]
)

# Register modular sub-toolkits
register_aiaura_tools(mcp)
register_cloud_tools(mcp)
register_security_tools(mcp)
register_network_tools(mcp)
register_system_tools(mcp)
register_operation_tools(mcp)

def main():
    mcp.run(transport="stdio")

if __name__ == "__main__":
    main()
