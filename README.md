# 🔐 hash-brute

**hash-brute** is a command-line, multi-threaded tool designed to crack cryptographic hashes by spraying password lists. It supports various hashing algorithms and leverages concurrent processing to expedite the cracking process.

---

## 🚀 Features

* Supports multiple hashing algorithms: **MD5**, **SHA-1**, **SHA-256**, and **SHA-512**.
* Automatic hash type identification using [hashid](https://github.com/psypanda/hashID).
* Multi-threaded execution for faster performance.
* Customizable wordlists for password spraying.
* Progress tracking with `tqdm` integration.
* Modular and extensible Python codebase.([github.com][1])

---

## 📦 Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/pevinkumar10/hash-brute.git
   cd hash-brute
   ```



2. **Installation**
   ```bash
   pip3 install -r requirements.txt

   ```
    or ,if you want to install it as a tool.
   ```
    sudo python3 setup.py install

   ```

---

## 🛠️ Usage

```bash
python hashbrute.py --hash <hash_value> [--wordlist <path_to_wordlist>] [--threads <number_of_threads>] [--debug]
```


### **Options:**

* `--hash` or `-H`: The hash value to crack.
* `--wordlist` or `-w`: Path to the password wordlist file. Defaults to a built-in list if not provided.
* `--threads` or `-t`: Number of threads to use. Default is 40.
* `--debug` or `-d`: Enable debug mode for verbose output.

### **Example:**

```bash
python hashbrute.py --hash 5d41402abc4b2a76b9719d911017c592 --wordlist rockyou.txt --threads 50 --debug
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
