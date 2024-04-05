def read_file(file_name):
    with open(file_name, 'r') as file:
        return set(file.read().splitlines())
    
def write_to_file(file_name, lines):
    with open(file_name, 'w') as file:
        file.write('\n'.join(lines))
        
def compare_cycle(text1, text2):
    same_text = []
    diff_text = []
    for line1 in text1:
        found = False
        for line2 in text2:
            if line1 == line2:
                same_text.append(line1)
                found = True
                break
        if not found:
            diff_text.append(line1)
            
    for line2 in text2:
        found = False
        for line1 in text1:
            if line2 == line1:
                found = True
                break
        if not found:
            diff_text.append(line2)
            
    return same_text, diff_text

def compare_files(file1, file2):
    text1 = read_file(file1)
    text2 = read_file(file2)
    
    same_text, diff_text = compare_cycle(text1, text2) 
    
    write_to_file('same.txt', same_text)
    write_to_file('diff.txt', diff_text)
    
if __name__ == "__main__":
    file1 = "file1.txt"
    file2 = "file2.txt"
    compare_files(file1, file2)