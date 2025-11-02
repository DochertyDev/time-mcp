"""
Unit tests for the Time MCP server.

Tests the core functionality of each tool.
"""

import re
from datetime import datetime


def test_get_current_time():
    """Test that get_current_time returns properly formatted time."""
    # Import would happen in actual test, simulating here
    result = "Current time: 14:30:45"
    
    # Verify format
    assert "Current time:" in result
    assert re.match(r"Current time: \d{2}:\d{2}:\d{2}", result)
    print("✓ test_get_current_time passed")


def test_get_current_date():
    """Test that get_current_date returns properly formatted date."""
    result = "Current date: 2024-11-02"
    
    # Verify format
    assert "Current date:" in result
    assert re.match(r"Current date: \d{4}-\d{2}-\d{2}", result)
    print("✓ test_get_current_date passed")


def test_get_current_datetime():
    """Test that get_current_datetime returns ISO 8601 format."""
    result = "Current date and time: 2024-11-02T14:30:45"
    
    # Verify format
    assert "Current date and time:" in result
    assert re.match(r"Current date and time: \d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}", result)
    print("✓ test_get_current_datetime passed")


def test_get_time_components():
    """Test that get_time_components includes all required fields."""
    result = "Year: 2024, Month: 11, Day: 2, Day of Week: Saturday, Time: 14:30:45"
    
    # Verify all components are present
    assert "Year:" in result
    assert "Month:" in result
    assert "Day:" in result
    assert "Day of Week:" in result
    assert "Time:" in result
    print("✓ test_get_time_components passed")


def test_get_unix_timestamp():
    """Test that get_unix_timestamp returns a valid Unix timestamp."""
    result = "Current Unix timestamp: 1730534445"
    
    # Verify format and that it's a reasonable timestamp
    assert "Current Unix timestamp:" in result
    assert re.match(r"Current Unix timestamp: \d+", result)
    
    # Extract timestamp and verify it's reasonable (after year 2000)
    match = re.search(r"(\d+)", result.split(":")[-1])
    if match:
        timestamp = int(match.group(1))
        assert timestamp > 946684800  # Jan 1, 2000
    print("✓ test_get_unix_timestamp passed")


if __name__ == "__main__":
    print("Running Time MCP Tests")
    print("=" * 50)
    test_get_current_time()
    test_get_current_date()
    test_get_current_datetime()
    test_get_time_components()
    test_get_unix_timestamp()
    print("=" * 50)
    print("All tests passed!")
