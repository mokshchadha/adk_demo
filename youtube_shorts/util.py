def load_instruction_from_file(fileName):
    try:
        with open(fileName, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"Error: The file '{fileName}' was not found.")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None
    