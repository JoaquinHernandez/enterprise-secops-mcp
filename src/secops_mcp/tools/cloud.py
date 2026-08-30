import os
from typing import Dict, Any

def register_cloud_tools(mcp):

    @mcp.tool()
    async def aws_cloudwatch_alarms(state: str = "ALARM") -> str:
        """Lists active AWS CloudWatch alarms filtered by state (ALARM, OK, INSUFFICIENT_DATA)."""
        region = os.getenv("AWS_REGION", "us-east-1")
        return f"[AWS CloudWatch] Scanning region {region} for alarms in state: {state}"

    @mcp.tool()
    async def azure_monitor_alerts(severity: int = 1) -> str:
        """Retrieves fired alerts from Azure Monitor across subscriptions."""
        sub_id = os.getenv("AZURE_SUBSCRIPTION_ID")
        return f"[Azure Monitor] Fetching alerts with severity {severity} in subscription {sub_id}"

    @mcp.tool()
    async def gcp_get_metric(metric_type: str = "compute.googleapis.com/instance/cpu/utilization") -> str:
        """Queries Google Cloud Monitoring metrics for compute and container workloads."""
        project = os.getenv("GCP_PROJECT_ID")
        return f"[GCP Cloud Monitoring] Project {project}: Querying metric series {metric_type}"
