stars = "********************************************************************"
main_menu = f"{stars}" \
            "\n*   Welcome to the Admin side of Youba. Please enter the the number of what you would like to do:" \
            "\n\t1. Manage Drivers" \
            "\n\t2. Manage Destinations " \
            "\n\t3. Manage Customers' Numbers" \
            f"\n{stars}" \
            "\n"


# Generalised Strings
continue_prompt = "Press ENTER to continue"
saved_confirmation = "Changes have been saved"
delete_confirmation = "Deletion complete"

# Format Strings
entity_number = "Please enter the number of {entities} you would like to add:\n"
entity_confirm = "Please press 1 to confirm that this is the {entity} you wish to {action}:"
id_prompt = "Please enter the ID of the {entity} you wish to {action}:" \
                       " Or enter 0 to go back to the {entity} Menu\n"
add_success = "{new_entity} has been successfully added\n"
now_adding = "Now adding {entity} #{entity_number}\n"
new_entity_prompt = "Please enter the name of the new {entity}\n"
all_entities = "Here are all {entities} in the format:" \
                  "\nID : {Entity}"
cancel_confirm = "Cancelling {action}. Returning to {entity} menu\n"
# Driver Strings
driver_menu = f"{stars}" \
              "\n*   Welcome to the Driver Management Menu. Please select an action. Enter any other number to go back " \
              "to the main menu" \
              "\n\t1. View All Drivers" \
              "\n\t2. Add New Driver " \
              "\n\t3. Edit Driver " \
              "\n\t4. Delete Driver " \
              "\n\n\t<-- Back\n"
all_drivers = "Here are all drivers in the format:" \
                     "\nID : [First Name, Last Name, Vehicle, Number of Trips Completed]"

edit_driver_prompt = "Please enter the ID of the driver you wish to change. Or enter 0 to go back to the Driver Menu\n"
edit_driver_current = "This is the driver you are currently editing:"

edit_driver_select_prompt = "What part of the driver would you like to edit " \
                            "\n1. First Name " \
                            "\n2. Last Name " \
                            "\n3. Car " \
                            "\n4. Trips Completed" \
                            "\n5. Entire Driver\n"
delete_driver_prompt = "Please enter the ID of the driver you wish to delete." \
                       " Or enter 0 to go back to the Driver Menu\n"

delete_driver_final = "This is the driver you are about to delete. Press 1 to confirm, enter any key to go back"

driver_name_prompt = "Please enter the new driver's {cardinal} name\n"
driver_vehicle_prompt = "Please enter the new driver's vehicle {type}\n"
delete_destination_final = \
    "This is the destination you are about to delete. Press 1 to confirm, enter any key to go back"

# Destination Strings
destinations_menu = f"{stars}" \
                    "\n*   Welcome to the Destinations Management Menu. Please select an action." \
                    " Enter any other number to go back to the main menu" \
                    "\n\t1. View All Destinations" \
                    "\n\t2. Add Destination " \
                    "\n\t3. Rename Destination " \
                    "\n\t4. Delete Destination " \
                    "\n\n\t<-- Back\n"

customers_menu = f"{stars}" \
                 "\n*   Welcome to the Customers' Number Management Menu. Please select an action." \
                 " Enter any other number to go back to the main menu" \
                 "\n\t1. View All Customers' Numbers" \
                 "\n\t2. Add Customer Number" \
                 "\n\t3. Delete Customer Number" \
                 "\n\t4. Edit Customer Number"\
                 "\n\n\t<-- Back\n"
all_dest_format = "Here are all destinations in the format:" \
                  "\nID : Location"
rename_dest_prompt = "Please enter the ID of the destination you wish to change." \
                     " Or enter 0 to go back to the destination Menu\n"
current_rename = "This is the destination you are currently renaming:"
delete_dest_prompt = "Please enter the ID of the destination you wish to delete." \
                     " Or enter 0 to go back to the Driver Menu\n"


def validate_yesno_input():
    """
    Prompts for a binary yes/no input. If not 0 or 1, re-prompt for entry
    Returns:
         1 for yes, 0 for no

    """
    while True:
        try:
            request = int(input())
        except ValueError:
            print("*    Please only enter 1 for Yes or 0 for No.")
            continue
        else:
            while request not in (0, 1):
                print("*    Please only enter 1 for Yes or 0 for No.")
                request = int(input())
        return request


def validate_reconfirmation(entry_name):
    """
    Displays input and confirms entry with user. User presses 1 to confirm, or 0 to renter
    Args:
        entry_name:

    Returns:
        validated user input
    """
    while True:
        print(f"*   Please enter the {entry_name}:")
        entry = input()
        print(f"*   Is this the correct: {entry_name} -> {entry}")
        print("*    Please enter 1 for Yes, 0 for no")
        confirm = validate_yesno_input()
        if confirm == 1:
            return entry


def validate_standard_string():
    entries = input()
    entries = entries.rstrip()
    entries = entries.lstrip()
#  2: Edit Drivers
#  3: Delete Driver
# (should show list of destinations)
#  1: Add new Destinations
#  2: Edit destinations
#  3: Delete Destinations
#
#
#
# (should show list of numbers and failed attempts)
#  1: Add new customer number
#  2: Edit customer number
#  3: Delete customer number"
