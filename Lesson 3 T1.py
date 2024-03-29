from datetime import datetime

def input_date():
    while True:
        date_str = input("Enter the date in YYYY-MM-DD format: ")
        try:
            valid_date = datetime.strptime(date_str, "%Y-%m-%d")
            return valid_date
        except ValueError:
            print("This is not a valid date. Please try again.")

date = input_date()

current_date = datetime.now()

days_since = (current_date - date).days
print(days_since)

