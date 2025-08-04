# 🔥 CharMinder

> A character encoding detective for text files and URLs - catch encoding issues before they evolve into problems!

[![PyPI version](https://badge.fury.io/py/charminder.svg)](https://badge.fury.io/py/charminder)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

CharMinder is a powerful encoding validation tool that detects character encoding issues in text files with precise, character-level reporting. It supports both local files and remote URLs (including GitHub).

## ✨ Features

- 🕵️ **Precise Detection**: Character-level reporting with exact line/column positions
- 🌐 **URL Support**: Works with HTTP/HTTPS URLs and GitHub blob URLs
- 🎯 **Multiple Encodings**: UTF-8, UTF-16, UTF-32, ASCII validation
- 📊 **Detailed Reports**: Unicode codepoints, context, and confidence levels
- 🔄 **GitHub Integration**: Automatic blob-to-raw URL conversion
- ⚡ **Fast & Reliable**: Built on charset_normalizer for accurate detection

## 🚀 Quick Start

### Installation
```bash
pip install charminder
```

### Basic Usage
```bash
# Check a local file
charminder -f myfile.txt -e UTF8

# Check a remote URL
charminder -f https://example.com/data.csv -e ASCII

# Check a GitHub file (blob URL auto-converted)
charminder -f https://github.com/user/repo/blob/main/data.json -e UTF8
```

## 📖 Usage Examples

### Valid File
```bash
$ charminder -f clean_file.txt -e UTF8
✓ clean_file.txt: Valid UTF8 encoding
```

### File with Issues
```bash
$ charminder -f problematic_file.txt -e UTF8
✗ problematic_file.txt: Invalid UTF8 encoding
  • Invalid character '—' (U+2014) at line 15, column 23
    Context: ...Hello — this is...
  • Invalid character '©' (U+00A9) at line 20, column 5
    Context: ...© 2024 Company...
```

## 🛠️ Development

CharMinder is built with:
- **charset_normalizer** for encoding detection
- **click** for the CLI interface
- **urllib** for URL handling

## 📝 License

Apache License, Version 2.0, ([LICENSE](LICENSE))

## 🤝 Contributing

Contributions welcome! Please read our [Contributing Guide](CONTRIBUTING.md) first.

---

*CharMinder - I choose you!* 🔥⚡