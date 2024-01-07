import json
import argparse
from collections import defaultdict
import sys

def print_title():
    title = """
      _                  _____                    _           
     | |                / ____|                  | |          
     | |___  ___  _ __ | |     _ __ __ ___      _| | ___ _ __ 
 _   | / __|/ _ \| '_ \| |    | '__/ _` \ \ /\ / / |/ _ \ '__|
| |__| \__ \ (_) | | | | |____| | | (_| |\ V  V /| |  __/ |   
 \____/|___/\___/|_| |_|\_____|_|  \__,_| \_/\_/ |_|\___|_|
 
"""
    print(title)

def load_json(file_path):
    """ Load the JSON file """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError as e:
        print(f"Invalid JSON: {e.msg} at line {e.lineno} column {e.colno}")
        sys.exit(1)

def recursive_analyze(data, path="root"):
    """ Recursively analyze the structure of the JSON data and identify fields and types """
    if isinstance(data, dict):
        for key, value in data.items():
            new_path = f"{path}.{key}" if path else key
            yield from recursive_analyze(value, new_path)
    elif isinstance(data, list):
        for i, item in enumerate(data):
            new_path = f"{path}[{i}]"
            yield from recursive_analyze(item, new_path)
    else:
        yield (path, type(data).__name__)

def analyze_structure(data, deep_scan=False):
    """ Analyze the structure of the JSON data and identify fields and types """
    field_types = defaultdict(set)
    if deep_scan:
        for path, type_name in recursive_analyze(data):
            field_types[path].add(type_name)
    else:
        if isinstance(data, list):
            for i, item in enumerate(data):
                if isinstance(item, dict):
                    for key, value in item.items():
                        field_types[key].add(type(value).__name__)
        elif isinstance(data, dict):
            for key, value in data.items():
                field_types[key].add(type(value).__name__)

    return field_types

def display_results(field_types):
    """ Display the results of the analysis """
    for field, types in field_types.items():
        print(f" - {field}: {', '.join(types)}")

def main(file_path, deep_scan):
    print_title()
    data = load_json(file_path)

    field_types = analyze_structure(data, deep_scan)

    inconsistent_fields = {key: types for key, types in field_types.items() if len(types) > 1}
    consistent_fields = {key: types for key, types in field_types.items() if len(types) == 1}

    # Report inconsistencies first
    if inconsistent_fields:
        print("\nInconsistencies found in JSON file:")
        display_results(inconsistent_fields)

    # Then, report other field types
    print("\nField types in JSON file:")
    display_results(field_types)
    if deep_scan or not inconsistent_fields:  # Display all in case of deep scan or no inconsistencies
        display_results(field_types)
    else:  # Display only consistent fields when not deep scanning and there are inconsistencies
        display_results(consistent_fields)

    # Note about no inconsistencies if applicable
    if not inconsistent_fields:
        print("\nNo inconsistencies or issues found.")

    print("\n")  
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Analyze the structure of a JSON file.")
    parser.add_argument('file_path', type=str, help='Path to the JSON file to analyze')
    parser.add_argument('--deep', action='store_true', help='Perform a deep scan of all nested data')
    
    args = parser.parse_args()
    
    main(args.file_path, args.deep)
