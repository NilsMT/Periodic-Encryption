from periodicencryption import vc

def test_unknown_not_in_row():
    row = vc.generate_row()
    assert row.find("�") == -1, f"Character '�' should not be in the row."


def test_generate_table():

    puk = "1234"
    row = vc.generate_row()
    first_row = puk+ vc.generate_row().replace(puk, "")
    second_row = first_row[1:] + first_row[:1]

    table = vc.generate_table(row, puk)

    assert table[first_row[0]].to_list() == list(first_row), f"Expected first row to start with ({puk}), but got {table[0]}"
    assert table[first_row[1]].to_list() == list(second_row), f"Expected {second_row} to be offsetted by 1, but got {table[1]}"



def test_encode_decode():
    
    row = vc.generate_row()
    puk = "kryptos"
    message = "secretmessage"
    prk = "hidden"

    res_encoded = vc.vigenere_encode(row, message, puk, prk)
    res_decoded = vc.vigenere_decode(row, res_encoded, puk, prk)

    assert res_encoded == "qAnevwGAjjmGz"
    assert res_decoded == message



def test_not_duplicate_in_row():
    row = vc.generate_row()
    assert len(row) == len(set(row)), f"Row contains duplicates: {row}"



def test_not_duplicate_in_table_indexes():
    row = vc.generate_row()

    table = vc.generate_table(row, "key")

    assert len(table.index.to_list()) == len(row), f"Table indexes contain duplicates: {table.index.to_list()}"