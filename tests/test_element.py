import pytest
import periodictable as pt

from periodicencryption import el

@pytest.mark.parametrize(
    "string",  # Test inputs and expected result
    [
        (""), # empty
        ("¤"), # loop
        ("test"), # normal
        ("¤test"), # loop + normal
    ]
)



def test_string_elements_conversion(string: str):
    element_list = el.turn_str_into_el(string)
    assert el.turn_el_into_str(element_list) == string, f"Expected {string}, but got {el.turn_el_into_str(element_list)}"



def test_is_loopcounter():
    element = el.turn_chr_into_el("¤")
    assert element.number >= 900
    assert isinstance(element, el.CounterElement), f"Expected type el.CounterElement, but got {type(element)}"



def test_is_not_loopcounter():
    element = el.turn_chr_into_el("a")
    assert element.number < 900
    assert isinstance(element, pt.core.Element), f"Expected type pt.core.Element, but got {type(element)}"

# Code by NilsMT on GitHub