import os 

def get_files_info(working_directory, directory="."):
    new_wd= os.path.abspath(working_directory)
    full_path = os.path.abspath(new_wd, directory)
    if not full_path.startswith(os.path.abspath(new_wd)):
        raise ValueError("aaaa")
    
    if not os.path.abspath(directory).startswith(os.getcwd()):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(full_path):
        return f'Error: "{directory}" is not a directory'
    
    result = []
    for a in os.listdir(new_wd):
        try:
            p = os.path.join(new_wd, a)
            file_size = os.path.getsize(p)
            print(file_size)
            is_dir = os.path.isdir(p)
            print(is_dir)
            result.append(f'- {a}: file_size={file_size} bytes, is_dir={is_dir}')
        except Exception as e:
            result.append(f'- {a}: Error: {str(e)}')
    return "\n".join(result)

