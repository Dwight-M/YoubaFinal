#################################################################################
"""
Youba Ltd. is a startup company that aims to revolutionize the local public transportation by
introducing a brand new way for travellers to connect with drivers. Users only need
to have a cellphone to utilize the service. Given your knowledge of ADTs, Youba Ltd.
has contracted you to implement the platform for their service.
"""

from Library import *
import csv_access

# Databases
DEST_DB = 'database/destinations_database.csv'
NUM_DB = 'database/numbers_database.csv'
DRV_DB = 'database/driver_database.csv'

1

#################################################################################
# Main Section
#################################################################################


# dest_db = 'database/destinations_database.csv'
# num_db = 'database/numbers_database.csv'
queue_dict = {}
# with open(dest_db) as f:
#     reader = csv.reader(f)
#     header_row = next(reader)
#     destinations = []
#     for row in reader:
#         destinations.append(row[1])
# with open(num_db) as f:
#     reader = csv.reader(f)
#     header_row = next(reader)
#     numbers = {}
#     for row in reader:
#         numbers[row[0]] = row[1]
#
#
# def make_av_queues():
#     for destination in destinations:
#         queue_dict[destination] = queue.make_availability_queue(destination)
#     return queue_dict
#
#
# def add_to_av_queues(a_queue_list):
#     return make_av_queues()
#
# def add_destination(loc):
#     with open(destination, 'a') as f:
#         f.write(loc)


# TODO Make each section its own .py file
# TODO Run Pycharm's code analyzer

def delete_entry(, entry):
    id = int(input(strings.delete_driver_prompt))
    # Load Driver from database
    driver = csv_access.get_item(DRV_DB, drv_id)
    print(driver)
    entry = int(input(strings.delete_driver_final))
    if entry == 1:
        csv_access.delete_item(DRV_DB, drv_id)
        print(strings.delete_confirmation)


if __name__ == '__main__':
    # Main Menu Loop
    while True:
        print(strings.main_menu)
        entry = int(input())

        # Driver Menu
        if entry == 1:
            while True:
                entry = int(input(strings.driver_menu))

                # Show All Drivers
                if entry == 1:
                    drivers = csv_access.get_all_items(DRV_DB)
                    print(strings.all_drivers_format)
                    for drv_id, driver in drivers.items():
                        print(drv_id, ' : ', driver)
                    input(strings.continue_prompt)

                # Add Driver(s)
                elif entry == 2:
                    drivers = int(input("Enter the number of drivers you would like to add:\n"))
                    if drivers > 0:
                        for i in range(drivers):
                            f_name = input("Please enter the new driver's first name\n")
                            l_name = input("Please enter the new driver's last name\n")
                            model = input("Please enter the new driver's vehicle model\n")
                            make = input("Please enter the new driver's vehicle make\n")
                            car = f"{model}|{make}"
                            new_driver = [f_name, l_name, car, 0]
                            csv_access.insert_item(DRV_DB, new_driver)
                            print(f"{new_driver} has been successfully added")
                            print(f"Now adding Driver #{i + 1}")

                # Edit Driver
                elif entry == 3:
                    drv_id = int(input(strings.edit_driver_prompt))
                    # Driver ID entered
                    if drv_id != 0:
                        # Load Driver from database
                        driver = csv_access.get_item(DRV_DB, drv_id)
                        print(strings.edit_driver_current)
                        print(driver)
                        entry = int(input(strings.edit_driver_select_prompt))

                        # Editing First Name
                        if entry == 1:
                            edit = strings.validate_reconfirmation("First Name")
                            driver[0] = edit
                            csv_access.edit_item(DRV_DB, drv_id, driver)
                            print(strings.saved_confirmation)

                        # Editing Last Name
                        elif entry == 2:
                            edit = strings.validate_reconfirmation("Last Name")
                            driver[1] = edit
                            csv_access.edit_item(DRV_DB, drv_id, driver)
                            print(strings.saved_confirmation)
                        # Editing Car Make|Model
                        elif entry == 3:
                            edit = strings.validate_reconfirmation("Car Make|Model")
                            driver[2] = edit
                            csv_access.edit_item(DRV_DB, drv_id, driver)
                            print(strings.saved_confirmation)
                        # Editing Number of Trips Completed
                        elif entry == 4:
                            edit = strings.validate_reconfirmation("Number of Trips Completed")
                            driver[3] = edit
                            csv_access.edit_item(DRV_DB, drv_id, driver)
                            print(strings.saved_confirmation)
                        # Editing Entire Driver
                        elif entry == 5:
                            edit = strings.validate_reconfirmation(
                                "[First Name, Last Name, Vehicle, Number of Trips Completed]")
                            driver = edit
                            csv_access.edit_item(DRV_DB, drv_id, driver)
                            print(strings.saved_confirmation)

                # Delete Driver
                elif entry == 4:
                    drv_id = int(input(strings.delete_driver_prompt))
                    # Load Driver from database
                    driver = csv_access.get_item(DRV_DB, drv_id)
                    print(driver)
                    entry = int(input(strings.delete_destination_final))
                    if entry == 1:
                        csv_access.delete_item(DRV_DB, drv_id)
                        print(strings.delete_confirmation)
                break

        # Destinations Menu
        if entry == 2:
            while True:
                entry = int(input(strings.destinations_menu))
                # Show all Destinations
                if entry == 1:
                    destinations = csv_access.get_all_items(DEST_DB)
                    print(strings.all_dest_format)
                    for dest_id, destination in destinations.items():
                        print(dest_id, ' : ', destination)
                    input(strings.continue_prompt)

                # Add Destination
                elif entry == 2:
                    dests = int(input("Enter the number of destinations you would like to add:\n"))
                    if dests > 0:
                        for i in range(dests):
                            new_dest = input("Please enter the name of the new destination")
                            csv_access.insert_item(DRV_DB, new_dest)
                            print(f"{new_dest} has been successfully added")


                # Rename Destination
                elif entry == 3:
                    dest_id = int(input(strings.rename_dest_prompt))
                    # Driver ID entered
                    if dest_id != 0:
                        # Load Driver from database
                        destination = csv_access.get_item(DEST_DB, dest_id)
                        print(strings.current_rename)
                        print(destination)
                        destination = strings.validate_reconfirmation("Destination")
                        csv_access.edit_item(DEST_DB, dest_id, destination)
                        print(strings.saved_confirmation)
                # Delete Destination
                elif entry == 4:
                    dest_id = int(input(strings.delete_dest_prompt))
                    # Load Destination from database
                    destination = csv_access.get_item(DEST_DB, dest_id)
                    print(destination)
                    entry = int(input(strings.delete_driver_final))
                    if entry == 1:
                        csv_access.delete_item(DEST_DB, dest_id)
                        print(strings.delete_confirmation)

                break
        # Customers Menu
        if entry == 3:
            while True:
                entry = int(input(strings.customers_menu))
                # Show all Customers
                if entry == 1:
                    destinations = csv_access.get_all_items(DEST_DB)
                    print(strings.all_dest_format)
                    for dest_id, destination in destinations.items():
                        print(dest_id, ' : ', destination)
                    input(strings.continue_prompt)

                # Add Destination
                elif entry == 2:
                    dests = int(input("Enter the number of destinations you would like to add:\n"))
                    if dests > 0:
                        for i in range(dests):
                            new_dest = input("Please enter the name of the new destination")
                            csv_access.insert_item(DRV_DB, new_dest)
                            print(f"{new_dest} has been successfully added")

                # Rename Destination
                elif entry == 3:
                    dest_id = int(input(strings.rename_dest_prompt))
                    # Driver ID entered
                    if dest_id != 0:
                        # Load Driver from database
                        destination = csv_access.get_item(DEST_DB, dest_id)
                        print(strings.current_rename)
                        print(destination)
                        destination = strings.validate_reconfirmation("Destination")
                        csv_access.edit_item(DEST_DB, dest_id, destination)
                        print(strings.saved_confirmation)
                # Delete Destination
                elif entry == 4:
                    dest_id = int(input(strings.delete_dest_prompt))
                    # Load Driver from database
                    destination = csv_access.get_item(DEST_DB, dest_id)
                    print(destination)
                    entry = int(input(strings.delete_driver_final))
                    if entry == 1:
                        csv_access.delete_item(DEST_DB, dest_id)
                        print(strings.delete_confirmation)

                break








        # # Makes new Availability Queues
        #
        # # A list of queues
        # a_queue_list = make_av_queues()  # TODO Generate a list of Availability Queues
        # # A dictionary of customers and their failed attempts
        # known_passengers = numbers
        #
        # # Adds to the list of Available Queues
        # # TODO Automate this or allow user to customize
        # add_to_av_queues(a_queue_list)
        #
        # # Represent the number of Drivers to create
        # print(lines)
        # print("*   Please enter the number of new Drivers you hired.")
        # print("*   Our travel locations are: UWI, Papine, Liguanea & Half-Way-Tree.")
        # # TODO Read from file all travel locations and display - replace the line above
        # no_of_drivers = int(input())
        # driver_lst =[]
        # # Creates the Drivers with input information
        # for i in range(no_of_drivers):
        #     print(
        #         "*   Enter the Drivers information.\n*   In the format - \"FirstName, LastName, CarMake|Model, LocationDestination\"")
        #
        #     driver_info = input().strip().split(",")
        #     # Driver ADT is created
        #     driver = make_new_driver(
        #         driver_info[0], driver_info[1], driver_info[2])
        #     driver_lst.append(driver)
        #     # Driver gets added to a location
        #     a_queue_enqueue(get_a_queue(driver_info[3], a_queue_list), driver)
        #     print("\n" + lines)
        # print("What would you like to do?")
        # print("1:   Manage Drivers\n 2:  Manage Locations\n3:    Manage Rates\n 4:  Manage Customers.")
        # choice = int(input())
        #
        # no_of_known_passengers = int(input())
        #
        # for i in range(no_of_known_passengers):
        #     print("\n*   In the format \"#######,Failed-trips\"")
        #     print(f"*   Please enter the 7-digit phone number for Passenger {i + 1} and the number of Failed Attempts: ")
        #     passenger = list(map(int, input().strip().split(",")))
        #     key = passenger[0]
        #     value = passenger[1]
        #     known_passengers[key] = value
        #
        # # Cost price per travel
        # fare = float(input("\n*   Please enter the price for a single travel: $"))
        #
        # print("\n" + lines + "\n" + lines)
        # print("*   Setup now completed.")
        # print("*   Moving on into the User side.")
        # print(lines + "\n")
        # youba()

#################################################################################
#################################################################################