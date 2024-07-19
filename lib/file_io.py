def write_file(file_name, file_content):
    file_name_with_extension = f"{file_name}.txt"
    with open(file_name_with_extension, mode="w") as file:
        file.write(file_content)

def append_file(file_name, file_content):
    file_name_with_extension = f"{file_name}.txt"
    with open(file_name_with_extension, mode="a") as file:
        file.write(file_content)

def read_file(file_name):
    file_name_with_extension = f"{file_name}.txt"
    with open(file_name_with_extension, mode="r") as file:
        content = file.read()
    return content
