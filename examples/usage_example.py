"""
Example usage script for the Time MCP.

This demonstrates how the Time MCP tools would be called and what they return.
"""

# Example 1: Get current time
# Tool: get_current_time()
# Output: "Current time: 14:30:45"

# Example 2: Get current date
# Tool: get_current_date()
# Output: "Current date: 2024-11-02"

# Example 3: Get current datetime
# Tool: get_current_datetime()
# Output: "Current date and time: 2024-11-02T14:30:45"

# Example 4: Get time components
# Tool: get_time_components()
# Output: "Year: 2024, Month: 11, Day: 2, Day of Week: Saturday, Time: 14:30:45"

# Example 5: Get Unix timestamp
# Tool: get_unix_timestamp()
# Output: "Current Unix timestamp: 1730534445"

print("Time MCP - Example Usage")
print("=" * 50)
print()
print("When integrated with Claude Desktop, you can ask:")
print()
print("1. 'What is the current time?'")
print("   -> Uses get_current_time()")
print()
print("2. 'What date is it today?'")
print("   -> Uses get_current_date()")
print()
print("3. 'Tell me the exact date and time.'")
print("   -> Uses get_current_datetime()")
print()
print("4. 'Break down the current time for me.'")
print("   -> Uses get_time_components()")
print()
print("5. 'What is the Unix timestamp right now?'")
print("   -> Uses get_unix_timestamp()")
print()
print("=" * 50)
print()
print("To test this MCP:")
print("1. Start the server: python src/server.py")
print("2. Use MCP Inspector: mcp dev src/server.py")
print("3. Or configure it in Claude Desktop")
