import hashlib
import tkinter as tk
from tkinter import filedialog

def get_fixed_algorithms():
    return ["md5", "sha1", "sha256", "sha512", "blake2b", "blake2s", "sha3_256", "sha3_512", "sha224", "sha384"]

def generate_hash(input_data, algorithm):
    try:
        hasher = hashlib.new(algorithm)
        hasher.update(input_data.encode('utf-8'))
        return hasher.hexdigest()
    except ValueError:
        return "Invalid algorithm selected."

def generate_file_hash(file_path, algorithm):
    try:
        hasher = hashlib.new(algorithm)
        with open(file_path, "rb") as f:
            while chunk := f.read(8192):
                hasher.update(chunk)
        return hasher.hexdigest()
    except ValueError:
        return "Invalid algorithm selected."

def select_file():
    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', True)  # Bring the window to the front
    file_path = filedialog.askopenfilename()
    root.destroy()
    return file_path

def main():
    algorithms = get_fixed_algorithms()
    print("Available Hash Algorithms:")
    for i, algo in enumerate(algorithms, 1):
        print(f"{i}. {algo}")
    
    choice = int(input("Enter the choice number of the hash algorithm: "))
    if choice < 1 or choice > len(algorithms):
        print("Invalid choice.")
        return
    algorithm = algorithms[choice - 1]
    
    print("1. Hash Text")
    print("2. Hash File")
    mode = int(input("Enter your choice: "))
    
    if mode == 1:
        input_data = input("Enter the text to hash: ")
        hash_value = generate_hash(input_data, algorithm)
    elif mode == 2:
        file_path = select_file()
        if file_path:
            hash_value = generate_file_hash(file_path, algorithm)
        else:
            print("No file selected.")
            return
    else:
        print("Invalid mode selected.")
        return
    
    print(f"Hash ({algorithm}): {hash_value}")
    
if __name__ == "__main__":
    main()