import json
import string


def strip_casefold(data):
    """Returns data stripped and lower case."""
    return data.strip().casefold()


def check_string_is_empty(data):
    """Checks if data consists of only whitespace characters."""
    if data.translate({ord(c): None for c in string.whitespace}) == "":
        return True


def write_to_json_file(file_name, data, path_to_folder):
    try:
        with open(f"{path_to_folder}/{file_name}.json", "x") as file:
            json.dump(data, file)
            print(f"{file_name}.json added to recipes.")
    except:
        print("File already exists")
