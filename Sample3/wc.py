import sys

if len(sys.argv) != 2:
    print("File name not entered")
else:
    filename=sys.argv[1]
    try:
        with open(filename, 'r') as file:
            lines = 0
            words = 0
            characters = 0

            for line in file:
                lines += 1
                words += len(line.split())
                characters += len(line)
            print("Lines:",lines, " Words:",words," Characters:",characters)
            file.close()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")