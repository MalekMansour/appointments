# CONSTRUCTOR:
class Appointment:
    def __init__(self, day_of_week, start_time_hour):
        self.day_of_week = day_of_week
        self.start_time_hour = start_time_hour
        self.appt_type = 0
        self.client_name = ""
        self.client_phone = ""

# GETTERS:
    def get_appt_type_desc(self):
        appt_types = {
            0: "Available",
            1: "Mens Cut",
            2: "Ladies Cut",
            3: "Mens Colouring",
            4: "Ladies Colouring"
        }
        return appt_types.get(self.appt_type, "Unknown")

    def get_end_time_hour(self):
        return self.start_time_hour + 1
    
# SETTERS:
    def schedule(self, client_name, client_phone, appt_type):
        self.client_name = client_name
        self.client_phone = client_phone
        self.appt_type = appt_type

    def cancel(self):
        self.client_name = ""
        self.client_phone = ""
        self.appt_type = 0

    def format_record(self):
        return f"{self.client_name},{self.client_phone},{self.appt_type},{self.day_of_week},{self.start_time_hour:02}"

    def __str__(self):
        return f"{self.client_name.ljust(20)} {self.client_phone.ljust(15)} " \
               f"{self.day_of_week.ljust(10)} {self.start_time_hour:02}:00 - " \
               f"{self.get_end_time_hour():02}:00     {self.get_appt_type_desc()}"
