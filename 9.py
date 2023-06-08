from datetime import datetime, timedelta

def check_date_difference(from_date, to_date, difference):
    # Convert the date strings to datetime objects
    from_date_obj = datetime.strptime(from_date, '%y-%m-%d')
    to_date_obj = datetime.strptime(to_date, '%y-%m-%d')

    # Calculate the difference between the dates in days
    date_difference = abs((to_date_obj - from_date_obj).days)

    # Check if the date difference is less than the specified number of days
    if date_difference < difference:
        return True
    else:
        return False

from_date = '21-06-01'
to_date = '21-06-15'
difference = 10

result = check_date_difference(from_date, to_date, difference)
print(result)

