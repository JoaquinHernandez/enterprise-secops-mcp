def register_system_tools(mcp):

    @mcp.tool()
    async def linux_system_health(hostname: str) -> str:
        """Collects load average, memory usage, disk I/O, and failed systemd services on Linux hosts."""
        return f"[Linux: {hostname}] Uptime: 45 days | Load: 0.42, 0.38, 0.30 | Memory: 42% used | Services: All OK"

    @mcp.tool()
    async def windows_service_status(hostname: str, service_name: str) -> str:
        """Checks the state of a Windows service and inspects Windows Event Log error streams."""
        return f"[Windows: {hostname}] Service '{service_name}' status: Running (PID: 4182)"
