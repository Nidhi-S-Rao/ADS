import sys

if len(sys.argv) != 2:
    print("File name not entered")
else:
    filename=sys.argv[1]
    try:
        with open(filename, 'r') as file:
            for i in range(5):
                line = file.readline()
                if not line:
                    break
                print(line, end='')
            file.close()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")