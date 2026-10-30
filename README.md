# Hashify

<p align="center">
  <strong>A lightweight file hashing utility.</strong>
  <br>
  Generate, compare and verify file hashes directly from your terminal.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/License-MIT-white?style=flat-square" />
  <img src="https://img.shields.io/badge/Platform-Windows-blue?style=flat-square" />
  <img src="https://img.shields.io/badge/Language-Python-yellow?style=flat-square" />
</p>

<br>

## Overview

Hashify is a lightweight command-line utility for generating and verifying cryptographic file hashes. It provides a straightforward interface with support for multiple hashing algorithms.

## Features

| Feature | Description |
|:--|:--|
| **Hash generation** | Generate hashes for individual files. |
| **Hash verification** | Verify files against existing hashes. |
| **Hash comparison** | Compare two files using their hashes. |
| **Algorithm selection** | Choose from multiple hashing algorithms. |

## Getting Started

Run Hashify directly from your terminal:

```bash
hashify [command] [arguments]
```

### Available Commands

| Command | Description |
|:--|:--|
| `hash` | Generate a file hash. |
| `verify` | Verify a file against an existing hash. |
| `compare` | Compare two files. |
| `help` | Display available commands. |

### Choosing an Algorithm

Hashify supports algorithm selection through the `--algorithm` or `-a` argument.

```bash
hashify hash file.exe --algorithm SHA256
hashify hash file.exe -a SHA512
```

If no algorithm is specified, **SHA256** is used by default.

### Examples

**Generate a hash**
```bash
hashify hash file.exe
```

**Generate a hash using a specific algorithm**
```bash
hashify hash file.exe -a SHA512
hashify hash file.exe -a MD5
```

**Verify a file**
```bash
hashify verify file.exe <hash> -a SHA256
```

**Compare two files**
```bash
hashify compare file1.exe file2.exe -a SHA256
```

## Supported Algorithms

| Algorithm | Hash Length |
|:--|--:|
| `SHA512` | 512-bit |
| `SHA256` | 256-bit |
| `SHA1` | 160-bit |
| `MD5` | 128-bit |

## Installation

1. Download the latest installer from [GitHub Releases](https://github.com/zzylenn/hashify/releases).
2. Run the installer and follow the setup instructions.
3. Open a terminal.
4. Run `hashify` to get started.

## Building from Source

Hashify can be built from source using [PyInstaller](https://pyinstaller.org/).

### Requirements

- Python 3.10+
- PyInstaller

### Build Instructions

1. Clone the repository:

```bash
git clone https://github.com/zzylenn/hashify.git
cd hashify/src
```

2. Install the dependencies:

```bash
pip install -r requirements.txt
```

3. Build the executable:

```bash
pyinstaller --onefile --icon NONE --name hashify main.py
```

The compiled executable will be available in the `dist` directory.
The installer is created via [Inno Setup 6.6.1](https://archive.org/details/inno-setup-6.6.1.7z)
Build before using installer creation script.



## License

Hashify is distributed under the [MIT License](LICENSE).

Copyright © 2026 zylen.