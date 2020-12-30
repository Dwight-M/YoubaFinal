import sys

from Library import *
import csv_access
import random

# Databases
DEST_DB = 'database/destinations_database.csv'
NUM_DB = 'database/numbers_database.csv'
DRV_DB = 'database/driver_database.csv'


def youba():
    """
    Handles the Customer side of the service

    Args:
        None

    Returns:
        None
    """
    print(strings.stars)
    print("*   Currently, there are only 4 Destinations that we cover.\n*   There will be more in the Future.")
    print("*   They are: UWI, Papine, Liguanea & Half-Way-Tree.")
    # TODO Change format string to Fstrings
    print(f"*   The price per trip is {fare} \n*   Discounts will be add where necessary.")

    print(strings.stars)
    print("*   Would you like to Request our services?")
    print("*   Enter 1 for Yes")
    print("*   Enter 0 for No\n")
    request = strings.validate_yesno_input()

    if request != 1:
        print("*    Would you like to exit YOUBA?")
        print("Enter 0 again to quit")
        cancel = strings.validate_yesno_input()
        if cancel == 0:
            sys.exit()
        request = 1
    # TODO Change Y and N to 1 and 0

    while request == 1:
        print(lines)
        # TODO change all phone numbers into Strings

        passenger_phone_num = validate_reconfirmation("Phone Number")
        passenger_location = validate_reconfirmation("Location")

        # TODO validate destination
        # while True:
        passenger_destination = validate_reconfirmation("Destination")
        # if passenger_destination in a_queue_list:
        #     break
        # else:
        #     print("*    Please enter a valid destination")

        request_taxi(passenger_phone_num, passenger_location,
                     passenger_destination, fare, known_passengers, a_queue_list)

        print("\n*   Would you like to Request our services again?")
        print("*   Enter 1 for Yes")
        print("*   Enter 0 for No")
        request = input()

    print(lines)
    print("Thank you for trying Youba. Please come again.\n")
    print("A list will be printed upon exit.")
    print("List of Drivers and Number of Jobs Completed.")

    for a_queue in a_queue_list:
        for driver in get_queue_contents(a_queue):
            print(get_first_name(driver) + "\t" + get_last_name(driver) + "\t" +
                  str(get_trips_completed(driver)))
    print(lines)
    print("*   List of Locations and Drivers for those that worked today.")
    print("* Current Location\tDriver Name\tCar Make & Model")

    for a_queue in a_queue_list:
        if not is_a_queue_empty(a_queue):
            driver = a_queue_front(a_queue)
            print("* " + get_location(a_queue) + "\t\t" + get_first_name(driver) + " " +
                  get_last_name(driver) + "\t\t" + get_make_and_model(driver))

    def make_av_queues():
        a_queue_UWI = make_availability_queue("UWI")
        a_queue_Papine = make_availability_queue("Papine")
        a_queue_Liguanea = make_availability_queue("Liguanea")
        a_queue_HalfWayTree = make_availability_queue("Half-Way-Tree")
        return (a_queue_UWI, a_queue_Papine, a_queue_Papine, a_queue_Liguanea, a_queue_HalfWayTree)

    def add_to_av_queues(a_queue_list):
        queues = make_av_queues()
        for queue in queues:
            add_a_queue(queue, a_queue_list)
        return a_queue_list