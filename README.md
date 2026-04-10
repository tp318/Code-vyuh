# 🚚 Code Vyuh - Logistics AI Project

[![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

An intelligent, AI-powered logistics management system built with **Python**, featuring autonomous AI agents, real-time tracking, and modular service architecture. This project leverages LLM-based decision-making to optimize routes, manage shipments, and automate logistics workflows.

## 📋 Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Configuration](#configuration)
- [Services](#services)
- [AI Agents](#ai-agents)
- [Usage Examples](#usage-examples)
- [Contributing](#contributing)
- [License](#license)

## Overview

**Code Vyuh** is a comprehensive Python-based intelligent system designed to streamline and automate complex logistics operations. The project integrates with **Qoder**, an AI-assisted development tool, to enable agent-based workflows and intelligent automation pipelines.

**Use Cases:**
- 📦 Real-time shipment tracking and status management
- 🗺️ Dynamic route optimization and delivery planning
- 🔔 Proactive notification systems for delays and exceptions
- 🤖 AI-driven decision-making for logistics operations

## Key Features

| Feature | Description |
|---------|-------------|
| 🤖 **AI Agent Integration** | Autonomous agents powered by LLMs for intelligent, context-aware logistics decisions |
| 📦 **Shipment Tracking** | Real-time tracking and comprehensive status updates for all orders |
| 🗺️ **Route Optimization** | Smart routing algorithms that minimize cost, time, and environmental impact |
| 🔔 **Smart Notifications** | Automated, event-driven alerts for delays, arrivals, and exceptional cases |
| ⚙️ **Modular Architecture** | Clean separation of concerns across independent, reusable service modules |
| 🛠️ **Flexible Configuration** | Centralized configuration management for environments and API integration |
| 🔐 **Production Ready** | Secure credential management and environment-based configuration |

## Project Structure

```
Code-vyuh/
│
├── logistics_ai_project/           # Core application logic
│   ├── models/                     # Data models and schemas
│   ├── agents/                     # AI agent definitions and runtime logic
│   ├── utils/                      # Helper utilities and common functions
│   └── main.py                     # Application entry point
│
├── services/                       # Modular service layer
│   ├── tracking/                   # Shipment & order tracking service
│   ├── routing/                    # Route optimization service
│   └── notifications/              # Alerts and notification service
│
├── .qoder/
│   └── agents/                     # Qoder AI agent configurations
│
├── config.py                       # Global configuration management
├── requirements.txt                # Project dependencies
├── README.md                       # This file
└── LICENSE                         # MIT License
```

## Getting Started

### Prerequisites

- **Python** 3.9 or higher
- **pip** (Python package manager)
- Virtual environment (recommended)

### Installation

```bash
# Clone the repository
git clone https://github.com/tp318/Code-vyuh.git
cd Code-vyuh

# Create and activate virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Running the Application

```bash
# Execute the main application
python main.py
```

## Configuration

Edit `config.py` to set your environment variables, API keys, and service endpoints:

```python
# config.py
DATABASE_URL = "your_database_url"
API_KEY = "your_api_key"
LOG_LEVEL = "INFO"
DEBUG = False

# Service endpoints
TRACKING_SERVICE_URL = "http://localhost:8001"
ROUTING_SERVICE_URL = "http://localhost:8002"
NOTIFICATION_SERVICE_URL = "http://localhost:8003"
```

⚠️ **Security Note:** Never commit sensitive credentials to version control. Use:
- Environment variables
- `.env` files (add to `.gitignore`)
- Secret management tools (AWS Secrets Manager, HashiCorp Vault, etc.)

## Services

The `services/` directory contains independent, reusable modules:

| Service | Purpose | Key Capabilities |
|---------|---------|------------------|
| **tracking** | Shipment management | Live tracking, status updates, historical logs |
| **routing** | Delivery optimization | Route calculation, cost minimization, ETAs |
| **notifications** | Event-driven alerts | Email, SMS, push notifications, webhooks |

## AI Agents

The `.qoder/agents/` directory contains AI agent configurations that power intelligent decision-making:

- **Route Planning Agent** — Optimizes delivery routes based on real-time data
- **Shipment Tracking Agent** — Monitors shipments and detects anomalies
- **Customer Notification Agent** — Generates timely, contextual alerts
- **Compliance Agent** — Ensures adherence to logistics regulations

## Usage Examples

### Track a Shipment

```python
from logistics_ai_project.services.tracking import TrackingService

tracker = TrackingService()
status = tracker.get_shipment_status(shipment_id="SHIP123")
print(status)
```

### Optimize a Route

```python
from logistics_ai_project.services.routing import RoutingService

router = RoutingService()
optimal_route = router.optimize_route(locations=["A", "B", "C"])
print(optimal_route)
```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add your feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

Please ensure:
- Code follows PEP 8 standards
- Tests are included for new features
- Documentation is updated

## License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

**Questions or Issues?** Open an issue on GitHub or contact the maintainers.