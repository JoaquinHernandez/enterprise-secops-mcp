# enterprise-secops-mcp
<div align="center">

# 🛡️ Enterprise SecOps & Infrastructure MCP Server

**A Unified, Hardened Model Context Protocol (MCP) Server for Modern Security Operations, Multi-Cloud Telemetry, and Infrastructure Automation.**

[![MCP Version](https://img.shields.io/badge/MCP%20Spec-2025.11-blue?style=for-the-badge&logo=anthropic)](https://modelcontextprotocol.io)
[![Python Version](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![FastMCP](https://img.shields.io/badge/Engine-FastMCP-0052CC?style=for-the-badge)](https://github.com/jlowin/fastmcp)
[![License](https://img.shields.io/badge/License-Apache%202.0-green?style=for-the-badge)](LICENSE)
[![Zero-Trust Hardened](https://img.shields.io/badge/Zero--Trust-Enforced-red?style=for-the-badge&logo=securityscorecard)](docs/security.md)

[Features](#-key-features) • [Architecture](#-architecture) • [Supported Integrations](#-supported-integrations) • [Quickstart](#-quickstart) • [Configuration](#-environment-variables) • [Security](#-security-guardrails)

</div>

---

## ⚡ Overview

The **Enterprise SecOps MCP Server** bridges the gap between Large Language Models (LLMs) and mission-critical enterprise environments. By translating high-level natural language intent into deterministic, validated API actions, security analysts, SREs, and DevOps engineers can triage incidents, audit vulnerabilities, verify network path topologies, and orchestrate automated remediations across hybrid architectures.

---

## 🏗️ Architecture
                   ┌───────────────────────────────┐
                   │   LLM Client / MCP Host       │
                   │  (Claude Desktop, Cursor, AI) │
                   └───────────────┬───────────────┘
                                   │ stdio / SSE (OAuth 2.1)
                                   ▼
                   ┌───────────────────────────────┐
                   │   FastMCP SecOps Engine       │
                   │   - Input Schema Validator    │
                   │   - Safe Execution Layer      │
                   │   - Least Privilege RBAC      │
                   └───────┬───────────────┬───────┘
                           │               │
  ┌────────────────────────┴─┐           ┌─┴────────────────────────┐
  │ Hybrid Multi-Cloud & SIEM│           │ Network, ITSM & Agents   │
  ├──────────────────────────┤           ├──────────────────────────┤
  │ • AWS CloudWatch         │           │ • Cisco IOS / NX-OS      │
  │ • Azure Monitor          │           │ • F5 BIG-IP Traffic LTM  │
  │ • GCP Cloud Ops          │           │ • NGINX Server Fleet     │
  │ • Splunk Enterprise/Cloud│           │ • ServiceNow Incidents   │
  │ • Microsoft Sentinel     │           │ • Jira Issue Pipeline    │
  │ • Tenable.io / Qualys VM │           │ • Microsoft Teams Alerts │
  │ • EDR Response Engine    │           │ • AiAura Platform API    │
  └──────────────────────────┘           └──────────────────────────┘
---

## 🎯 Supported Integrations

### 1. 🛡️ SIEM, Vulnerability & Endpoint Response
* **Splunk**: Execute raw SPL queries, monitor scheduled search jobs, extract live alert streams.
* **Microsoft Sentinel**: Query incidents across Log Analytics workspaces by severity and MITRE ATT&CK tactics.
* **Tenable.io / Tenable.sc**: Fetch asset vulnerability postures and CVE exposure levels.
* **Qualys VMDR**: Run dynamic vulnerability queries and host risk metrics.
* **EDR Agent API**: Trigger network isolation, policy quarantine, or process remediation.

### 2. ☁️ Multi-Cloud Telemetry & Infrastructure
* **AWS CloudWatch & EC2**: Scan alarms across AWS regions, query metrics, and parse status checks.
* **Azure Monitor**: Retrieve alert summaries and resource metrics across enterprise subscriptions.
* **Google Cloud Monitoring**: Inspect compute and GKE container metrics via TimeSeries queries.

### 3. 🌐 Enterprise Network & Delivery
* **F5 BIG-IP**: Audit LTM pools, active connection distributions, and node health.
* **Cisco IOS/NX-OS**: Execute whitelisted, operational read-only CLI diagnostics via Netmiko.
* **NGINX**: Read runtime statistics via status modules and inspect upstream pools.

### 4. ⚙️ Operating Systems & ITSM Automation
* **Linux / Windows Hosts**: Audit host resource utilization, service status, and critical event logs.
* **ServiceNow**: Automatically create and triage ITSM incident tickets (Table API).
* **Jira**: Generate issue tracking tasks with full markdown diagnostics.
* **Microsoft Teams**: Dispatch real-time adaptive cards to incident response channels.
* **AiAura Platform**: Connect directly to multi-tenant telemetry and autonomous remediation pipelines.

---

## 🚀 Quickstart

### Prerequisites
* Python `>= 3.10`
* [uv](https://github.com/astral-sh/uv) (recommended) or standard `pip`

### 1. Clone & Setup

```bash
# Clone the repository
git clone [https://github.com/your-username/enterprise-secops-mcp.git](https://github.com/your-username/enterprise-secops-mcp.git)
cd enterprise-secops-mcp

# Create and activate virtual environment using uv
uv venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install editable package with core dependencies
uv pip install -e .
