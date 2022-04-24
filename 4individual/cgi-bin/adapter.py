from typing import Dict, List
from lxml import etree


def dict_to_xml(input_dict: Dict) -> etree.ElementBase:
    el = etree.Element("element")
    for key in input_dict.keys():
        attr = etree.Element("attr")
        attr.set("key", key)
        attr.set("value", str(input_dict[key]))
        el.append(attr)
    return el


def xml_to_dict(el: etree.ElementBase) -> Dict:
    output_dict = {}
    for child in el:
        key = child.get("key")
        value = child.get("value")
        output_dict[key] = value
    return output_dict


def export_to_file(dict_list: List, path: str):
    root = etree.Element("items")
    for item in dict_list:
        root.append(dict_to_xml(item))
    with open(path, "w+") as file:
        file.write(etree.tostring(root, pretty_print=True).decode("utf-8"))


def import_from_file(path: str) -> List:
    dict_list = []
    with open(path, "r") as file:
        text = file.read().encode("utf-8")
    items = etree.XML(text)
    for item in items:
        dict_list.append(xml_to_dict(item))
    return dict_list
