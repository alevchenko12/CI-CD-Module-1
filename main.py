def read_file(file_name):
    with open(file_name, 'r') as file:
        return set(file.read().splitlines())