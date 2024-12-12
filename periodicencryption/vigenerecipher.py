import string
import pandas as pd

def generate_row() -> str:
    """
    Generates a row of characters that can be used for Vigenère cipher.
    It includes ASCII letters, digits, special characters, whitespace, and some accented  letters.
    """
    letters = string.ascii_letters
    digits = string.digits
    special_characters = string.punctuation
    whitespace = string.whitespace
    unicode_characters = "ÀÁÂÃÄÅàáâãäåÈÉÊËèéêëÌÍÎÏìíîïÒÓÔÕÖØòóôõöøÙÚÛÜùúûüÝŸýÿ"

    return letters + digits + special_characters + whitespace + unicode_characters



def generate_table(row: str, public_key: str) -> pd.DataFrame:
    """
    Generates the Vigenère table by shifting the row based on the `public_key`.\n
    The `public_key` determines the shifting for each row.
    """
    row_without_key = "".join([char for char in row if char not in public_key])
    df_row = list(public_key + row_without_key)

    df = pd.DataFrame(columns=list(df_row), index=list(df_row))

    # Create the first row
    df.loc[df_row[0]] = df_row

    df.index
    # Create the following rows
    for i in range(1, len(row)):
        df_row = df_row[1:] + df_row[:1]

        df.loc[
            df.index.tolist()[i]
        ] = df_row

    return df



def vignere_encode(row: str, public_key: str, private_key: str, message: str) -> str:
    """
    Encodes a message using the Vigenère cipher.
    """
    table = generate_table(row, public_key)
    encoded_message = ""

    # Ensure len(private_key) is at least len(message)
    private_key = (private_key * ((len(message) // len(private_key)) + 1))[:len(message)]

    for m,k in zip(message, private_key):
        encoded_message += table.loc[m][k]
    
    return encoded_message



def vignere_decode(row: str, public_key: str, private_key: str, encoded_message: str) -> str:
    """
    Decodes a message using the Vigenère cipher.
    """
    table = generate_table(row, public_key)
    decoded_message = ""

    # Ensure len(private_key) is at least len(encoded_message)
    private_key = (private_key * ((len(encoded_message) // len(private_key)) + 1))[:len(encoded_message)]

    for m,k in zip(encoded_message, private_key):
        # Find the column (public_key) and look for the original row (message character)
        decoded_message += table[table[k] == m].index[0]
    
    return decoded_message