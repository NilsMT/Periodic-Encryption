from distutils.core import setup

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="periodicencryption",
    packages = ["periodicencryption"], 
    version = '1.1.4',
    license='MIT',

    description="Allows you to encrypt and decrypt messages by the mean of Vigenere Cipher and Periodic Table of Elements",
    long_description=long_description,
    long_description_content_type='text/markdown',

    author="NilsMT",
    author_email="nilsmoreauthomas@gmail.com",

    url="https://github.com/NilsMT/periodic-encryption",

    install_requires = [
        'periodictable',
        'numpy',
        'pandas'
    ],

    keywords = ['CRYPTOGRAPHY', 'SECURITY', 'PERIODIC TABLE', 'CHEMICAL', 'WEIRD'],
  
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Security :: Cryptography',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)