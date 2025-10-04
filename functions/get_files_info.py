import os 

def get_files_info(working_directory, directory="."):
    full_path_working_directory= os.path.abspath(working_directory)
    full_path_directory = os.path.abspath(os.path.join(full_path_working_directory, directory))
    
    
    if not full_path_directory.startswith(full_path_working_directory):
        print(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')


    if not os.path.isdir(full_path_directory):
        print(f'Error: "{directory}" is not a directory')
    
    result = []
    # if os.path.isfile(directory)
    for filename in os.listdir(full_path_directory):
        try:
            p = os.path.join(full_path_directory, filename)
            file_size = os.path.getsize(p)
            is_dir = os.path.isdir(p)
            result.append(f'- {filename}: file_size={file_size} bytes, is_dir={is_dir}')
        except Exception as e:
            result.append(f'- {filename}: Error: {str(e)}')
    print("\n".join(result))
