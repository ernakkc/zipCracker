# 🔐 ZIP Cracker

<div align="center">

![Python](https://img.shields.io/badge/Python-3-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/platform-Windows-blue?style=for-the-badge)
![License](https://img.shields.io/github/license/ernakkc/zipCracker?style=for-the-badge)

*Password recovery tool for encrypted ZIP archives using dictionary and brute-force attacks*

[🚀 Features](#-features) • [⚠️ Disclaimer](#-disclaimer) • [📖 Usage](#-usage)

</div>

---

## 📖 Overview

ZIP Cracker is a Python-based tool designed to recover lost passwords from encrypted ZIP archives. It supports dictionary attacks using wordlists and can help recover forgotten passwords for your own files.

## ✨ Features

- 🔑 **Dictionary Attack**: Uses wordlist files for password recovery
- ⚡ **Fast Processing**: Multi-threaded password testing
- 📊 **Progress Tracking**: Real-time progress updates
- 📝 **Logging**: Detailed operation logs
- 🎯 **Success Reporting**: Displays found passwords immediately
- 🗂️ **Custom Wordlists**: Support for any text-based wordlist

## ⚠️ Disclaimer

**IMPORTANT - Legal and Ethical Use Only**

This tool is provided for **educational purposes** and **password recovery on your own files only**.

- ❌ **DO NOT** use on files you don't own
- ❌ **DO NOT** use for unauthorized access
- ❌ **DO NOT** use for illegal activities
- ✅ **DO** use to recover your own forgotten passwords
- ✅ **DO** use for educational cybersecurity learning

**The author is not responsible for misuse of this tool. Always comply with applicable laws.**

## 🚀 Installation

### Prerequisites
- Python 3.x
- pip package manager

### Quick Setup

```bash
git clone https://github.com/ernakkc/zipCracker.git
cd zipCracker
pip install -r requirements.txt
```

## 💻 Usage

### Basic Usage

```bash
python zipCracker.py
```

The program will prompt you for:
1. Path to the encrypted ZIP file
2. Path to the wordlist file
3. Start the cracking process

### Command Line Arguments (if supported)

```bash
python zipCracker.py --zip file.zip --wordlist passwords.txt
```

### Wordlist Format

Wordlist should be a text file with one password per line:
```
password123
admin
qwerty123
...
```

## 📁 Project Structure

```
zipCracker/
├── zipCracker.py       # Main script
├── requirements.txt    # Python dependencies
├── wordlists/         # Sample wordlists (optional)
└── README.md          # This file
```

## 🛠️ How It Works

1. **Load ZIP File**: Opens the encrypted ZIP archive
2. **Load Wordlist**: Reads passwords from wordlist file
3. **Test Passwords**: Tries each password sequentially
4. **Success**: Displays password if found
5. **Failure**: Reports if password not in wordlist

### Algorithm

```python
for password in wordlist:
    try:
        zip_file.extract(password)
        print(f"Password found: {password}")
        break
    except:
        continue
```

## 📊 Performance

- **Speed**: Depends on CPU and ZIP encryption strength
- **Traditional ZIP**: ~1000-10000 passwords/second
- **AES Encrypted**: Slower (~100-1000 passwords/second)
- **Multi-threading**: Can improve speed on multi-core systems

## 🔧 Advanced Features

### Custom Wordlists

Create your own wordlists:
```bash
# Common passwords
echo "123456" >> mylist.txt
echo "password" >> mylist.txt

# Generated combinations
crunch 4 8 abc123 > generated.txt
```

### Integration with Wordlist Generators

```bash
# Using John the Ripper's wordlist
john --wordlist=/path/to/wordlist --rules --stdout > custom.txt

# Using CeWL for website-based wordlists
cewl http://example.com > website-words.txt
```

## ⚡ Optimization Tips

1. **Start with Common Passwords**: Use common password lists first
2. **Custom Wordlists**: Create lists based on known information
3. **Multi-threading**: Enable if supported in your version
4. **GPU Acceleration**: Consider GPU-based crackers for serious use
5. **Rainbow Tables**: Pre-computed hash tables can be faster

## 🔍 Troubleshooting

### "Permission Denied"
```bash
# Ensure you have read access to ZIP file
chmod +r encrypted.zip
```

### "Module Not Found"
```bash
# Reinstall dependencies
pip install --upgrade -r requirements.txt
```

### Slow Performance
- Use smaller, targeted wordlists
- Check CPU usage
- Consider using dedicated password recovery tools for heavy tasks

## 📚 Resources

### Wordlist Sources
- [SecLists](https://github.com/danielmiessler/SecLists)
- [RockYou](https://github.com/brannondorsey/naive-hashcat/releases)
- [CrackStation](https://crackstation.net/crackstation-wordlist-password-cracking-dictionary.htm)

### Related Tools
- **John the Ripper**: Advanced password cracker
- **Hashcat**: GPU-accelerated password recovery
- **fcrackzip**: Specialized ZIP password cracker

## 🤝 Contributing

Contributions are welcome! Ideas for improvements:
- GPU acceleration support
- Hybrid attack modes
- Progress saving/resume functionality
- Improved UI/UX
- Additional encryption type support

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👤 Author

**Eren Akkoç**
- GitHub: [@ernakkc](https://github.com/ernakkc)
- Email: ern.akkc@gmail.com

## 🔒 Security Note

Remember to:
- Use strong, unique passwords for your archives
- Store passwords securely (password manager)
- Enable 2FA where possible
- Regular security audits of your files

---

<div align="center">

**⚠️ Educational Use Only - Always Act Ethically! 🔐**

[![GitHub stars](https://img.shields.io/github/stars/ernakkc/zipCracker?style=social)](https://github.com/ernakkc/zipCracker)
[![GitHub forks](https://img.shields.io/github/forks/ernakkc/zipCracker?style=social)](https://github.com/ernakkc/zipCracker/fork)
[![GitHub issues](https://img.shields.io/github/issues/ernakkc/zipCracker)](https://github.com/ernakkc/zipCracker/issues)
[![GitHub last commit](https://img.shields.io/github/last-commit/ernakkc/zipCracker)](https://github.com/ernakkc/zipCracker/commits)

</div>
    

