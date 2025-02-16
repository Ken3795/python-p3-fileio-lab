import os

def write_file(file_name, file_content):
    """Write content to a file, creating it if necessary."""
    # Add .txt extension to the file name
    file_name_with_extension = f"{file_name}.txt"
    
    # Open the file for writing (creates the file if it doesn't exist)
    with open(file_name_with_extension, 'w') as f:
        f.write(file_content)

def append_file(file_name, append_content):
    """Append content to an existing file."""
    # Add .txt extension to the file name
    file_name_with_extension = f"{file_name}.txt"
    
    # Open the file for appending (creates the file if it doesn't exist)
    with open(file_name_with_extension, 'a') as f:
        f.write(append_content)

def read_file(file_name):
    """Read content from a file."""
    # Add .txt extension to the file name
    file_name_with_extension = f"{file_name}.txt"
    
    # Open the file for reading and return the content
    with open(file_name_with_extension, 'r') as f:
        return f.read()
