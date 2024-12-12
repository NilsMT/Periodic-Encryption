import pytest
from periodicencryption import encryption as en
from periodicencryption import element as el
from periodicencryption import vigenerecipher as vc



def test_encrypt_decrypt_no_set_keys():
    message = "Hello, World!"
    row = vc.generate_row()

    encrypted = en.encrypt_keys_auto(row, message)

    public_key, private_key = en.give_keys_from_string(message)

    decrypted = en.decrypt(row, public_key, private_key, encrypted)

    assert decrypted == message, f"Expected {message}, but got {decrypted}"

def test_encrypt_decrypt_set_keys():
    message = "Hello, World!"
    row = vc.generate_row()

    puk = "Kryptos"
    prk = "Hide"

    encrypted = en.encrypt_keys_manual(row, puk, prk, message)

    decrypted = en.decrypt(row, puk, prk, encrypted)

    assert decrypted == message, f"Expected {message}, but got {decrypted}"

def test_encrypt_decrypt_duplicate_in_private():
    row = vc.generate_row()

    public_key, private_key = "hj","aa"
    
    with pytest.raises(ValueError):
        en.decrypt(row, public_key, private_key, "message"), f"Expected Error, but got ..."



def test_encrypt_decrypt_duplicate_in_public():
    row = vc.generate_row()

    public_key, private_key = "aa","hj"

    with pytest.raises(ValueError):
        en.decrypt(row, public_key, private_key, "message"), f"Expected Error, but got ..."