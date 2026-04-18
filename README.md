# seeding-mcp-server

An MCP server for FGC tournament seeding. Exposes tools that fetch player and
tournament data from the [start.gg](https://start.gg) GraphQL API, run seeding
score calculations, and return structured data for Claude to reason over.

## Setup

```bash
python -m venv .venv
source .venv/Scripts/activate   # Windows
# source .venv/bin/activate     # macOS/Linux

pip install -e .
```

## Configuration

Copy `.env.example` to `.env` and fill in your start.gg API token:

```
STARTGG_TOKEN=your_token_here
```

## Running

```bash
seeding-mcp
```

## Project structure

```
src/seeding_mcp/
  server.py          — MCP tool definitions and entry point
  startgg_client.py  — start.gg GraphQL API client
  scoring.py         — seeding score calculations
  config.py          — environment variable loading
tests/
  test_scoring.py
  test_startgg_client.py
```
