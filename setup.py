from distutils.core import setup

setup(
    name="Periodic_Encryption",
    packages = ["Periodic_Encryption"], 
    version = '1.0',
    license='MIT',

    description="Allow you to encrypt & decrypt strings using the periodic table elements",

    author="Nils Moreau--Thomas",
    author_email="nilsmoreauthomas@gmail.com",

    url="https://github.com/NilsMT/periodic-encryption",
    download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz'

    install_requires = [
        'periodictable',
        'numpy',
        'wheel',
        'pandas',
        'pytest'
    ]
    
    keywords = ['CRYPTOGRAPHY', 'SECURITY', 'PERIODIC TABLE', 'CHEMICAL', 'WEIRD'],
  
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers, Cryptography Engineers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)