"""A client library for accessing Mitsubishi Motors Connected Services API (Kintaro & IDM)"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
