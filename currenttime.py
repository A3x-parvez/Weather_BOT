import datetime

def get_current_hour():
    # Get the current time
    current_time = datetime.datetime.now()
    
    # Extract the current hour (0-23)
    current_hour = current_time.hour
    
    return current_hour

# Example usage
hour = get_current_hour()
print(hour)