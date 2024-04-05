def read_file(file_name):
    with open(file_name, 'r') as file:
        return set(file.read().splitlines())
    
def write_to_file(file_name, lines):
    with open(file_name, 'w') as file:
        file.write('\n'.join(lines))