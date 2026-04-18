"""Seeding score calculations.

Single responsibility: pure functions that compute seeding scores and rankings
from player and tournament data. Takes structured data as input (no API calls)
and returns numeric scores or ranked lists. All logic is stateless and
independently testable.
"""
