import sys
import os

def list_files_only(directory_path="."):
    try:
        with os.scandir(directory_path) as entries:
            for entry in entries:
                if entry.is_file():
                    print(entry.name)
    except FileNotFoundError:
        print(f"Error: Directory '{directory_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if len(sys.argv) == 1:
    list_files_only()
elif len(sys.argv) == 2:
    directory_path = sys.argv[1]
    list_files_only(directory_path)
else:
    print("Error")

