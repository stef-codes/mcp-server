import os
import json
from typing import Dict, Any
from datetime import datetime


async def hello_world_tool(arguments: Dict[str, Any]) -> str:
    """Simple hello world tool"""
    name = arguments.get("name", "World")
    return f"Hello, {name}!"


async def get_time_tool(arguments: Dict[str, Any]) -> str:
    """Get current time"""
    format_type = arguments.get("format", "iso")

    now = datetime.now()

    if format_type == "iso":
        return now.isoformat()
    elif format_type == "timestamp":
        return str(int(now.timestamp()))
    else:
        return now.strftime("%Y-%m-%d %H:%M:%S")


async def list_files_tool(arguments: Dict[str, Any]) -> str:
    """List files in a directory"""
    path = arguments.get("path", ".")

    try:
        files = os.listdir(path)
        return json.dumps({
            "path": path,
            "files": files,
            "count": len(files)
        }, indent=2)
    except Exception as e:
        return f"Error listing files: {str(e)}"


async def read_file_tool(arguments: Dict[str, Any]) -> str:
    """Read contents of a file"""
    file_path = arguments["file_path"]

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        return content
    except Exception as e:
        return f"Error reading file: {str(e)}"