import datetime
from datetime import datetime, timedelta


def get_days_from_today():
    while True:
        try:
            date_str=input('input data in format YYYY-MM-DD ')
            formated_date=datetime.strptime(date_str,'%Y-%m-%d')
            print(formated_date)
            break
        except ValueError:
            print('Incorrect input, pls follow order')
    
    today=datetime.now()
    delta= today-formated_date
    return delta.days



get_delta = print(get_days_from_today())