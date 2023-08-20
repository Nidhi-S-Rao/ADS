import sys

if len(sys.argv) != 3:
        print("File name not entered")
        
else:
    source_filename = sys.argv[1]
    destination_filename = sys.argv[2]


    try:
            with open(source_filename, 'r') as source_file:
                source_contents = source_file.read()

                with open(destination_filename, 'w') as destination_file:
                    destination_file.write(source_contents)

            print(f"File '{source_filename}' copied to '{destination_filename}'")
    except FileNotFoundError:
            print(f"Error: File '{source_filename}' not found.")
    except Exception as e:
            print(f"An error occurred: {e}")


    
    