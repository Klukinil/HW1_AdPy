from application.salary import calculate_salary
from application.db.people import get_employees
import datetime

def actual_date():
    current_date = datetime.date.today()
    return current_date


if __name__ == '__main__':
    print(actual_date())
    calculate_salary()
    get_employees()
