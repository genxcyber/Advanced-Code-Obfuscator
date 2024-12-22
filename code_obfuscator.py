import argparse
import random
import string
import re

def randomize_name(name_length=8):
    """Generate a randomized name."""
    return ''.join(random.choices(string.ascii_letters, k=name_length))

def encrypt_string(s, method="hex"):
    """Encrypt a string using the selected method."""
    if method == "hex":
        return ''.join(f"\\x{ord(c):02x}" for c in s)
    elif method == "base64":
        import base64
        return base64.b64encode(s.encode()).decode()
    else:
        raise ValueError("Unsupported encryption method!")

def remove_comments(code, lang):
    """Remove comments based on the programming language."""
    if lang == "python":
        return re.sub(r"#.*", "", code)
    elif lang in ["c++", "c#"]:
        return re.sub(r"//.*|/\*[\s\S]*?\*/", "", code)
    return code

def obfuscate_variables(code, lang):
    """Obfuscate variable names based on the language."""
    var_map = {}
    
    def replace_var(match):
        var_name = match.group(0)
        if var_name not in var_map:
            var_map[var_name] = randomize_name()
        return var_map[var_name]
    
    if lang == "python":
        return re.sub(r"\b[a-zA-Z_][a-zA-Z0-9_]*\b(?=\s*=)", replace_var, code)
    elif lang in ["c++", "c#"]:
        return re.sub(r"\b[a-zA-Z_][a-zA-Z0-9_]*\b(?=\s*(=|;))", replace_var, code)
    else:
        return code

def obfuscate_strings(code, lang):
    """Encrypt string literals based on the language."""
    if lang in ["python", "c++", "c#"]:
        return re.sub(r"(\".*?\"|'.*?')", lambda m: f'"{encrypt_string(m.group(0)[1:-1])}"', code)
    return code

def obfuscate_code(input_file, output_file, lang, obfuscate_vars=True, encrypt_strings=True, remove_com=True):
    """Perform the obfuscation process."""
    with open(input_file, 'r') as infile:
        code = infile.read()

    if remove_com:
        code = remove_comments(code, lang)
    if obfuscate_vars:
        code = obfuscate_variables(code, lang)
    if encrypt_strings:
        code = obfuscate_strings(code, lang)

    with open(output_file, 'w') as outfile:
        outfile.write(code)

    print(f"[+] Obfuscation complete! Output written to {output_file}")

def main():
    parser = argparse.ArgumentParser(description="Advanced Code Obfuscator Tool")
    parser.add_argument("-i", "--input", required=True, help="Input file to obfuscate")
    parser.add_argument("-o", "--output", required=True, help="Output obfuscated file")
    parser.add_argument("-l", "--language", required=True, choices=["python", "c++", "c#"], help="Programming language of the input file")
    parser.add_argument("--no-var", action="store_false", help="Disable variable name obfuscation")
    parser.add_argument("--no-strings", action="store_false", help="Disable string encryption")
    parser.add_argument("--no-comments", action="store_false", help="Disable comment removal")

    args = parser.parse_args()

    try:
        obfuscate_code(
            input_file=args.input,
            output_file=args.output,
            lang=args.language,
            obfuscate_vars=args.no_var,
            encrypt_strings=args.no_strings,
            remove_com=args.no_comments
        )
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
