<p align="center">
  <a href="https://github.com/DochertyDev/time-mcp">
    <img src="images/apple-touch-icon.png" width="150" alt="Time MCP">
  </a>
</p>

<h1 align="center">
Time MCP
</h1>

<h2 align="center">Effortless system time access, anywhere your LLM needs it.</h2>

<div align="center">

[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE) [![GitHub Stars](https://img.shields.io/github/stars/DochertyDev/time-mcp)](https://github.com/DochertyDev/time-mcp)

</div>

:star: _Love Time MCP? Give us a star to help other developers discover it!_

<br />

<div>
<img src="images/Time-MCPscreenshot.png" alt="Time MCP Screenshot" width="800" style="border-radius: 16px; box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3), 0 0 0 1px rgba(255, 255, 255, 0.1), inset 0 1px 0 rgba(255, 255, 255, 0.2); transform: perspective(1000px) rotateX(2deg); transition: transform 0.3s ease;">
</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Quick Start](#-quick-start-local-development)
- [Usage](#️-usage)
- [Technologies Used](#️-technologies-used)
- [Security Notes](#-security-notes)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [Support the Project](#-support-the-project)
- [Disclaimer](#️-disclaimer)

## 📄 Overview

Time MCP is a simple and lightweight Model Context Protocol (MCP) server that provides tools to fetch the current date and time from your system. It's perfect for integrating time-related functionality into Claude, Gemini CLI, and other MCP-compatible LLM applications.

This MCP demonstrates core MCP functionality with a focused, practical use case that works reliably across all MCP-compatible platforms.

### Features

This MCP provides the following tools:

-   **get_current_time()** - Returns the current time in HH:MM:SS format
-   **get_current_date()** - Returns the current date in YYYY-MM-DD format
-   **get_current_datetime()** - Returns both date and time in ISO 8601 format
-   **get_time_components()** - Returns detailed breakdown of time (year, month, day, hour, minute, second, day of week)
-   **get_unix_timestamp()** - Returns the current Unix timestamp

## 🚀 Quick Start (Local Development)

### Prerequisites
- Python 3.9 or higher
- pip

### From PyPI (Recommended)

Once published, you can install directly from PyPI:

```bash
pip install time-mcp
```

### From Source (Development)

1. Clone the repository:

    ```sh
    git clone https://github.com/DochertyDev/time-mcp.git
    ```

2. Navigate to the project directory:

    ```sh
    cd time-mcp
    ```

3. Install in development mode:
    ```sh
    pip install -e .
    ```

4. Or install dependencies manually:
    ```sh
    pip install -r requirements.txt
    ```

### Running the Server

To start the MCP server:

```bash
python src/server.py
```

The server will start and wait for incoming MCP protocol connections.

### Testing with MCP Inspector

To debug and test your MCP with the MCP Inspector:

```bash
mcp dev src/server.py
```

This will open the MCP Inspector interface where you can test each tool interactively.

## ⚙️ Usage

### Using with Claude Desktop

To add this MCP to Claude Desktop, update your `claude_desktop_config.json`:

#### If installed from PyPI:
```json
{
  "mcpServers": {
    "time-mcp": {
      "command": "time-mcp"
    }
  }
}
```

#### If installed from source:
```json
{
  "mcpServers": {
    "time-mcp": {
      "command": "python",
      "args": ["C:\\path\\to\\time-mcp\\src\\server.py"]
    }
  }
}
```

Replace `C:\path\to\time-mcp` with the actual path to your time-mcp directory.

### Using with Gemini CLI

Add to your Gemini CLI settings.json:

```json
{
  "mcpServers": {
    "time-mcp": {
      "command": "time-mcp"
    }
  }
}
```

## 🛠️ Technologies Used

-   **FastMCP Framework**
-   **Python 3.9+**
-   **pip**

## 🔒 Security Notes

-   This MCP only accesses time-related information from your system
-   No file system access
-   No network requests
-   No external API calls
-   No credentials or secrets required

## ❓ Troubleshooting

**Issue**: MCP Inspector won't connect
-   **Solution**: Ensure Python 3.9+ is installed and the mcp package is available

**Issue**: Tools not appearing in Claude
-   **Solution**: Make sure the MCP server is running and properly configured in claude_desktop_config.json

**Issue**: Import errors
-   **Solution**: Run `pip install -r requirements.txt` to ensure all dependencies are installed

## 🤝 Contributing

<div align="center">
<a href="https://github.com/DochertyDev/time-mcp/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=DochertyDev/time-mcp&max=400&columns=20"  width="100"/>
</a>
</div>

We welcome contributions from the community! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

## 🌟 Support the Project

**Love Time MCP?** Give us a ⭐ on GitHub!

<div align="center">
  <p>
      <img width="800" src="https://api.star-history.com/svg?repos=DochertyDev/time-mcp&type=Date" alt="Star-history">
  </p>
</div>

If you encounter any issues, please open an issue [here](https://github.com/DochertyDev/time-mcp/issues).

## ⚠️ Disclaimer

This project is intended for educational and experimental use. While every effort has been made to ensure its reliability, please use it responsibly and note that the authors cannot provide guarantees for every situation.
