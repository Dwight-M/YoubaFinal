from Library import *
#################################################################################
# Taxi Section
#################################################################################

# Moves a Driver from one location to the other

# Parameter names to long, change to start_loc, end_loc
lines = "********************************************************************"
def move_taxi(start_location, end_location, a_queue_list):
    """
    Moves a taxi from one location to another with an Availability Queue list

    Args:
        start_location: Customers current location
        end_location: Customers desired destination
        a_queue_list: A list of Availability Queues

    Returns:
        None
    """
    if is_a_queue_empty(get_a_queue(start_location, a_queue_list)):
        print("*   No driver at location.\n")
    else:
        driver = a_queue_front(get_a_queue(start_location, a_queue_list))
        a_queue_dequeue(get_a_queue(start_location, a_queue_list))
        a_queue_enqueue(get_a_queue(end_location, a_queue_list), driver)
        increase_trips_completed(driver)


# Parameters names are long, can be changed to pass_num, pass_loc, pass_dest, ava_queue_lst

def request_taxi(passenger_phone_num, passenger_location, passenger_destination, price, passengers, a_queue_list):
    """
    Requests a taxi for a customer at a specific location

    Args:
        passenger_phone_num: Customers telephone number
        passenger_location: Customers current location
        passenger_destination: Customers desired destination
        price: Cost per trip
        passengers: A dictionary of customers and their failed attempts
        a_queue_list: A list of Availability Queues

    Returns:
       None
    """
    if passenger_location == passenger_destination:
        print("\n*\n*   Start and end locations are the same!\n*\n")
    else:
        # Fare for the trip is calculated
        trip_fare = calculate_fare(passenger_phone_num, price, passengers)
        print("*   Your final fare is ${}.".format(trip_fare))

        option = input(
            "*   Enter \"Y\" to confirm the trip or \"N\" to cancel - ")
        if option == "Y" or option == "y":
            if is_a_queue_empty(get_a_queue(passenger_location, a_queue_list)):
                passengers[passenger_phone_num] += 1
                print("\n*   Unfortunately, there are no drivers at that location.")
                print("*   We apologize for any inconvenience.")
                print("*   You will receive a 10% discount on your next trip.")
            else:
                print(lines)
                print("*   A Taxi is on the way.\n")
                print(lines)
                move_taxi(passenger_location,
                          passenger_destination, a_queue_list)
        else:
            print(lines)
            print("*   Cancelling trip")
            print(lines)
