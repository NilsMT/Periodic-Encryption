import periodictable as pt

##############################################
# CUSTOM ELEMENT TO HANDLE CODES OUT OF RANGE
##############################################

class CounterElement(pt.core.Element):
    """
    A custom element class to handle elements with codes out of the periodic table range.\n
    It store in the mass: `900 + loop counter` how many time we looped out of range over the periodic table to finaly fit the ASCII code in the table.\n
    The name store the element that we finally are able to fit into as last part this element name.\n
    """
    def __init__(self, cnt: int, el: pt.core.Element):        
        # Initialize the parent class
        super().__init__(
            name=f"Counterium-{cnt}-{el.name}",
            symbol=f"Lc{el.symbol}{cnt}",
            Z=900 + cnt,
            ions=(),
            table="public"
        )
        
        self._mass = 900 + cnt

    @property
    def mass(self):
        return self._mass

    @mass.setter
    def mass(self, value):
        self._mass = value

##############################################
# GET ELEMENTS
##############################################

def get_el_by_number(number: int) -> pt.core.Element:
    """
    Return the element by its number
    """
    return pt.elements[number]



def get_last_el() -> pt.core.Element:
    """
    Return the last element of the periodic table
    """
    bst = 0
    for e in pt.elements:
        if e.number > bst:
            bst = e.number
    return get_el_by_number(bst)

def get_el_by_name(name: str) -> pt.core.Element:
    """
    Return the element by its name
    """
    return pt.elements.name(name)

def get_el_by_symbol(symbol: str) -> pt.core.Element:
    """
    Return the element by its symbol
    """
    return pt.elements.symbol(symbol)

##############################################
# TEXT ----> ELEMENTS
##############################################

def turn_chr_into_el(character: chr) -> pt.core.Element:
    """
    Convert a character into an element
    """
    el = None
    last = get_last_el().number

    code = ord(character)

    #gotta truncate or it won't fit periodic table
    if code > last:
        quot = code // last
        truncated_code = code % last

        return CounterElement(
            quot,
            get_el_by_number(truncated_code)
        )

    else:
        return get_el_by_number(code)



def turn_str_into_el(string: str) -> list[pt.core.Element]:
    """
    Convert a string into a list of elements
    """
    lst: list[pt.core.Element] = []
    for c in string:
        lst.append(turn_chr_into_el(c))
    return lst

##############################################
# ELEMENTS ----> TEXT
##############################################

def turn_el_into_chr(element: pt.core.Element) -> chr:
    """
    Convert an element into a character
    """
    if (element.number < 900):
        #its a normal element
        return chr(element.number)
    else:
        #its a loop counter element
        loop_count = element.number - 900
        el_name = element.name.split("-")[-1]

        excess = loop_count * get_last_el().number

        return chr(excess + get_el_by_name(el_name).number)



def turn_el_into_str(element_list: list[pt.core.Element]) -> str:
    """
    Convert a list of elements into a string
    """
    string = ""
    for e in element_list:
        string += turn_el_into_chr(e)
    return string