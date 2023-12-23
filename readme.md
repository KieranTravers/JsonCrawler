# AntJournal 🐜📓

Welcome to AntJournal, a versatile tool for analyzing the structure of JSON files right from your command line!

## Features 🚀

- Load and analyze JSON files.
- Identify fields and types within JSON data.
- Validate consistency of data types for each field.
- User-friendly CLI interface with detailed error messages.

## Installation 🛠️

```bash
# Clone the repository to your local machine
git@github.com:KieranTravers/AntJournal.git

cd AntJournal

# Ensure you have Python installed, and then set up a virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install the required dependencies
pip3 install -r requirements.txt
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

## Written by✍️:
https://github.com/KieranTravers