# MCP Server

A basic Model Context Protocol (MCP) server implementation in Python that provides utility tools for interacting with the file system and getting system information.

## Features

This MCP server provides the following tools:

- **hello_world**: A simple greeting tool that accepts an optional name parameter
- **get_time**: Get the current time in various formats (ISO, timestamp, or readable)
- **list_files**: List files and directories in a specified path
- **read_file**: Read the contents of a text file

## Installation

### Prerequisites

- Python 3.13+
- uv package manager

### Setup

1. Clone the repository:
```bash
git clone https://github.com/stef-codes/mcp-server.git
cd mcp-server
```

2. Install dependencies using uv:
```bash
uv sync
```

## Usage

Run the MCP server:

```bash
uv run python main.py
```

The server will start and listen for MCP connections via stdio transport.

## Project Structure

```
├── main.py          # Entry point and tool registration
├── server.py        # Core MCP server implementation
├── tools.py         # Tool implementations
├── pyproject.toml   # Project configuration and dependencies
└── README.md        # This file
```

## Available Tools

### hello_world
Greets a user with an optional name parameter.

**Parameters:**
- `name` (string, optional): Name to greet (defaults to "World")

### get_time
Returns the current time in the specified format.

**Parameters:**
- `format` (string, optional): Format type - "iso", "timestamp", or "readable" (defaults to "iso")

### list_files
Lists files and directories in the specified path.

**Parameters:**
- `path` (string, optional): Directory path to list (defaults to current directory)

### read_file
Reads and returns the contents of a text file.

**Parameters:**
- `file_path` (string, required): Path to the file to read

## Development

The server uses a modular architecture:

- `MCPServer` class handles server initialization and tool registration
- Tools are implemented as async functions in `tools.py`
- The `main.py` file registers all tools and starts the server

To add new tools:

1. Implement the tool function in `tools.py`
2. Register it in `main.py` using `mcp_server.register_tool()`

## License

This project is open source and available under the MIT License.