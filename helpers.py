import json

def export_to_json(data, filename="airtime_payments.json"):
    """
    Exports a list of dictionaries to a JSON file.

    Args:
        data: A list of dictionaries to be exported.
        filename: The name of the JSON file to create (default: "airtime_payments.json").
    """

    with open(filename, "w") as f:  # "w" for write mode
        json.dump(data, f, indent=4)  # indent for pretty formatting
    print(f"Data exported to {filename}")