import periodictable as pt
import re
from periodicencryption import vigenerecipher as vc
from periodicencryption import element as el

def give_keys_from_string(string: str) -> tuple[str, str]:
    """
    Generates the private and public keys, needed for the encryption process, from a string.
    """
    element_list = el.turn_str_into_el(string)

    if len(element_list) == 0:
        raise ValueError("Element list cannot be empty.")

    first_element = element_list[0]
    last_element = element_list[-1]

    # private key : 1st element name + last element symbol + 1st element symbol + last element name
    private_key = first_element.name.capitalize() + last_element.symbol + first_element.symbol + last_element.name.capitalize()
    # public key : last element mass + 1st element name + last element name + 1st element mass
    public_key = str(last_element.mass) + first_element.name.capitalize() + last_element.name.capitalize() + str(first_element.mass)

    return "".join(dict.fromkeys(public_key)), "".join(dict.fromkeys(private_key))

def encrypt_keys_manual(row: str, public_key: str, private_key: str, message: str) -> str:
    """
    Encrypts a message using the Vigenère cipher and the periodic table elements, with the specified keys.
    """
    if len("".join(dict.fromkeys(public_key))) != len(public_key) or len("".join(dict.fromkeys(private_key))) != len(private_key):
        raise ValueError("Public and private keys must not contain duplicates.")
    
    if len(message) == 0:
        raise ValueError("Message cannot be empty.")
    
    # 1 - turn message into elements

    element_list = el.turn_str_into_el(message)

    # 2 - encode message using Vigenère cipher

    string_element = ''.join([e.symbol for e in element_list])

    encoded = vc.vignere_encode(row, public_key, private_key, string_element)
    
    return encoded

def encrypt_keys_auto(row: str, message: str) -> str:
    """
    Encrypts a message using the Vigenère cipher and the periodic table elements, keys are generated from the message.
    """
    if len(message) == 0:
        raise ValueError("Message cannot be empty.")

    public_key, private_key = give_keys_from_string(message)
    
    return encrypt_keys_manual(row, public_key, private_key, message)


def decrypt(row: str, public_key: str, private_key: str, encoded: str) -> str:
    """
    Decrypts a message using the Vigenère cipher and the periodic table elements.
    """
    if len("".join(dict.fromkeys(public_key))) != len(public_key) or len("".join(dict.fromkeys(private_key))) != len(private_key):
        raise ValueError("Public and private keys must not contain duplicates.")
    
    if len(encoded) == 0:
        raise ValueError("Message cannot be empty.")
    
    # 1 - decode message using Vigenère cipher

    decoded = vc.vignere_decode(row, public_key, private_key, encoded)

    # 2 - turn elements into message

    elements_names = re.findall('[A-Z][^A-Z]*', decoded)
    elements_list = [el.get_el_by_symbol(name) for name in elements_names]

    message = el.turn_el_into_str(elements_list)

    return message