import sys
import os

def find_most_recent_file(directory_path="."):
    most_recent_file = None
    most_recent_time = 0

    try:
        with os.scandir(directory_path) as entries:
            for entry in entries:
                if entry.is_file():
                    modification_time = entry.stat().st_mtime
                    if modification_time > most_recent_time:
                        most_recent_time = modification_time
                        most_recent_file = entry.path

        if most_recent_file:
            print("Most recently modified file:",most_recent_file)
        else:
            print("No files found in the directory.")

    except FileNotFoundError:
        print(f"Error: Directory '{directory_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if len(sys.argv) == 1:
    find_most_recent_file()
elif len(sys.argv) == 2:
    directory_path = sys.argv[1]
    find_most_recent_file(directory_path)
else:
    print("Error")

