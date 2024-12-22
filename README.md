# Advanced Code Obfuscator

### 🛡️ Obfuscate Your Code Across Multiple Programming Languages

The **Advanced Code Obfuscator** is a powerful tool designed for developers and security professionals to obscure source code, making it difficult to reverse-engineer or analyze. It supports **Python**, **C++**, and **C#**, and incorporates advanced features such as variable name randomization, string encryption, and comment removal.

---

## 🚀 Features

- **Multi-Language Support**: Obfuscate Python, C++, and C# source code.
- **Variable Name Obfuscation**: Automatically replace variable names with randomized strings.
- **String Encryption**: Convert string literals into encrypted formats (e.g., hex, Base64).
- **Comment Removal**: Strip all comments from the code to reduce readability.
- **Customizable Options**: Enable or disable specific features (e.g., string encryption, variable obfuscation).
- **Reserved Keyword Handling**: Ensure language-specific keywords remain unaffected.
- **Cross-Platform Compatibility**: Works on Windows, macOS, and Linux.

---

## 🛠️ Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/Advanced-Code-Obfuscator.git
   cd Advanced-Code-Obfuscator
   ```

2. **Install Dependencies**:
   Ensure Python 3.6+ is installed. Install additional dependencies using:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Tool**:
   ```bash
   python code_obfuscator.py --help
   ```

---

## 📋 Usage

### **Basic Command**
```bash
python code_obfuscator.py -i <input_file> -o <output_file> -l <language> [options]
```

### **Options**

| Flag               | Description                                                                                  |
|--------------------|----------------------------------------------------------------------------------------------|
| `-i, --input`      | Input file to obfuscate (required).                                                          |
| `-o, --output`     | Output file to save the obfuscated code (required).                                          |
| `-l, --language`   | Programming language of the input file (`python`, `c++`, `c#`).                              |
| `--no-var`         | Disable variable name obfuscation (default: enabled).                                        |
| `--no-strings`     | Disable string encryption (default: enabled).                                                |
| `--no-comments`    | Disable comment removal (default: enabled).                                                  |

### **Examples**

#### 1. Obfuscate a Python file:
```bash
python code_obfuscator.py -i script.py -o obfuscated_script.py -l python
```

#### 2. Obfuscate a C++ file with string encryption disabled:
```bash
python code_obfuscator.py -i code.cpp -o obfuscated_code.cpp -l c++ --no-strings
```

#### 3. Obfuscate a C# file while retaining comments:
```bash
python code_obfuscator.py -i program.cs -o obfuscated_program.cs -l c# --no-comments
```

---

## 📜 Advanced Features

### **1. String Encryption**
- Converts all string literals into an encrypted format.
- Default: Hexadecimal encoding.
- Planned Enhancement: Add AES encryption for additional security.

### **2. Variable Name Obfuscation**
- Replaces variable names with random strings.
- Avoids reserved keywords and retains syntax integrity.

### **3. Comment Removal**
- Removes all single-line (`#`, `//`) and multi-line (`/* */`) comments to reduce readability.

---

## 🌟 Supported Languages

| Language | Features Supported          | Notes                                      |
|----------|-----------------------------|--------------------------------------------|
| Python   | Variables, Strings, Comments| Compatible with Python 3.6+                |
| C++      | Variables, Strings, Comments| Handles standard and STL-based syntax      |
| C#       | Variables, Strings, Comments| Supports modern C# syntax (up to C# 9.0)   |

---

## 🔍 Example

### Input (`example.py`):
```python
# This is a simple Python script
def greet_user(name):
    print(f"Hello, {name}!")  # Print greeting

greet_user("Alice")
```

### Output (`obfuscated_example.py`):
```python
def RkYuiToxPz(name):
    print("\x48\x65\x6c\x6c\x6f\x2c\x20" + name + "\x21")

RkYuiToxPz("\x41\x6c\x69\x63\x65")
```

---

## 🛡️ Roadmap

- [ ] Add support for **JavaScript** and **Java**.
- [ ] Introduce **AES encryption** for strings.
- [ ] Add **syntax validation** to prevent invalid output.
- [ ] Provide a web-based interface for ease of use.

---

## 🤝 Contributing

Contributions are welcome! Please fork the repository and create a pull request. Ensure your code adheres to the existing style and include appropriate tests.

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](./https://github.com/genxcyber/Advanced-Code-Obfuscator/blob/main/LICENSE) file for details.

---

## 🌐 Author

Created by **[GenXCyber](https://github.com/genxcyber)**  
For more tools and tutorials, visit **[GenX Cyber](https://genxcyber.com/tools/)**.
