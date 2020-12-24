import csv
from csv import writer


def get_header(db):
    """
    Gets the header row
    Args:
        db: A path to the needed .csv file

    Returns: a list containing the header of the file

    """
    with open(db) as f:
        reader = csv.reader(f)
        header_row = next(reader)
    return header_row


def get_all_items(db):
    """
    :param db: path to .csv file
    :return: list of items from the CSV file
    """
    with open(db) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        items = {}
        for row in reader:
            if len(row) <= 2:
                items[int(row[0])] = row[1]
            else:
                items[int(row[0])] = row[1:]
        return items


def generate_new_id(db):
    """
    Gets the id in a csv file
    :param db: database path for csv files
    :return: new id for csv files
    """
    with open(db) as f:
        reader = csv.reader(f)
        new_id = len(list(reader))
    return new_id


def insert_item(db, items):
    """
    Inserts an item  into .csv file
    Args:
        db: A path to the needed .csv file
        items: A list containing the items to be inserted

    """
    i_item = [generate_new_id(db)]
    if isinstance(items, str):
        i_item = [i_item[0], items]
    else:
        for item in items:
            i_item.append(item)
    with open(db, 'a+', newline='') as write_obj:
        csv_writer = writer(write_obj)
        csv_writer.writerow(i_item)


def get_item(db, item_id):
    """

    Args:
        db: A path to the needed .csv file
        item_id: The id of the item to be returned

    Returns: item string of a given ID

    """
    items = get_all_items(db)
    try:
        return items[item_id]
    except KeyError:
        pass


def delete_item(db, item_id):
    """
    Deletes a destination from the database
    Args:
        db: A path to the needed .csv file
        item_id: id of item to be deleted

    Returns:

    """
    items = get_all_items(db)
    del items[item_id]
    rewrite_db(db, items)


def edit_item(db, item_id, edited_item):
    """
    Edits an item in the database
    Args:
        db: A path to the needed .csv file
        item_id: The id of the item to be edited
        edited_item: The new item to be added

    Returns:

    """
    items = get_all_items(db)
    items[item_id] = edited_item
    rewrite_db(db, items)


def rewrite_db(db, items):
    """
    Rewrites the database given a dictionary. Note that this must be used to update or delete .csv files
    Args:
        db: A path to the needed .csv file
        items: A dictionary of the items that will serve as the source to rewrite the .csv

    Returns:

    """
    header = get_header(db)
    with open(db, 'w+', newline='') as write_obj:
        csv_write = writer(write_obj)
        csv_write.writerow(header)
        for item_row in items.items():
            csv_write.writerow(item_row)
