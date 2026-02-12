#!/usr/bin/python3
"""
    Serialize and deserialize from XML
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    serialize_to_xml write XML in specify file
    algo :
    1 - create root element
    2 - add each element from dict as a child of root
    3 - save XML file

    Args:
        dictionary (dict): data
        filename (string): filename
    """
    root_element = ET.Element("data")

    for key, value, in dictionary.items():
        child = ET.SubElement(root_element, key)
        child.text = str(value)

    tree = ET.ElementTree(root_element)
    try:
        with open(filename, "wb") as xml_file:
            tree.write(xml_file, encoding="utf-8", xml_declaration=False)
    except IOError:
        return None


def deserialize_from_xml(filename):
    """
    deserialize_from_xml

    Args:
        filename (str): XML file to read

    Returns:
        dict: the deserialized dictionnary
    """

    try:
        tree = ET.parse(filename)  # catch the tree
        root = tree.getroot()  # catch the root

        my_dict = {}

        for child in root:
            my_dict[child.tag] = child.text

        return my_dict

    except (FileNotFoundError, ET.ParseError):
        return None
