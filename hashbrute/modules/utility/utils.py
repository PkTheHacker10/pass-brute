class Utils:
    """
        Class for support functions.
    """
    def get_file_contents(self,file:str) -> list:
        """
            Functions to get the file contents.
            Args:
                file    (str): File path to read the content
            
            Returns:
                content (list): Returns the list of the contents if it has content ,else None.
        """
        try:
            with open(file) as opened_file:
                content = opened_file.readlines()
                if content:
                    return content
                else:
                    None
        except (FileNotFoundError,PermissionError):
            print(f"[ + ] Couldn't open the file or the didn't exist")