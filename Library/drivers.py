
#################################################################################
# Driver Section
#################################################################################


# Parameter names are long, can be shortened to f_name, l_name, car_mk_mod
def make_new_driver(first_name, last_name, car_make_and_model):
    """
    Constructs an ADT for a new Driver

    Args:
        first_name: Drivers first name
        last_name: Drivers last name
        car_make_and_model: Drivers car make and model

    Returns:
        driver: A Driver ADT
    """
    trips_completed = 0
    return ("Driver", [first_name, last_name, car_make_and_model,
                       trips_completed])


def make_driver(first_name, last_name, car_make_and_model, trips_completed):
    """
    Constructs an ADT for an existing Driver

    Args:
        first_name: Drivers first name
        last_name: Drivers last name
        car_make_and_model: Drivers car make and model
        trips_completed: Number of trips made per day

    Returns:
        driver: A Driver ADT
    """
    return ("Driver", [first_name, last_name, car_make_and_model,
                       trips_completed])


def is_driver(driver):
    """
    Determines whether an object is a Driver

    Args:
        driver: A Driver ADT

    Returns:
        boolean: True or False
    """
    if len(driver) == 2 and driver[0] == "Driver":
        driver_info = get_driver_info(driver)
        if type(driver_info) == type([]) and len(driver_info) == 4:
            return True
    return False


def get_driver_info(driver):
    """
    Gets the list of Driver details

    Args:
        driver: A Driver ADT

    Returns:
        driver_info: list of Driver information
    """
    driver_info = driver[1]
    return driver_info


# Gets the Drivers first name


def get_first_name(driver):
    """


    Args:
        driver: A Driver ADT

    Returns:
        f_name: Drivers first name
    """
    f_name = get_driver_info(driver)[0]
    return f_name


def get_last_name(driver):
    """
    Gets the Drivers last name

    Args:
        driver: A Driver ADT

    Returns:
        l_name: Drivers last name
    """
    l_name = get_driver_info(driver)[1]
    return l_name


def get_make_and_model(driver):
    """
    Gets the Drivers car make and model

    Args:
        driver: A Driver ADT

    Returns:
        make_model: Drivers care make and model
    """
    make_model = get_driver_info(driver)[2]
    return make_model


def change_make_and_model(driver, new_make_model):
    """
    Updates the Drivers car make and model

    Args:
        driver: A Driver ADT

    Returns:
        None
    """
    if is_driver(driver):
        driver_info = get_driver_info(driver)
        driver_info[2] = new_make_model
    else:
        print("*\n*   ERROR: ")
        print("*   Didn't receive a Driver\n")


def get_trips_completed(driver):
    """
    Gets the Drivers number of trips completed for the day

    Args:
        driver: A Driver ADT

    Returns:
        trips: Drivers total trips completed
    """
    trips = get_driver_info(driver)[3]
    return trips


# Function name too long, change to inc_trips_done

def increase_trips_completed(driver):
    """
    Increases the number of trips a Driver makes

    Args:
        driver: A Driver ADT

    Returns:
        None
    """
    driver_info = get_driver_info(driver)
    driver_info[3] = get_trips_completed(driver) + 1


def is_driver_new(driver):
    """
    Determines whether a Driver is new or not

    Args:
        driver: A Driver ADT

    Returns:
        boolean: True or False
    """
    num = get_trips_completed(driver)
    if num == 0:
        return True
    return False

