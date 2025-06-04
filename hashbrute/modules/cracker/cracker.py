try:
    from tqdm import tqdm
    from hashid import HashID
    from hashlib import md5,sha1,sha256,sha512
    from concurrent.futures import ThreadPoolExecutor
    from concurrent.futures import as_completed

except ImportError as Ie:
    print(f"[ ! ] Couldn't import '{Ie}'")

class HashCracker:
    """
        Class to handle the hash cracking.

        Args:
            thread_count    (int): Number of threads to spawn.
            debug           (bool): To set debug flag.
        Returns:
            password        (str): returns password if found , else returns None.
    """
    def __init__(self,thread_count = 40, debug = False):
        self.debug = debug
        self.threads = thread_count

    def identify_hash_type(self, input_hash:str) -> str:
        """
            Function to indentify the the hash type.

            Args:
                input_hash  (str): hash value to check.

            Returns:
                hash_type   (str): returns the hash type.
        """
        hid = HashID()
        hash_length = len(input_hash)
        matches = list(hid.identifyHash(input_hash))

        if hash_length == 32 and any("md5" in match.name.lower() for match in matches):
            if self.debug:
                print(f"[ ✓ ] Hash identified : MD5")

            return "MD5"

        elif hash_length == 40 and any("sha1" in match.name.lower() for match in matches):
            if self.debug:
                print(f"[ ✓ ] Hash identified : SHA-1")

            return "SHA-1"

        elif hash_length == 64 and any("sha256" in match.name.lower() for match in matches):
            if self.debug:
                print(f"[ ✓ ] Hash identified : SHA-256")

            return "SHA-256"

        elif hash_length == 128 and any("sha512" in match.name.lower() for match in matches):
            if self.debug:
                print(f"[ ✓ ] Hash identified : SHA-512")

            return "SHA-512"

        else:
            if self.debug:
                print(f"[ ! ] Hash can't identified")
            return None

    def crack_hash(self,input_hash:str,hash_type:str,password:str) ->str:
        """
            Function to crack the the hash.

            Args:
                input_hash  (str): Hash value to crack.
                hash_type   (str): Type of the hash to crack.
                password    (str): password to check with hash.

            Returns:
                password   (str): returns the password if found ,else return None.
        """
        if hash_type.lower() == "md5":

            hashed = md5(password.encode()).hexdigest()
            if hashed == input_hash:
                return password
            return None
        
        elif hash_type.lower() == "sha-1":
            hashed = sha1(password.encode()).hexdigest()

            if hashed == input_hash:
                if self.debug:
                    print(f"[ ✓ ] Password Cracked: {password}")
                return password
            
            return None
        
        elif hash_type.lower() == "sha-256":
            hashed = sha256(password.encode()).hexdigest()

            if hashed == input_hash:
                if self.debug:
                    print(f"[ ✓ ] Password Cracked: {password}")
                return password
            
            return None
        
        elif hash_type.lower() == "sha-512":
            hashed = sha512(password.encode()).hexdigest()

            if hashed == input_hash:
                if self.debug:
                    print(f"[ ✓ ] Password Cracked: {password}")
                return password
            
            return None

        else:
            print("[ ! ] Unsupported hash type.")

    def hash_cracker(self, hash_type:str, input_hash:str, passwords:list) -> str:
        """
            Function to crack the the hash.

            Args:
                input_hash  (str): Hash value to crack.
                hash_type   (str): Type of the hash to crack.
                passwords   (list): list of passwords to brutforce.

            Returns:
                result   (str): returns the password if found ,else return None.
        """
        try:
            with ThreadPoolExecutor(max_workers=self.threads) as executor:
                tasks = {
                    executor.submit(self.crack_hash, input_hash, hash_type, password.strip()): password
                    for password in passwords
                }

                for future in tqdm(as_completed(tasks), total=len(tasks), desc="[ ↺ ] Cracking", ncols=80,colour="red"):
                    result = future.result()
                    if result is not None:
                        return result

        except Exception as Ue:
            print(f"[ ! ] Unexpected Error : {Ue}")


    def main(self ,input_hash:str,passwords:list) ->str:
        """
            Main function for the HashCracker.

            Args:
                input_hash  (str):  hash value to check.
                passwords   (list): list of passwords to brutforce.

            Returns:
                password   (str): returns the password for the cracked hash.
        """
        if self.debug:
            print(f"[ > ] Checking hash: {input_hash}")
            print("[ ↺ ] identifying hash type...")

        hash_type = self.identify_hash_type(input_hash)
        
        if hash_type:
            password = self.hash_cracker(hash_type,input_hash,passwords)
            return password
