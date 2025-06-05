# 🔐 HashBrute

**hash-brute** is a command-line, multi-threaded tool designed to crack cryptographic hashes by spraying password lists. It supports various hashing algorithms and leverages concurrent processing to expedite the cracking process.

---

## 🚀 Features

* Supports multiple hashing algorithms: **MD5**, **SHA-1**, **SHA-256**, and **SHA-512**.
* Automatic hash type identification using [hashid](https://github.com/psypanda/hashID).
* Multi-threaded execution for faster performance.
* Customizable wordlists for password spraying.
* Progress tracking with `tqdm` integration.
* Modular and extensible Python codebase.

---

## Tool Structure:

```
.
├── LICENSE                   # LICENSE.
├── README.md                 # Readme file.
├── UPDATELOG.md              # Update log file.
├── hashbrute                 # Hash Brute main directory.
│   ├── __init__.py
│   ├── hashbrute.py             # HashBrute handler.
│   ├── modules                     # Modules for HashBrute.
│   │   ├── __init__.py
│   │   ├── cli                        # Cli modules.
│   │   │   ├── __init__.py
│   │   │   └── cli.py                    # Cli handler file.
│   │   ├── core.py                    # Core file for HashBrute.
│   │   ├── cracker                    # Hash Cracker module.
│   │   │   ├── __init__.py    
│   │   │   └── cracker.py                # Hash cracker handler.
│   │   └── utility                    # Utility file for support funtions.
│   │       ├── __init__.py
│   │       └── utils.py                  # Utilities for support functions.
│   └── wordlist                 # Default wordlist directory.
│       └── default-wordlist.txt
├── requirements.txt          # requirements for HashBrute.
└── setup.py                  # Setup file for HashBrute.
```

---

## 📦 Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/pevinkumar10/hash-brute.git
   cd hash-brute
   ```



2. **Installation**
- It needed hashid ,tqdm as dependency . You can install it from pypi or by this following command.
   - Ensure you are in the tool directory that hash setup.py
      ```bash
      pipx install .

      ```

---

## 🛠️ Usage

```bash
hashbrute --hash <hash_value> [--wordlist <path_to_wordlist>] [--threads <number_of_threads>] [--debug]
```


### **Options:**

* `--hash` or `-H`: The hash value to crack.
* `--wordlist` or `-w`: Path to the password wordlist file. Defaults to a built-in list if not provided.
* `--threads` or `-t`: Number of threads to use. Default is 40.
* `--debug` or `-d`: Enable debug mode for verbose output.

### **Example:**

```bash
hashbrute --hash 5d41402abc4b2a76b9719d911017c592 --wordlist rockyou.txt --threads 50 --debug
```

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

---

## 🤝 Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

---

## 📬 Contact

For any inquiries or feedback, please open an issue on the [GitHub repository](https://github.com/pevinkumar10/hash-brute/issues).

---

*Happy Cracking!* 🔓

---
