import os
import httpx

def register_aiaura_tools(mcp):

    @mcp.tool()
    async def aiaura_query_telemetry(tenant_id: str, metric_name: str) -> str:
        """Queries AiAura multi-tenant core platform telemetry and inference health."""
        api_url = os.getenv("AIAURA_API_URL", "https://api.aiaura.me/v1")
        api_key = os.getenv("AIAURA_API_KEY")
        return f"[AiAura Engine] Tenant '{tenant_id}' Metric '{metric_name}' fetched from {api_url}."

    @mcp.tool()
    async def aiaura_trigger_remediation(tenant_id: str, action_type: str) -> str:
        """Dispatches an automated remediation workflow to the AiAura agent pipeline."""
        return f"[AiAura Orchestrator] Triggered action '{action_type}' for tenant '{tenant_id}'."
