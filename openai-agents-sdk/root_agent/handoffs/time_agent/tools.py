from datetime import datetime
from tzlocal import get_localzone

from agents import function_tool

@function_tool 
def get_current_time() -> str:
    local_tz = get_localzone()  # Dynamically gets your system's timezone
    now = datetime.now(local_tz)
    return f"The current time is: {now.strftime('%Y-%m-%d %H:%M:%S')} ({local_tz})"