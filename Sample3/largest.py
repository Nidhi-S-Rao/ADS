import sys
import os

def find_largest_file(directory_path="."):
    largest_file = None
    largest_size = 0

    try:
        with os.scandir(directory_path) as entries:
            for entry in entries:
                if entry.is_file():
                    file_size = entry.stat().st_size
                    if file_size > largest_size:
                        largest_size = file_size
                        largest_file = entry.path
                        

        if largest_file:
            print("Largest file:",largest_file)
        else:
            print("No files found in the directory.")

    except FileNotFoundError:
        print(f"Error: Directory '{directory_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if len(sys.argv) == 1:
    find_largest_file()
elif len(sys.argv) == 2:
    directory_path = sys.argv[1]
    find_largest_file(directory_path)
else:
    print("Error")


