try:
    import sys
    import argparse
    from colorama import Fore,Style

except ImportError as Ie:
    print(f"[ + ] Couldn't import '{Ie}'")

class CommandLine:
    """
        Class to handle commandline.

        Args:
            None
        
        Results:
            None
    """
    def __init__(self) -> None:
        self.blue = Fore.BLUE
        self.red=Fore.RED
        self.blue=Fore.BLUE
        self.white=Fore.WHITE
        self.magenta=Fore.MAGENTA
        self.bright=Style.BRIGHT
        self.green=Fore.GREEN
        self.red=Fore.RED
        self.bold=Style.BRIGHT
        self.reset=Style.RESET_ALL

    def get_banner(self) ->str:
        """
            Function that return banner for the HashBrute.

            Args:
                None
            
            Returns:
                Banner (str) : Banner for the HashBrute.
                
        """
        banner = """
         _______ _________         __         ______              __         
        |   |   |   ___   |.-----.|  |--.    |   __ \\.----.--.--.|  |_.-----.
        |       |  |  _   ||__ --||     |    |   __ <|   _|  |  ||   _|  -__|
        |___|___|  |______||_____||__|__|    |______/|__| |_____||____|_____|
                |_________|                                                  

                Tool to bruteforce the hashes with known password.
                          Github : pevinkumar10
        """

        return banner

    def get_arguments(self) -> list:
        """
            Function to parse arguments

            Args:
                None
            
            Returns:
                Arguments for the HashBrute.

        """
        parser=argparse.ArgumentParser(add_help=False,usage=argparse.SUPPRESS,exit_on_error=False)
        try:
            parser.add_argument("--hash",type=str)
            parser.add_argument("-w","--wordlist")
            parser.add_argument("-t","--threads",type=int)
            parser.add_argument("-d","--debug",action="store_true")
            parser.add_argument("-h","--help",action="store_true")

            arguments=parser.parse_args()

            return arguments
        
        except argparse.ArgumentError:
            print(f"{self.bright}{self.red}[ ! ] {self.reset}{self.blue}Value needed for the argument Please use -h to get more information.")
            exit()
            
        except argparse.ArgumentTypeError:
            print(f"{self.bright}{self.blue}\n [ ! ] {self.reset}{self.blue}Please use -h to get more information.")
            exit()
        
        except Exception as e:
            print(f"{self.bright}{self.red}\n [ ! ] {self.reset}{self.blue}Unexpected Argument Error:{e}")
            exit()
    
    def get_help(self) ->str:
        """
            Function that return Help menu for the HashBrute.

            Args:
                None
            
            Returns:
                Help menu (str) : Help menu for the HashBrute.
                
        """
        return f"""
        {self.bold}{self.white}[{self.reset}{self.bold}{self.blue}DESCRIPTION{self.reset}{self.white}]{self.reset}: {self.white}{self.bold}hash-brute{self.reset} {self.white}is used to crack hashes {self.reset}{self.bold}{self.green}pevinkumar10{self.reset}.\n
            {self.bold}{self.white}[{self.reset}{self.bold}{self.blue}Usage{self.reset}{self.white}]{self.reset}:{sys.argv[0]} [ options ]\n
                    {self.white}hash-brute {self.bold}{self.white}<{self.reset}{self.bold}{self.blue}Flags{self.reset}{self.bold}{self.white}>\n
            [{self.reset}{self.bold}{self.blue}Flags{self.reset}{self.bold}{self.white}]
                    [{self.reset}{self.bold}{self.blue}Input{self.reset}{self.bold}{self.white}]{self.reset}
                              --hash                    :  Input hash to do bruteforce                                                  [Mandatory]
                        -w,   --wordlist                :  List of passwords one per line (default wordlist/default-wordlist.txt)       [Mandatory]   

                    [{self.reset}{self.bold}{self.blue}Options{self.reset}{self.bold}{self.white}]{self.reset}
                        -t,   --threads                 :  Number of threads (default : 40)               

                    {self.bold}{self.white}[{self.reset}{self.bold}{self.blue}Debug{self.reset}{self.bold}{self.white}]{self.reset}
                        -d,   --debug                   :  To set debug flag.
                        -h,   --help                    :  To see all the available options.

                        """