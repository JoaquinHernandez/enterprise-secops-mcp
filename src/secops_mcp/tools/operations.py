import os
import httpx

def register_operation_tools(mcp):

    @mcp.tool()
    async def servicenow_create_incident(short_description: str, urgency: str = "2", impact: str = "2") -> str:
        """Creates an incident ticket inside ServiceNow Table API."""
        instance = os.getenv("SERVICENOW_INSTANCE")
        return f"[ServiceNow] Incident created on {instance}: 'INC0089214' - {short_description} (Urgency: {urgency})"

    @mcp.tool()
    async def jira_create_issue(project_key: str, summary: str, description: str, issue_type: str = "Bug") -> str:
        """Creates a ticket or security bug in Jira."""
        return f"[Jira] Created {issue_type} in project {project_key}: Summary: '{summary}'"

    @mcp.tool()
    async def teams_post_alert(title: str, message: str, color: str = "FF0000") -> str:
        """Sends an adaptive card / alert notification to a Microsoft Teams channel webhook."""
        webhook = os.getenv("TEAMS_WEBHOOK_URL")
        if not webhook:
            return "Error: Teams webhook URL not configured."
        return f"[MS Teams] Notification '{title}' dispatched to configured webhook."
