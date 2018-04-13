############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    # flavor = "yum"

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""
        self.pairings = []
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name
#initializing all the attributes above.


    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)
#Adding to the list defined as pairings.


    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code
#rebinding the new value of code to the attribute code for self.


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = [] #Create an empty list to append to

    muskmelon = MelonType('musk', 1998, 'green', True, True, 'Muskmelon')  # Create MelonType instance of muskmelon
    muskmelon.add_pairing('mint')  #Add pairing to muskmelon
    all_melon_types.append(muskmelon)  #Add instance to list

    casaba = MelonType('cas', 2003, 'orange', False, False, 'Casaba')  # Create MelonType instance of casaba
    casaba.add_pairing('stawberry')  # Add pairing
    casaba.add_pairing('mint')  #Add pairing
    all_melon_types.append(casaba)  # Add instance to list

    crenshaw = MelonType('cren', 1996, 'green', False, False, 'Crenshaw')  # Create MelonType instance of crenshaw
    crenshaw.add_pairing('proscuitto')  # Add pairing
    all_melon_types.append(crenshaw)  # Add instance to list

    y_watermelon = MelonType('yw', 2013, 'yellow', False, True, 'Yellow Watermelon')  # Create MelonType instance of y_watermelon
    y_watermelon.add_pairing('ice cream')  # Add pairing
    all_melon_types.append(y_watermelon)  # Add instance to list

    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""
    for melon in melon_types:  #loop through each instance in the list
        print "{} pairs with ".format(melon.name)  # print name attribute of instance
        for pairing in melon.pairings:  # loop through each element in list of pairings
            print "- {}".format(pairing)  # print pairing


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_codes = {}  #create an empty dictionary

    for melon in melon_types: #loop through each instance in the list
        melon_codes[melon.code] = melon  # create dictionary key/value pair

    return melon_codes #return dictionary of instances

melon_types = make_melon_types()
melon_types_lookup = make_melon_type_lookup(melon_types)

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    def __init__(self, melon_type, shape_rating, color_rating, harvest_field, harvested_by, 
                 name):
        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.harvest_field = harvest_field
        self.harvested_by = harvested_by
    
    def IsSellable(self):
        return self.shape_rating > 5 and self.color_rating > 5 and self.harvest_field != 3

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    melons = []
    melons.append(Melon(melon_types['yw'], 8, 7, 2, 'Sheila', 'Melon 1'))
    melons.append(Melon(melon_types['yw'], 3, 4, 2, 'Sheila', 'Melon 2'))
    melons.append(Melon(melon_types['yw'], 9, 8, 3, 'Sheila', 'Melon 3'))
    melons.append(Melon(melon_types['cas'], 10, 6, 35, 'Sheila', 'Melon 4'))
    melons.append(Melon(melon_types['cren'], 8, 9, 35, 'Michael', 'Melon 5'))
    melons.append(Melon(melon_types['cren'], 8, 2, 35, 'Michael', 'Melon 6'))
    melons.append(Melon(melon_types['cren'], 2, 3, 4, 'Michael', 'Melon 7'))
    melons.append(Melon(melon_types['musk'], 6, 7, 4, 'Michael', 'Melon 8'))
    melons.append(Melon(melon_types['yw'], 7, 10, 3, 'Sheila', 'Melon 9'))

    return melons
    

    # look in make_melon_type_looup() dictionary for instance of MelonType




def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # for melon in melons:  #loop through each instance in the list
        
    #     print "{} pairs with ".format(melon.name)  # print name attribute of instance

melons = make_melons(melon_types_lookup)

