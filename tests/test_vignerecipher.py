from periodic_encryption import vigenerecipher as vc

def test_unknown_not_in_row():
    row = vc.generateRow()
    assert row.find("�") == -1, f"Character '�' should not be in the row."


def test_generate_table():

    key = "1234"
    row = "abcdefghijklmnopqrstuvwxyz"+key
    first_row = key+"abcdefghijklmnopqrstuvwxyz"
    second_row = first_row[1:] + first_row[:1]

    table = vc.generateTable(row, key)

    assert table[first_row[0]].to_list() == list(first_row), f"Expected first row to start with encodingKey ({key}), but got {table[0]}"
    assert table[first_row[1]].to_list() == list(second_row), f"Expected {second_row} to be offsetted by 1, but got {table[1]}"



def test_vigenere_encode_decode():
    
    row = "abcdefghijklmnopqrstuvwxyz"
    key = "kryptos"
    message = "secretmessage"
    keystream = "hidden"

    res_encoded = vc.encode(row, key, keystream, message)
    print(res_encoded)
    assert res_encoded == "qknevwskjjmsz"
    assert vc.decode(row, key, keystream, res_encoded) == message



def test_not_duplicate_in_row():
    row = vc.generateRow()
    assert len(row) == len(set(row)), f"Row contains duplicates: {row}"



def test_not_duplicate_in_table_indexes():
    row = vc.generateRow()

    table = vc.generateTable(row, "key")

    assert len(table.index.to_list()) == len(row), f"Table indexes contain duplicates: {table.index.to_list()}"