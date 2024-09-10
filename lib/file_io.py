

# Function to write content to a .txt file
def write_file(file_name, file_content):
    file_name = str(file_name)  # Convert to string to handle pathlib.Path
    # Ensure the file name ends with '.txt'
    if not file_name.endswith('.txt'):
        file_name += '.txt'

    # Write the content to the file (overwrite if exists)
    with open(file_name, 'w') as file:
        file.write(file_content)


# Function to append content to an existing .txt file
def append_file(file_name, append_content):
    # Convert file_name to a string to handle PosixPath or Path objects
    file_name = str(file_name)
    
    # Ensure the file name ends with '.txt'
    if not file_name.endswith('.txt'):
        file_name += '.txt'

    # Open the file in append mode and add the new content
    with open(file_name, 'a') as file:
        file.write(append_content)


# Function to read content from a .txt file and return it
def read_file(file_name):
    file_name = str(file_name)  # Convert to string to handle pathlib.Path
    # Ensure the file name ends with '.txt'
    if not file_name.endswith('.txt'):
        file_name += '.txt'

    # Read the content of the file and return it
    with open(file_name, 'r') as file:
        return file.read()
