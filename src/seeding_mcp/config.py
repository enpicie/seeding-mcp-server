"""Application configuration.

Single responsibility: load and validate all environment variables and
configuration values. Every other module imports from here instead of
reading environment variables directly. Fails fast with a clear error
if a required variable is missing.
"""
