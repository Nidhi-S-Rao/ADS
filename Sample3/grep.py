import sys
import re

if len(sys.argv) != 3:
    print("File name and pattern not entered")
else:
    filename=sys.argv[1]
    pattern=sys.argv[2]
    try:
        with open(filename, 'r') as file:
            for line in file:
                if re.search(pattern, line):
                    print(line, end='')
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")