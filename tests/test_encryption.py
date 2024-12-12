import pytest
from periodic_encryption import encryption as en
from periodic_encryption import element as el
from periodic_encryption import vigenerecipher as vc



def test_encrypt_decrypt():
    message = "Hello, World!"
    row = vc.generateRow()

    encrypted = en.encrypt(row, message)

    publicKey, privateKey = en.giveKeysFromString(message)

    print(publicKey, privateKey)

    decrypted = en.decrypt(row, publicKey, privateKey, encrypted)

    assert decrypted == message, f"Expected {message}, but got {decrypted}"



def test_encrypt_decrypt_duplicate_in_private():
    message = "Hello, World!"
    row = vc.generateRow()

    encrypted = en.encrypt(row, message)

    publicKey, privateKey = "hj","aa"
    
    with pytest.raises(ValueError):
        en.decrypt(row, publicKey, privateKey, encrypted), f"Expected Error, but got ..."



def test_encrypt_decrypt_duplicate_in_public():
    message = "Hello, World!"
    row = vc.generateRow()

    encrypted = en.encrypt(row, message)

    publicKey, privateKey = "aa","hj"

    with pytest.raises(ValueError):
        en.decrypt(row, publicKey, privateKey, encrypted), f"Expected Error, but got ..."