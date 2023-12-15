def read_file(file_name:str):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return f"El archivo '{file_name}' no se encontró."
    except Exception as e:
        return f"Se produjo un error: {str(e)}"