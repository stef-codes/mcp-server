#!/usr/bin/env python3

import asyncio
from server import mcp_server
from tools import hello_world_tool, get_time_tool, list_files_tool, read_file_tool


def register_tools():
    """Register all available tools with the server"""

    # Register hello world tool
    mcp_server.register_tool(
        name="hello_world",
        description="A simple greeting tool",
        parameters={
            "name": {
                "type": "string",
                "description": "Name to greet (optional)",
                "default": "World"
            }
        },
        handler=hello_world_tool
    )

    # Register time tool
    mcp_server.register_tool(
        name="get_time",
        description="Get the current time in various formats",
        parameters={
            "format": {
                "type": "string",
                "description": "Format type: 'iso', 'timestamp', or 'readable'",
                "enum": ["iso", "timestamp", "readable"],
                "default": "iso"
            }
        },
        handler=get_time_tool
    )

    # Register list files tool
    mcp_server.register_tool(
        name="list_files",
        description="List files in a directory",
        parameters={
            "path": {
                "type": "string",
                "description": "Directory path to list (defaults to current directory)",
                "default": "."
            }
        },
        handler=list_files_tool
    )

    # Register read file tool
    mcp_server.register_tool(
        name="read_file",
        description="Read the contents of a text file",
        parameters={
            "file_path": {
                "type": "string",
                "description": "Path to the file to read"
            }
        },
        handler=read_file_tool
    )


async def main():
    """Main entry point"""
    # Register all tools
    register_tools()

    # Start the server
    await mcp_server.run()


if __name__ == "__main__":
    asyncio.run(main())