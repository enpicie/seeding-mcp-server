"""start.gg API client.

Single responsibility: all network communication with the start.gg GraphQL API.
Fetches player profiles, tournament entrants, set results, and seeding data.
No scoring logic lives here — raw API responses are returned as-is for
callers to interpret.
"""
