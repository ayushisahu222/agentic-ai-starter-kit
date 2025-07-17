from datetime import datetime

def current_time() -> str:
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"The current time is: {now}"
