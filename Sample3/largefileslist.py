import sys
import os

def parse_size(size_str):
    suffixes = {'K': 1e3, 'M': 1e6, 'G': 1e9}

    if size_str[-1] in suffixes:
        return int(float(size_str[:-1]) * suffixes[size_str[-1]])
    else:
        return int(size_str)

def find_large_files(directory_path, min_size):
    try:
        min_size_bytes = parse_size(min_size)

        for root, _, filenames in os.walk(directory_path):
            for filename in filenames:
                filepath = os.path.join(root, filename)
                file_size = os.path.getsize(filepath)
                if file_size > min_size_bytes:
                    print(f"Size: {file_size} bytes, File: {filepath}")

    except FileNotFoundError:
        print(f"Error: Directory '{directory_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if len(sys.argv) != 3:
    print("Error")
else:
    directory_path = sys.argv[1]
    min_size = sys.argv[2]
    find_large_files(directory_path, min_size)


