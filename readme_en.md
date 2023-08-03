# EasyZipDecryptor: Simple Compression Password Cracker

[中文版README](./readme.md)

## Introduction
This is a simple password cracking script that helps you crack passwords for zip, rar, and 7z compressed files. Password cracking is a sensitive task, and to use it for legal, compliant, and ethical purposes, make sure you have obtained authorization or permission and abide by applicable laws.This script is intended to be used only for academic research and other legal purposes. If the use of this script results in the violation of local laws and regulations, the user will be responsible for the consequences.

## Features
- Supports password cracking for zip, rar, and 7z formats.
- Uses a dictionary file as a password list, attempting each password for cracking.
- Prints the cracked password and stops when successful; displays failure message on unsuccessful cracking.

## Prerequisites
Before using the script, ensure you have installed the following Python libraries: `rarfile`, `zipfile`, and `py7zr`. You can install them using pip:

```bash
pip install rarfile zipfile py7zr
```

## Usage
1. Create a Dictionary File: Prepare a dictionary file containing the list of passwords. Each password should be on a separate line. You can customize the password list as needed for your research. In [My Clouddisk](https://cloud.gloridust.xyz/s/5mu3), we provide a simple password dictionary. You can use it after unzipping. The content of the dictionary comes from the Internet.(in [./dic/passwords.zip](./dic/passwords.zip) is also avavaible.)


2. Run the Script: Open a terminal or command prompt, navigate to the directory containing the script file, and run the Python script. Follow the prompts to input the dictionary file location and the compressed file location.

## Example Usage
Assuming your dictionary file is named `passwords.txt`, and the compressed file is named `example.zip`, you can execute the following command to run the script:

```bash
python unzip.py
```

Then, follow the prompts to input the dictionary file location and compressed file location.

## Important Notes
- This script is intended for academic research purposes only. Please adhere to legal requirements and ensure you have obtained proper authorization.
- Password cracking involves security and privacy concerns, and unauthorized password cracking is illegal.
- Using a more comprehensive dictionary file may improve the success rate of password cracking, but ensure you obtain these dictionary files legally.

## Summary
This simple password cracking script can help you crack passwords for zip, rar, and 7z compressed files in academic research. Remember to use it legally and responsibly, ensuring you have proper authorization and permissions. If you need further assistance or have any other questions, feel free to ask.