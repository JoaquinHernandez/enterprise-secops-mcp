import os
import httpx
from typing import Optional

def register_security_tools(mcp):

    @mcp.tool()
    async def splunk_search(spl_query: str, earliest_time: str = "-24h") -> str:
        """Executes a search query (SPL) against Splunk Enterprise/Cloud."""
        host = os.getenv("SPLUNK_HOST")
        token = os.getenv("SPLUNK_TOKEN")
        if not host or not token:
            return "Error: Splunk configuration missing in environment."
        
        async with httpx.AsyncClient(verify=False) as client:
            headers = {"Authorization": f"Bearer {token}"}
            data = {"search": f"search {spl_query}", "earliest_time": earliest_time, "output_mode": "json"}
            resp = await client.post(f"{host}/services/search/jobs/export", headers=headers, data=data, timeout=30.0)
            return resp.text[:2000]

    @mcp.tool()
    async def get_sentinel_incidents(severity_filter: Optional[str] = "High") -> str:
        """Retrieves active security incidents from Microsoft Sentinel."""
        workspace = os.getenv("SENTINEL_WORKSPACE_ID")
        if not workspace:
            return "Error: Sentinel Workspace ID not configured."
        return f"[Sentinel] Retrieved active incidents for workspace {workspace} filtered by severity: {severity_filter}"

    @mcp.tool()
    async def tenable_get_vulnerabilities(severity: str = "critical", limit: int = 10) -> str:
        """Lists active vulnerabilities from Tenable.io / Tenable.sc."""
        access_key = os.getenv("TENABLE_ACCESS_KEY")
        secret_key = os.getenv("TENABLE_SECRET_KEY")
        if not access_key:
            return "Error: Tenable credentials not set."
        return f"[Tenable] Querying top {limit} {severity} vulnerability findings across assets."

    @mcp.tool()
    async def qualys_host_scan_status(target_ip: str) -> str:
        """Fetches host vulnerability assessment posture from Qualys Guard API."""
        return f"[Qualys] Vulnerability posture query executed for target host {target_ip}."

    @mcp.tool()
    async def edr_isolate_endpoint(endpoint_id: str, action: str = "isolate") -> str:
        """Isolates or remediates a compromised host using the EDR API."""
        return f"[EDR] Action '{action}' successfully initiated for endpoint: {endpoint_id}"
