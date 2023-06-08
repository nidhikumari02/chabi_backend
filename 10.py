from datetime import datetime, timedelta

def get_date_before(date, n):
    return (datetime.strptime(date, '%y-%m-%d') - timedelta(days=n)).strftime("'%y-%m-%d'")

date = '16-12-10'
n = 11

result = get_date_before(date, n)
print(result)

