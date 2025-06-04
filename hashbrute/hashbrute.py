try:
    from hashbrute.modules.core import CrackerCore

except ImportError as Ie:
    print(f"[ + ] Couldn't import '{Ie}'")

def main():
    cracker = CrackerCore()
    cracker.handler()