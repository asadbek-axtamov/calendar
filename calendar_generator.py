class CalendarGenerator:
    def __init__(self, year, month):
        self.year = year
        self.month = month

    def is_leap_year(self):
        if self.year % 400 != 0 and self.year % 100 == 0:
            return False
        elif self.year % 4 != 0:
            return False
        else:
            return True
    
    def get_days_in_month(self):
        months = {
            1:31,
            2:28,
            3:31,
            4:30,
            5:31,
            6:30,
            7:31,
            8:31,
            9:30,
            10:31,
            11:30,
            12:31
            }
        if self.month==2:
            return months[self.month]+int(self.is_leap_year())
        return months[self.month]
    
    def get_start_day_of_month(self):
        return 
    
    def build_grid_string(self):
        return

    def generate_calendar(self):
        return 


check_leap_year = CalendarGenerator(2024, 1)
#print(check_leap_year.is_leap_year())

days = CalendarGenerator(2024,5)
print(days.get_days_in_month())
