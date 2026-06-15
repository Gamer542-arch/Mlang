class BridgeError(Exception):
    """Base exception for bridge errors."""

class ConnectionError(BridgeError):
    """Failed to connect to the bridge."""

class AuthError(BridgeError):
    """Authentication failed."""

class MethodNotFoundError(BridgeError):
    """Method not found on the server."""

class TimeoutError(BridgeError):
    """Request timed out."""
