import pytest
import periodictable as pt

from periodic_encryption import element as el
from periodic_encryption import encryption as en

@pytest.mark.parametrize(
    "string",  # Test inputs and expected result
    [
        (""), # empty
        ("╠"), # loop
        ("test"), # normal
        ("╠test"), # loop + normal
    ]
)



def test_string_elements_conversion(string: str):
    elementList = el.turnStringIntoElements(string)
    assert el.turnElementsIntoString(elementList) == string, f"Expected {string}, but got {el.turnElementsIntoString(elementList)}"



def test_is_loopcounter():
    element = el.turnCharacterIntoElement("╠")
    assert element.number >= 900
    assert isinstance(element, el.LoopCounterElement), f"Expected type el.LoopCounterElement, but got {type(element)}"



def test_is_not_loopcounter():
    element = el.turnCharacterIntoElement("a")
    assert element.number < 900
    assert isinstance(element, pt.core.Element), f"Expected type pt.core.Element, but got {type(element)}"