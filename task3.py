def merge_files(file_list, output_file):    
    files_data = []
    for filename in file_list:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            files_data.append((filename, len(lines), lines))    
    
    files_data.sort(key=lambda x: x[1])    
    
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for filename, line_count, lines in files_data:
            outfile.write(f"{filename}\n{line_count}\n")
            outfile.writelines(lines)
            outfile.write("\n")


file_list = ['1.txt', '2.txt', '3.txt']
output_file = 'output_file.txt'

merge_files(file_list, output_file)


