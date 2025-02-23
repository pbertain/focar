from datetime import datetime

def generate_date():
    # Get the current date and time
    current_date = datetime.now()
    
    # Format the date
    formatted_date = current_date.strftime("%Y-%m-%d")
    
    return formatted_date

if __name__ == "__main__":
    print(generate_date())

