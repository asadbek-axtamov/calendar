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
    


check_leap_year = CalendarGenerator(2024, 1)
print(check_leap_year.is_leap_year())
