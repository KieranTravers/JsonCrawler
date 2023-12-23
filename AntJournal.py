import json
import argparse
from collections import defaultdict

def load_json(file_path):
    """ Load the JSON file """
    with open(file_path, 'r') as file:
        return json.load(file)

def analyze_structure(data):
    """ Analyze the structure of the JSON data and identify fields and types """
    field_types = defaultdict(set)
    errors = []

    for i, item in enumerate(data):
        if not isinstance(item, dict):
            errors.append(f"Item {i+1} is not a JSON object")
            continue

        for key, value in item.items():
            field_types[key].add(type(value).__name__)  # Change to type name for better readability
            if value is None:
                errors.append(f"Item {i+1}: '{key}' is null")

    return field_types, errors

def validate_consistency(field_types):
    """ Validate the consistency of data types for each field """
    consistency_errors = []
    for key, types in field_types.items():
        if len(types) > 1:
            consistency_errors.append(f"Inconsistent types for '{key}': {types}")
    return consistency_errors

def main(file_path):
    data = load_json(file_path)
    if not isinstance(data, list):
        print("JSON root is not a list. Cannot process.")
        return

    field_types, null_errors = analyze_structure(data)
    consistency_errors = validate_consistency(field_types)

    if null_errors or consistency_errors:
        print("Errors found in JSON file:")
        for error in null_errors + consistency_errors:
            print(f" - {error}")
    else:
        print("No errors found. Field types:")
        for field, types in field_types.items():
            print(f" - {field}: {', '.join(types)}")  

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Analyze the structure of a JSON file.")
    parser.add_argument('file_path', type=str, help='Path to the JSON file to analyze')
    
    args = parser.parse_args()
    
    main(args.file_path)
