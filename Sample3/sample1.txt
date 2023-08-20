import sys

if len(sys.argv) != 2:
    print("File name not entered")
else:
    filename=sys.argv[1]
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            print(contents)
            file.close()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")