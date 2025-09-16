import asyncio
import logging
from typing import Dict, Any, List, Optional

from mcp.server import Server
from mcp.types import Tool, TextContent, CallToolRequest, CallToolResult
from pydantic import BaseModel


class MCPServer:
    def __init__(self, name: str = "example-mcp-server"):
        self.name = name
        self.server = Server(name)
        self.tools: Dict[str, Tool] = {}

        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def register_tool(self, name: str, description: str, parameters: Dict[str, Any], handler):
        """Register a tool with the server"""
        tool = Tool(
            name=name,
            description=description,
            inputSchema={
                "type": "object",
                "properties": parameters,
                "required": list(parameters.keys())
            }
        )

        self.tools[name] = tool

        @self.server.call_tool()
        async def call_tool(name: str, arguments: Dict[str, Any]) -> CallToolResult:
            if name in self.tools:
                try:
                    result = await handler(arguments)
                    return CallToolResult(
                        content=[TextContent(type="text", text=str(result))]
                    )
                except Exception as e:
                    self.logger.error(f"Error executing tool {name}: {e}")
                    return CallToolResult(
                        content=[TextContent(type="text", text=f"Error: {str(e)}")],
                        isError=True
                    )
            else:
                return CallToolResult(
                    content=[TextContent(type="text", text=f"Unknown tool: {name}")],
                    isError=True
                )

    def list_tools(self) -> List[Tool]:
        """Return list of available tools"""
        return list(self.tools.values())

    async def run(self, transport_type: str = "stdio"):
        """Start the MCP server"""
        self.logger.info(f"Starting {self.name} MCP server...")

        if transport_type == "stdio":
            from mcp.server.stdio import stdio_server
            async with stdio_server() as (read_stream, write_stream):
                await self.server.run(read_stream, write_stream)
        else:
            raise ValueError(f"Unsupported transport type: {transport_type}")


# Create server instance
mcp_server = MCPServer()