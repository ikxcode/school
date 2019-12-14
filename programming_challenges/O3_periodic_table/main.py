from element import Element
import json

elements = [
    Element("hydrogen", "H", -1, "hydrogen", 1),
    Element("helium", "He", 0, "noble gases", 4),
    Element("lithium", "Li", 1, "alkali metals", 7),
    Element("sodium", "Na", 11, "alkali metals", 23),
    Element("neon", "Ne", 10, "noble gases", 20),
    Element("potassium", "K", 19, "alkali metals", 39)
]

name = input("What is the name of the element? ")

for e in elements:
    if name == e.name:
        print(e.group_number, e.atomic_weight, e.group_name, e.symbol)

symbol = input("What is the symbol of the element? ")

for e in elements:
    if symbol == e.symbol:
        print(e.group_number, e.atomic_weight, e.group_name, e.name)

group = input("What is the group name of the element? ")

for e in elements:
    if group == e.group_name:
        print(e.group_number, e.atomic_weight, e.symbol, e.name)
