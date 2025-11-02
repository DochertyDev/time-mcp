"""
Time MCP Server

A simple Model Context Protocol server that provides tools to fetch the current
date and time from the system. This MCP only accesses time-related information
and no other system data.
"""

from datetime import datetime
from mcp.server.fastmcp import FastMCP, Context

# Create a named server
mcp = FastMCP("time-mcp")


@mcp.tool()
def get_current_time() -> str:
    """
    Get the current time from the system.
    
    Returns the current time in HH:MM:SS format (24-hour).
    
    Returns:
        str: Current time in HH:MM:SS format
    """
    try:
        now = datetime.now()
        time_str = now.strftime("%H:%M:%S")
        return f"Current time: {time_str}"
    except Exception as e:
        return f"Error retrieving time: {str(e)}"


@mcp.tool()
def get_current_date() -> str:
    """
    Get the current date from the system.
    
    Returns the current date in YYYY-MM-DD format.
    
    Returns:
        str: Current date in YYYY-MM-DD format
    """
    try:
        now = datetime.now()
        date_str = now.strftime("%Y-%m-%d")
        return f"Current date: {date_str}"
    except Exception as e:
        return f"Error retrieving date: {str(e)}"


@mcp.tool()
def get_current_datetime() -> str:
    """
    Get the current date and time from the system.
    
    Returns both the current date and time in ISO 8601 format.
    
    Returns:
        str: Current date and time in ISO 8601 format (YYYY-MM-DDTHH:MM:SS)
    """
    try:
        now = datetime.now()
        datetime_str = now.strftime("%Y-%m-%dT%H:%M:%S")
        return f"Current date and time: {datetime_str}"
    except Exception as e:
        return f"Error retrieving date and time: {str(e)}"


@mcp.tool()
def get_time_components() -> str:
    """
    Get detailed breakdown of the current time components.
    
    Returns individual components like year, month, day, hour, minute, and second.
    Useful for understanding the full temporal context.
    
    Returns:
        str: JSON-formatted string with time components
    """
    try:
        now = datetime.now()
        components = {
            "year": now.year,
            "month": now.month,
            "day": now.day,
            "hour": now.hour,
            "minute": now.minute,
            "second": now.second,
            "day_of_week": now.strftime("%A"),
            "weekday_number": now.weekday()
        }
        
        # Format as readable string
        result = (
            f"Year: {components['year']}, "
            f"Month: {components['month']}, "
            f"Day: {components['day']}, "
            f"Day of Week: {components['day_of_week']}, "
            f"Time: {components['hour']:02d}:{components['minute']:02d}:{components['second']:02d}"
        )
        return result
    except Exception as e:
        return f"Error retrieving time components: {str(e)}"


@mcp.tool()
def get_unix_timestamp() -> str:
    """
    Get the current Unix timestamp (seconds since epoch).
    
    Useful for system-level time operations and comparisons.
    
    Returns:
        str: Current Unix timestamp
    """
    try:
        now = datetime.now()
        timestamp = int(now.timestamp())
        return f"Current Unix timestamp: {timestamp}"
    except Exception as e:
        return f"Error retrieving Unix timestamp: {str(e)}"


def main():
    """Main entry point for the time-mcp server."""
    mcp.run()


if __name__ == "__main__":
    main()
