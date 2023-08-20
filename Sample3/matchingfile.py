import sys
import os
import glob

def find_matching_files(directory_path, pattern):
    try:
        for root, _, filenames in os.walk(directory_path):
            for filename in filenames:
                if glob.fnmatch.fnmatch(filename, pattern):
                    print(os.path.join(root, filename))
    except FileNotFoundError:
        print(f"Error: Directory '{directory_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if len(sys.argv) != 3:
    print("Error")
        
else:
    directory_path = sys.argv[1]
    pattern = sys.argv[2]
    find_matching_files(directory_path, pattern)
