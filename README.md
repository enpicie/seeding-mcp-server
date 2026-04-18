# seeding-mcp-server

An MCP server for FGC tournament seeding. Exposes tools that fetch player and
tournament data from the [start.gg](https://start.gg) GraphQL API, run seeding
score calculations, and return structured data for Claude to reason over.

## Setup

Requires `make` and Python 3.11+. All commands should be run from **Git Bash** (Windows) or a standard terminal (macOS).

**First time on a new machine:**
```bash
make install
```
This creates a `.venv` virtual environment and installs the package in editable mode. Safe to re-run — it skips venv creation if one already exists.

## Configuration

Copy `.env.example` to `.env` and fill in your start.gg API token:

```
STARTGG_TOKEN=your_token_here
```

## Development

| Command | What it does |
|---|---|
| `make install` | Create `.venv` and install dependencies |
| `make dev` | Launch the MCP Inspector to test tools interactively |
| `make test` | Run the test suite with pytest |
| `make` | Alias for `make dev` |

**Every session:**
```bash
make dev
```

This opens the MCP Inspector in your browser. Select a tool, provide inputs, and click Run to test it without needing a connected client.

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
