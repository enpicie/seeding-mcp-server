"""MCP server entry point.

Single responsibility: define MCP tools and wire them to the FastMCP app.
Business logic lives in startgg_client.py and scoring.py — this file only
contains tool definitions and the main() entry point.
"""

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("seeding-mcp")


@mcp.tool()
def ping() -> str:
    """Verify that the MCP server is reachable and responding.

    Returns:
        The string "pong".
    """
    return "pong"


def main() -> None:
    """Start the MCP server using stdio transport (default for MCP clients)."""
    mcp.run()
