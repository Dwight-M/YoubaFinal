#################################################################################
# Fair Calculation Section
#################################################################################

# Calculates the discount for a customer

# Function name too long, change to calc_dis
import csv_access
def calculate_discount(phone_num, passengers):
    """
    Calculates the discount to be applied for a customer

    Args:
        phone_num: Customers telephone number
        passengers: Dictionary of Customers information

    Returns:
        failed_attempts: A float value of discounted price
    """

    for number, failed_attempts in passengers.items():
        if number == phone_num:
            return failed_attempts * 0.10

    passengers[phone_num] = 0
    return 0.00


# Calculates the final fare for the customer

# Function name too long, change to calc_fare

def calculate_fare(phone_num, price, passengers):
    """
    Calculates the customers total fare after discount has been applied

    Args:
        phone_num: Customers telephone number
        price: The cost per taxi trip
        passengers: Dictionary of Customers information

    Returns:
        discounted_fare: Discounted price
    """

    discount = calculate_discount(phone_num, passengers)

    discounted_fare = price - (price * discount)

    # TODO Constants /Discount Table
    if discounted_fare < 0.00:
        return 0.00
    return discounted_fare