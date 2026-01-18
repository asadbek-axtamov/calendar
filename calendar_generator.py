class CalendarGenerator:
    def __init__(self, year, month):
        self.year = year
        self.month = month

    def is_leap_year(y1):
        if y1.year % 400 != 0 and y1.year % 100 == 0:
            return False
        elif y1.year % 4 != 0:
            return False
        else:
            return True
    
    def get_days_in_month(self):
        return 
    
    def get_start_day_of_month(self):
        return 
    
    def build_grid_string(self):
        return

    def generate_calendar(self):
        return 


check_leap_year = CalendarGenerator(2024, 1)
print(check_leap_year.is_leap_year())

