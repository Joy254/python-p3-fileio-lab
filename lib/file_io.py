import os

def write_file(file_name, file_content):
    pass
    file_path = f"{file_name}.txt"
    with open(file_path, 'w') as file:
        file.write(file_content)


def append_file(file_name, append_content):
    pass
    file_path = f"{file_name}.txt"
    with open(file_path, 'a') as file:
        file.write('\n' + append_content)

def read_file(file_name):
    pass
    file_path = f"{file_name}.txt"
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            content = file.read()
            return content
    else:
        return f"File '{file_name}.txt' not found."

