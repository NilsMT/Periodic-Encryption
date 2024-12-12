# Periodic Encryption

Classical cryptography, enhanced by chemistry !

## Summary

This package allows you to encrypt and decrypt messages by the mean of `Vigenere Cipher` and `Periodic Table of Elements`.

Here is a quick example :
```py
import periodicencryption as pe

row = pe.vc.generate_row()

puk, prk = pe.give_keys_from_string("Hello World")

print(puk)
print(prk)

enc = pe.encrypt(row, "Hello World")

print(enc)
print(pe.decrypt(row, puk, prk, enc))
```
```
257.0HafniumFer1846
HafniumFer
ueTqrD8G#zMbbg3vhB6J44
Hello World
```

## Table of contents

1. [Installation](#installation)
2. [About this package](#about-this-package)
3. [In a nutshell how does it work](#in-a-nutshell-how-does-it-work)
4. [Package Documentation](#package-documentation)

## Installation

Enter the following command :
```sh
pip install periodicencryption
```

## About this package

This package allow you to encrypt and decrypt messages by the mean of `Vigenere Cipher` and `Periodic Table of Elements`.

## In a nutshell how does it work

Strings are made up of characters, those characters have a unique code (generally called ASCII code). As it turns out, elements of the periodic table have number linked to them. So this package basicaly retrieve the chemical elements that share the same numbers as the characters. Then that list of element is encoded using a `Vigenere Cipher`

## Package Documentation

