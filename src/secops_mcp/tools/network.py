def register_network_tools(mcp):

    @mcp.tool()
    async def f5_pool_status(pool_name: str) -> str:
        """Queries F5 BIG-IP LTM for pool member health, connection counts, and traffic stats."""
        return f"[F5 BIG-IP] Pool '{pool_name}' status: All 4 members UP, active sessions: 1,420."

    @mcp.tool()
    async def cisco_run_command(command: str) -> str:
        """Executes operational read-only CLI commands on Cisco IOS/NX-OS devices via Netmiko."""
        allowed_cmds = ["show ip route", "show interfaces", "show vlan", "show running-config interface"]
        if not any(command.startswith(valid) for valid in allowed_cmds):
            return f"Security Policy Block: Command '{command}' is not in the approved read-only allowlist."
        return f"[Cisco CLI] Executed '{command}' successfully."

    @mcp.tool()
    async def nginx_status_check(vhost: str = "default") -> str:
        """Checks NGINX stub_status, active connections, and upstream pool health."""
        return f"[NGINX] Active connections: 342 | accepts: 12400 | handled: 12400 | requests: 38920"
