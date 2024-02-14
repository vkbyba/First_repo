from datetime import datetime

def input_date():
    while True:
        date_str = input("Enter the date in YYYY-MM-DD format: ")
        try:
            # Attempt to convert the string into a datetime object
            valid_date = datetime.strptime(date_str, "%Y-%m-%d")
            return valid_date
        except ValueError:
            # If the conversion fails, inform the user and prompt again
            print("This is not a valid date. Please try again.")

# Example usage
date = input_date()
print(f"The entered date is: {date.strftime('%Y-%m-%d')}")
