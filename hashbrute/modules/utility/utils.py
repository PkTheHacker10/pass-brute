class Utils:
    def __init__(self):
        pass

    def get_file_contents(self,file):
        try:
            with open(file) as opened_file:
                content = opened_file.readlines()
                if content:
                    return content
                else:
                    None
        except (FileNotFoundError,PermissionError):
            print(f"[ + ] Couldn't open the file or the didn't exist")