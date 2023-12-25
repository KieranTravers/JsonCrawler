# AntJournal 🐜📓

Welcome to AntJournal, a versatile tool for analyzing the structure of JSON files right from your command line!

## Features 🚀

- Load and analyze JSON files.
- Identify fields and types within JSON data.
- Validate consistency of data types for each field.
- User-friendly CLI interface with detailed error messages.

## Installation 🛠️

Make sure you have Python 3+ installed on your system. You can download it from the [Python official website](https://www.python.org/).

Then, clone the repository:

```bash
# Clone the repository to your local machine
git clone git@github.com:KieranTravers/AntJournal.git

cd AntJournal
```
Usage 📖
To use AntJournal, simply run the script followed by the path to the JSON file you wish to analyze:

```bash
python3 AntJournal.py /path/to/yourfile.json
```

Example:

```bash
# Analyze a file named `test1.json`
python3 AntJournal.py test1.json
```

Output:

```bash
Using file: test1.json
No errors found. Field types:
 - id: int
 - name: str
 - value: float
```

Understanding Errors and Outputs
When analyzing JSON files, AntJournal meticulously scans for and reports any irregularities or issues. Here are some common errors you might encounter:

'field' is null: Indicates a null value for 'field'. Nulls might be intentional or represent missing data, but they can also disrupt data uniformity and processing.

Inconsistent types for 'field': Highlights when values under the same field across different objects have varying data types. Uniform data types are crucial for consistent data processing and analysis.

Sample Error Output:
If you run AntJournal with a JSON file that has inconsistencies or issues, you might see output like this:

```bash
Errors found in JSON file:
 - Item 2: 'website' is null
 - Item 3: 'contact_number' is null
 - Inconsistent types for 'name': {'str', 'int'}
 - Inconsistent types for 'id': {'str', 'int'}
 - Inconsistent types for 'website': {'str', 'NoneType'}
 - Inconsistent types for 'contact_number': {'str', 'NoneType'}
```

This detailed reporting helps you understand exactly what needs attention, allowing for precise corrections and consistency in your JSON data.

## Written by✍️:
https://github.com/KieranTravers