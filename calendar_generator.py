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
        m = self.month
        y = self.year
        if m<3:
            m += 12
            y -= 1
        q = 1
        K = y%100
        J = (y)//100
        h = ((q + 13*(m+1)//5+K + K//4 + J//4 - 2*J)%7)
        return (h+6)%7
    
    def build_grid_string(self):
        output = "Su Mo Tu We Th Fr Sa\n"
        first_day = self.get_start_day_of_month()
        total_days = self.get_days_in_month()

        for i in range(1,total_days+1):
            day_of_week = (first_day+i-1)%7
            if i == 1:
                output += '   '*first_day
            if day_of_week==0 and i != 1:
                output += '\n'
            output += f"{i:2d} "
        return output

    def generate_calendar(self):
        return 


check_leap_year = CalendarGenerator(2024,1)
#print(check_leap_year.is_leap_year())

days = CalendarGenerator(2024,5)
#print(days.get_days_in_month())

start_day = CalendarGenerator(2026,2)
#print(start_day.get_start_day_of_month())

grid = CalendarGenerator(2026,2)
print(grid.build_grid_string())
