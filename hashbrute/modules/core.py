try:
    import sys
    from colorama import Fore,Style
    from hashbrute.modules.cli.cli import  CommandLine
    from hashbrute.modules.utility.utils import Utils
    from hashbrute.modules.cracker.cracker  import HashCracker

except ImportError as Ie:
    print(f"[ + ] Couldn't import '{Ie}'")

class CrackerCore:
    def __init__(self ,threads = 40, debug = False):

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

        self.debug = debug

        self.wordlist = "hashbrute/wordlist/default-wordlist.txt"

        self.utility = Utils()
        self.commandline = CommandLine()
        self.cracker = HashCracker(debug = debug ,thread_count = threads)


    def handler(self):
        print(self.commandline.get_banner())
        arguments = self.commandline.get_arguments()

        if arguments.help:
            print(self.commandline.get_help())
            exit()

        if arguments.hash or arguments.file:
            if arguments.hash and arguments.file:
                print(f" Two entries are not allowed:\n{self.bright}{self.blue} Usage :{sys.argv[0]} {self.reset}--hash / --file {self.red}<hash / file>{self.reset} {self.red}[options]{self.reset} \n {self.blue}Use --help for more information.{self.reset}\n")
                exit(1)

            if arguments.hash:
                input_hash = arguments.hash
                passwords = self.utility.get_file_contents(arguments.wordlist) if arguments.wordlist else self.utility.get_file_contents(self.wordlist)

                print(f"[ + ] Total passwords in wordlist: {len(passwords)}")
                
                password = self.cracker.main(input_hash, passwords)
                if password:
                    print(f"[ ✓ ] Found '{password}'")
                else:
                    print("[ ✓ ] Password couldn't found")


            if arguments.file:
                hash_file = arguments.file
                print(f"[!] File cracking not implemented yet: {hash_file}")
                exit()
        else:
            print(f" Missing required arguments:\n{self.bright}{self.blue} Usage :{sys.argv[0]} {self.reset}--hash / --file {self.red}<hash / file>{self.reset} {self.red}[options]{self.reset} \n {self.blue}Use --help for more information.{self.reset}\n")
            exit(1)         

if __name__ == "__main__":
    cracker = CrackerCore()
    cracker.handler()