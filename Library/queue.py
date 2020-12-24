#################################################################################
# Availability Queue Section
#################################################################################

# Function name too long, change to mk_ava_queue

def make_availability_queue(location):
    """
    Creates an Availability Queue

    Args:
        location: A location

    Returns:
        a_queue: An Availability Queue ADT
    """
    a_queue = ("AvailabilityQueue", [])
    return a_queue


def get_queue_contents(a_queue):
    """
    Gets Availability Queue contents

    Args:
        a_queue: An Availability Queue ADT

    Returns:
        queue_contents: The list of Drivers at an Availability Queue
    """
    queue_contents = a_queue[2]
    return queue_contents


def get_a_queue(location_name, a_queue_list):
    """
    Gets the Availability Queue from the list based on location

    Args:
        location_name: A location
        a_queue_list: A list of Availability Queues

    Returns:
        a_queue: An Availability Queue ADT
    """
    for a_queue in a_queue_list:
        if get_location(a_queue) == location_name:
            return a_queue
    print("There are no Availability Queues for this location.")
    return make_availability_queue("")


def is_a_queue(a_queue):
    """
    Check if an Availability Queue is empty/ doesn't exist.
    This is separate from an availability queue not having drivers.

    Args:
        a_queue: An Availability Queue ADT

    Returns:
        boolean: True or False
    """
    if get_location(a_queue) == "":
        return False
    return True


def get_location(a_queue):
    """
    Gets the Availability Queue location name

    Args:
        a_queue: An Availability Queue ADT

    Returns:
        location: The location of an Availability Queue
    """
    location = a_queue[1]
    return location


def a_queue_front(a_queue):
    """
    Returns the first Driver in the Availability Queue list

    Args:
        a_queue: An Availability Queue ADT

    Returns:
        driver: An ADT representing a Driver
    """
    if is_a_queue_empty(a_queue):
        print("\nThere are no Taxi Drivers present at the moment.\n")
        return make_availability_queue("")
    else:
        return get_queue_contents(a_queue)[0]


def a_queue_enqueue(a_queue, driver):
    """
    Adds a driver to an Availability Queue list

    Args:
        a_queue: An Availability Queue ADT
        driver: A Driver ADT

    Returns:
        None
    """
    get_queue_contents(a_queue).append(driver)


def a_queue_dequeue(a_queue):
    """
    Removes a driver from an Availability Queue list

    Args:
        a_queue: An Availability Queue ADT

    Returns:
        None
    """
    if is_a_queue_empty(a_queue):
        print("\nERROR.\nThere are no Drivers at this Location to remove.\n")
    else:
        get_queue_contents(a_queue).pop(0)


def is_a_queue_empty(a_queue):
    """
    Checks to see if an Availability Queue is Empty

    Args:
        a_queue: An Availability Queue ADT

    Returns:
        boolean: True or False
    """
    if get_queue_contents(a_queue) == []:
        return True
    return False


def add_a_queue(a_queue, a_queue_list):
    """
    Adds an Availability Queue to the list of Availability Queues

    Args:
        a_queue: An Availability Queue ADT
        a_queue_list: A list of Availability Queues

    Returns:
        None
    """
    a_queue_list.append(a_queue)


def remove_a_queue(a_queue, a_queue_list):
    """
    Removes an Availability Queue from the list of Availability Queues

    Args:
        a_queue: An Availability Queue ADT
        a_queue_list: A list of Availability Queues

    Returns:
        None
    """
    x = -1
    for i in range(len(a_queue_list)):
        if a_queue_list[i] == a_queue:
            x = i
            break

    if x != -1:
        a_queue_list.pop(x)
    else:
        print("There are no Availability Queues for this location.\n")