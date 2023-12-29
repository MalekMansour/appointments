import appointment as ap
import os

# Variables
DASH_36 = "=" * 36
DASH_90 = "-" * 90
VALID_SELECTION = ['1', '2', '3', '4', '9']
VALID_APPOINTMENT_TYPE = [1, 2, 3, 4]
WORKING_DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

# Function 1: Create Weekly Calendar
def create_weekly_calendar(appt_list):
    for day in WORKING_DAYS:
        for hour in range(9, 17):
            appointment = ap.Appointment(day, hour)
            appt_list.append(appointment)
    print("Weekly calendar created")

# Function 2: Load the appointments1.csv with 3 schedules by default
def load_scheduled_appointments(appt_list):
    filename = input("Enter appointment filename: ")
    while filename != "appointments1.csv":
        filename = input("File not found. Re-enter appointment filename: ")
    file = open("appointments1.csv", "r")
    number_of_scheduled_appointments = 0

    for line in file:
        values = line.rstrip().split(",")
        name = values[0]
        phone_number = values[1]
        appt_type = int(values[2])
        day = values[3]
        start_time = int(values[4])
        appointments = find_appointment_by_time(appt_list, day, start_time)
        if appointments is not None:
            appointments.schedule(name, phone_number, appt_type)
            number_of_scheduled_appointments += 1

    file.close()
    return number_of_scheduled_appointments

# Function 3: This is the print screen where user can input his selection.
def print_menu():
    print("Jojo's Hair Salon Appointment Manager")
    print(DASH_36)
    print(" 1) Schedule an appointment")
    print(" 2) Find appointment by name")
    print(" 3) Print calendar for a specific day")
    print(" 4) cancel an appointment")
    print(" 9) Exit the system")
    selection = input("Enter your selection: ")

    while selection not in VALID_SELECTION:
        print("Invalid selection! Please try again.")
        selection = input("Enter your selection: ")
    print()
    return int(selection)

# Function 4: Checks the appointment using the time of the day (24h)
def find_appointment_by_time(appt_list, day, start_time):
    for appointment in appt_list:
        if (
            appointment.day_of_week == day.lower().capitalize()
            and appointment.start_time_hour == start_time
        ):
            return appointment

# Function 5: Finds and prints appointments whose client names contain the specified name.
def show_appointments_by_name(appt_list, name):
    matching_appointments = []
    for appointment in appt_list:
        if name.upper() in appointment.client_name.upper():
            matching_appointments.append(appointment)
            print(appointment)

    return matching_appointments


# Function 6: Finds and prints appointments using the day (days of the week).
def show_appointments_by_day(appt_list, day):
    for appointment in appt_list:
        if day.capitalize() in appointment.day_of_week:
            print(appointment)

# Function 7: Saves the scheduled appointments.
def save_scheduled_appointments(appt_list):
    nbr_of_saved_appointment = 0
    file_name = input("Enter a file name: ")
    file_path = os.path.join("", file_name)
    file_overwrite = True

    while os.path.isfile(file_path) and file_overwrite:
        overwrite = input("File already exists. Do you want to overwrite it? (Y/N): ").upper()
        while overwrite not in ("Y", "N"):
            overwrite = input("Invalid input. Do you want to overwrite it? (Y/N): ").upper()

        if overwrite == "Y":
            file_overwrite = False
        elif overwrite == "N":
            file_name = input("Enter a different file name: ")
            file_path = os.path.join("", file_name)

    file_name_f = open(file_path, "w")
    for appointment in appt_list:
        if 0 != appointment.appt_type and appointment.appt_type in (1, 2, 3, 4):
            file_name_f.write(appointment.format_record() + "\n")
            nbr_of_saved_appointment += 1
    file_name_f.close()
    print(f"{nbr_of_saved_appointment} sheduled appointments have been successfully saved")

# Main Function
def main():
    appt_list = []

    print("Starting the Appointment Manager System")
    create_weekly_calendar(appt_list)
    load_schedule_appointments_option = input("Would you like to load previously scheduled appointments from a file (Y/N)? ")

    while load_schedule_appointments_option.upper() not in ("Y", "N"):
        load_schedule_appointments_option = input("Would you like to load previously scheduled appointments from a file (Y/N)? ")

    if load_schedule_appointments_option.upper() == "Y":
        loaded_appointments = load_scheduled_appointments(appt_list)
        print(f"{loaded_appointments} previously scheduled appointments have been loaded")
        print()
        print()
    else:
        print()
        print()

    selection = print_menu()

    while selection != 9:
        if selection == 1:
            print("** Schedule an appointment **")

            day = input("What day: ")
            start_hour = int(input("Enter start hour (24-hour clock): "))

            found = False
            index = 0

            while index < len(appt_list) and not found:
                current_appointment = appt_list[index]

                if current_appointment.day_of_week == day.capitalize() and current_appointment.start_time_hour == start_hour and current_appointment.appt_type == 0:
                    found = True
                index += 1

            if found:
                client_name = input("Client Name: ")
                client_phone = input("Client Phone: ")

                print("Appointment types")
                print("1: Mens Cut $50, 2: Ladies Cut $80, 3: Mens Colouring $50, 4: Ladies Colouring $120")

                type_of_appointment = int(input("Type of Appointment: "))

                if type_of_appointment in VALID_APPOINTMENT_TYPE:
                    current_appointment.schedule(client_name.capitalize(), client_phone, type_of_appointment)
                    print(f"Ok, {client_name.capitalize()}'s appointment is scheduled!")

                else:
                    print("Sorry, that is not a valid appointment type!")

            elif day.capitalize() not in WORKING_DAYS or start_hour not in range(9, 17):
                print("Sorry, that time slot is not in the weekly calendar")

            else:
                print("Sorry, that time slot is booked already!")

        elif selection == 2:
            print('** Find appointment by name **')
            client_name = input("Enter Client Name: ")
            print(f"Appointments for {client_name}")
            print()
            print("{:20s}{:15s}{:10s}{:10s}{:10s}{:20s}".format("Client Name", "Phone", "Day", "Start", "End", "Type"))
            print(DASH_90)

            named_appointments = show_appointments_by_name(appt_list, client_name)
            if not named_appointments:
                print("No appointments found.")

        elif selection == 3:
            print('** Print calendar for a specific day **')
            day = input("Enter the day of week: ")
            print(f"Appointments for {day}")
            print()
            print("{:20s}{:15s}{:10s}{:10s}{:10s}{:20s}".format("Client Name", "Phone", "Day", "Start", "End", "Type"))
            print(DASH_90)

            show_appointments_by_day(appt_list, day)

        elif selection == 4:
            print('** Cancel an appointment **')
            day = input("What day: ")
            start_hour = int(input("Enter start hour (24-hour clock): "))

            found = False 
            index = 0
            while index < len(appt_list) and not found:
                current_appointment = appt_list[index]

                if current_appointment.day_of_week == day.capitalize() and current_appointment.start_time_hour == start_hour and current_appointment.appt_type != 0:
                    found = True
                index += 1

            if found:
                print("Appointment: {} {} - {} for {} has been cancelled!".format(current_appointment.day_of_week, str(current_appointment.start_time_hour).zfill(2) + ":00", str(current_appointment.get_end_time_hour()).zfill(2) + ":00", current_appointment.client_name))
                current_appointment.cancel()

            elif day.capitalize() not in WORKING_DAYS or start_hour not in range(9, 17):
                print("Sorry, that time slot is not in the weekly calendar")

            else:
                print("That time slot isn't booked and doesn't need to be cancelled")

        print()
        selection = print_menu()

    print("** Exit the system **")
    save_option = input("Would you like to save all scheduled appointments to a file (Y/N)? ")

    while save_option.upper() not in ('Y', 'N'):
        print("Invalid Option! Please try again")
        save_option = input("Would you like to save all scheduled appointments to a file (Y/N)? ")

    if save_option.upper() == 'Y':
        save_scheduled_appointments(appt_list)
        print("Good Bye!")

    else:
        print("Good Bye!")

if __name__ == "__main__":
    main()
