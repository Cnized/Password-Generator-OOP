# 🔐 Password Generator  

A Python project that generates secure and customizable passwords.  
It includes three types of generators: **PIN codes, random passwords, and memorable word-based passwords**.  

---

## 🚀 Features  

- ✅ **PIN Code Generator** – Generates numeric PINs of any length.  
- ✅ **Random Password Generator** – Create random passwords with:  
  - Letters (default)  
  - Optional numbers  
  - Optional symbols  
- ✅ **Memorable Password Generator** – Generates passwords made of real words from the NLTK corpus, easier to remember, with options to:  
  - Set number of words  
  - Choose a separator (e.g., `-` or `_`)  
  - Randomly capitalize words  

---

## 🛠️ Installation  

1. Clone the repository:  
   ```bash
   git clone https://github.com/your-username/password-generator.git
   cd password-generator
   ```
## 	
2.	Install dependencies:
```bash
pip install -r requirements.txt
```
##
3. Download the NLTK words corpus (only needed for MemorablePasswordGenerator):
```bash
import nltk
nltk.download("words")
```
## 📖 Usage
Run the script directly:
```bash
python src/main.py
```
Example Output:
```bash
Random Password: K9!aS&3#XqLp
PIN Code: 4821
Memorable Password: tiger-DESK-glass-apple
```
## 📂 Project Structure
```bash
password-generator/
│── src/
│   ├── main.py          # Main script
│   ├── old_main.py      # Old version (kept for reference)
│── README.md            # Documentation
│── requirements.txt     # Dependencies
```
## 📦 Classes Documentation

This project contains three main password generator classes:

---

### 🔹`PinCodeGenerator`

Generates numeric PINs of a given length.

### Example
```python
from main import PinCodeGenerator

pin = PinCodeGenerator(4)
print(pin.generator())  # Example: "4928"
```
---
### 🔹 RandomPasswordGenerator

Generates random passwords with customizable options.
- •	Letters (default)
- •	Optional numbers
- •	Optional symbols

### Example
```python
from main import RandomPasswordGenerator

rpassword = RandomPasswordGenerator(12, include_numbers=True, include_symbols=True)
print(rpassword.generator())  # Example: "Ax7!dP#kR2fQ"
```
---
### 🔹 MemorablePasswordGenerator

Generates passwords made of real words (from NLTK corpus).
Options:
- •	Number of words
- •	Separator between words
- •	Random capitalization

### Example
```python
from main import MemorablePasswordGenerator

memorable = MemorablePasswordGenerator(4, seperator="-", be_capital=True)
print(memorable.generator())  # Example: "House-dog-CHAIR-bird"
```
---
## 📄 License
This project is licensed under the MIT License – feel free to use and modify.
## 👨‍💻Author
💻 Built with ❤️ by Kian Kheiri N. ([@Cnized](https://github.com/Cnized))