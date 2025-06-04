try:
    from hashid import HashID
    from hashlib import md5,sha1,sha224,sha256,sha384,sha512
    from concurrent.futures import ThreadPoolExecutor

except ImportError as Ie:
    print(f"[ + ] Couldn't import '{Ie}'")

class HashCracker:
    def __init__(self,thread_count = 40, debug = False):
        self.debug = debug
        self.threads = thread_count

    def identify_hash_type(self, input_hash):
        hid = HashID()
        hash_length = len(input_hash)
        matches = list(hid.identifyHash(input_hash))

        if self.debug:
            print(f"[>] Checking hash: {input_hash}")

        if hash_length == 32 and any("md5" in match.name.lower() for match in matches):
            if self.debug:
                print(f"[+] Hash identified : MD5")

            return "MD5"

        elif hash_length == 40 and any("sha1" in match.name.lower() for match in matches):
            if self.debug:
                print(f"[+] Hash identified : SHA-1")

            return "SHA-1"

        elif hash_length == 56 and any("sha224" in match.name.lower() for match in matches):
            if self.debug:
                print(f"[+] Hash identified : SHA-224")

            return "SHA-224"

        elif hash_length == 64 and any("sha256" in match.name.lower() for match in matches):
            if self.debug:
                print(f"[+] Hash identified : SHA256")

            return "SHA-256"

        elif hash_length == 96 and any("sha384" in match.name.lower() for match in matches):
            if self.debug:
                print(f"[+] Hash identified : SHA384")

            return "SHA-384"

        elif hash_length == 128 and any("sha512" in match.name.lower() for match in matches):
            if self.debug:
                print(f"[+] Hash identified : SHA512")

            return "SHA-512"

        else:
            if self.debug:
                print(f"[+] Hash can't identified")

            return None

    def crack_hash(self,input_hash,password):

        hashed = md5(password.encode()).hexdigest()
        if hashed == input_hash:
            print(f"[+] Password Cracked: {password}")
            return password
        return None


    def hash_cracker(self, hash_type, input_hash, passwords):
        if hash_type.lower() == "md5":
            if self.debug:
                print("[>] Cracking MD5 hash...")

            with ThreadPoolExecutor(max_workers=self.threads) as executor:
                Results = executor.map(
                    lambda password: self.crack_hash(input_hash,password),
                    passwords
                )
                for result in Results:
                    if result:
                        return result
        else:
            print("[!] Unsupported hash type.")


    def main(self , input_hash):
        if self.debug:
            print("[>] identifying hash")

        hash_type = self.identify_hash_type(input_hash)

        if self.debug:
            print("[>] Cracking hash")

        passwords = ["test1","test2","test3","test4","test5","test6","test7","test","test2","test1","test3","test4","test5","test6","test7",]

        password = self.hash_cracker(hash_type,input_hash,passwords)

        if not password:
            print(f"[X] Password Couldn't be cracked ")

if __name__ == "__main__":
    hashes = {
            "MD5": "098f6bcd4621d373cade4e832627b4f6",
            "SHA-1": "a94a8fe5ccb19ba61c4c0873d391e987982fbbd3",
            "SHA-224": "90a4224ec6cf2de7901261d5977b1cbe4c1b9b7412be3ec3bf",
            "SHA-256": "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08",
            "SHA-384": "768412320f7b0aa5812fce428dc1a828fded6c3c09fcd4f1dfd1fabcbfbd353c7dd761c74fbf95fdbae903d5",
            "SHA-512": "ee26b0dd4af7e749aa1a8ee3c10ae9923f618980772e473f8819a5d4940e0db2"
                       "7ac185f8a0e1d5f84f88bc887fd67b143732c304cc5fa9ad8e6f57f50028a8ff"
        }
    cracker = HashCracker(debug=True)
    cracker.main(hashes["MD5"])
