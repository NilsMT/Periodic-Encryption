from distutils.core import setup

setup(
    name="periodic_encryption",
    packages = ["periodic_encryption"], 
    version = '1.0',
    license='MIT',

    description="Allow you to encrypt & decrypt strings using the periodic table elements",

    author="NilsMT",
    author_email="nilsmoreauthomas@gmail.com",

    url="https://github.com/NilsMT/periodic-encryption",

    install_requires = [
        'periodictable',
        'numpy',
        'wheel',
        'pandas',
        'pytest'
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