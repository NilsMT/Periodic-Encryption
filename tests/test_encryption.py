import pytest

from periodicencryption import en, vc



def test_encrypt_decrypt_no_set_keys():
    message = "Hello, World!"
    row = vc.generate_row()

    encoded, puk, prk = en.encrypt_keys_auto(row, message)

    decrypted = en.decrypt(row, encoded, puk, prk)

    assert decrypted == message, f"Expected {message}, but got {decrypted}"

def test_encrypt_decrypt_set_keys():
    message = "Hello, World!"
    row = vc.generate_row()

    puk = "Kryptos"
    prk = "Hide"

    encrypted = en.encrypt_keys_manual(row, message, puk, prk)

    decrypted = en.decrypt(row, encrypted, puk, prk)

    assert decrypted == message, f"Expected {message}, but got {decrypted}"

def test_encrypt_decrypt_duplicate_in_private():
    row = vc.generate_row()

    puk, prk = "hj","aa"
    
    with pytest.raises(ValueError):
        en.decrypt(row, "message", puk, prk), f"Expected Error, but got ..."



def test_encrypt_decrypt_duplicate_in_public():
    row = vc.generate_row()

    puk, prk = "aa","hj"

    with pytest.raises(ValueError):
        en.decrypt(row, "message", puk, prk), f"Expected Error, but got ..."

def test_encrypt_decrypt_out_of_bound():
    message = "¤"
    row = vc.generate_row()

    encoded, puk, prk = en.encrypt_keys_auto(row, message)

    decrypted = en.decrypt(row, encoded, puk, prk)

    assert decrypted == message, f"Expected {message}, but got {decrypted}"