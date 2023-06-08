def get_file_types(extension_type_list, file_list):
    file_types = {}
    extension_type_pairs = extension_type_list.split(';')
    for file in file_list:
        if '.' in file:
            filename, extension = file.split('.')
            file_type = 'unknown'
            for pair in extension_type_pairs:
                ext, typ = pair.split(',')
                if ext.lower() == extension.lower():
                    file_type = typ
                    break
            file_types[file] = file_type
        else:
            file_types[file] = 'unknown'
    return file_types

# Test the function
extension_type_list = "xls,spreadsheet;xlsx,spreadsheet;jpg,image"
file_list = ["abc.jpg", "xyz.xls", "text.csv", "123"]
file_types = get_file_types(extension_type_list, file_list)

# Format the output as multiline strings
output = ",\n".join(f'"{filename}": "{file_type}"' for filename, file_type in file_types.items())
output = "{\n" + output + "\n}"

print(output)
# 