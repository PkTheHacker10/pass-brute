try:
    import sys
    from colorama import Fore,Style
    from hashbrute.modules.cli.cli import  CommandLine
    from hashbrute.modules.utility.utils import Utils
    from hashbrute.modules.cracker.cracker  import HashCracker

except ImportError as Ie:
    print(f"[ + ] Couldn't import '{Ie}'")

class CrackerCore:
    """
        Class to handle the hash cracker.

        Args:
            None

        Returns:
            None
    """
    def __init__(self):
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

        self.debug = False
        self.default_threads = 40

        self.wordlist = "hashbrute/wordlist/default-wordlist.txt"

    def handler(self) -> None:
        # Intializing the classes.
        commandline = CommandLine()
        utilis = Utils()

        # printing banner.
        print(commandline.get_banner())

        # Parsing arguments 
        arguments = commandline.get_arguments()

        # Checking for the help flag.
        if arguments.help:
            print(commandline.get_help())
            exit()

        # Checking for the debug flag.
        if arguments.debug:
            print("[ ✓ ] Debug mode activated")
            self.debug = True

        # Checking for the threads flag to adjust default thread count.
        if arguments.threads:
            self.default_threads = arguments.threads
            if arguments.debug:
                print(f"[ ✓ ] Threads increased to {self.default_threads}")

        # Checking for the wordlist flag to adjust default wordlist.
        if arguments.wordlist:
            if arguments.debug:
                print(f"[ ✓ ] Wordlist changed to '{arguments.wordlist}'")

        # Actual logics starts here.
        if arguments.hash:
            input_hash = arguments.hash
            passwords = utilis.get_file_contents(arguments.wordlist) if arguments.wordlist else utilis.get_file_contents(self.wordlist)

            print(f"[ + ] Total passwords in wordlist: {len(passwords)}")

            cracker = HashCracker(debug = self.debug ,thread_count = self.default_threads)

            password = cracker.main(input_hash, passwords)

            if password:
                print(f"[ ✓ ] '{input_hash}' is Cracked => '{password}'")
            else:
                print("[ ✓ ] Password couldn't found")

        else:
            print(f" Missing required arguments:\n{self.bright}{self.blue} Usage :{sys.argv[0]} {self.reset}--hash / --file {self.red}<hash / file>{self.reset} {self.red}[options]{self.reset} \n {self.blue}Use --help for more information.{self.reset}\n")
            exit(1)         

if __name__ == "__main__":
    cracker = CrackerCore()
    cracker.handler()