import os

def load_instruction_from_file(fileName):
    try:
        # Get the directory of the current script file
        current_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Construct the full path to the target file in the current directory
        file_path = os.path.join(current_dir, fileName)
        
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"Error: The file '{fileName}' was not found.")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None