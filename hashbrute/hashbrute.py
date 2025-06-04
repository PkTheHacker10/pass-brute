try:
    from hashbrute.modules.core import CrackerCore

except ImportError as Ie:
    print(f"[ + ] Couldn't import '{Ie}'")

def main() -> None:
    """
        Main function for the HashBrute.
        Args:
            None

        Returns:
            None
    """
    cracker = CrackerCore()
    cracker.handler()

if __name__ == "__main__":
    main()