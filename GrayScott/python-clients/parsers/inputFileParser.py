#!/usr/bin/env python
"""
Input file parser which parses the inputs required and creates the attributes list for Komadu.
ex:
settings.json -> Komadu attributes
"""
import json
from xml.etree.ElementTree import Element, SubElement, tostring


def input_parser(file, file_type):
    """
    Parses a given input file and returns attributes
    :param file: input file
    :param file_type: name of the input file (ex: grayscott)
    :return: xml.etree element of <kom:attributes>
    """
    if file_type.lower() is "grayscott":
        return gray_scott_input_parser(file)
    elif file_type.lower() is "adiosConfig":
        return adios_config_parser(file)
    else:
        return None


def gray_scott_input_parser(input_file):
    """
    Parses the gray scott input json file into Komadu attributes
    :param input_file: settings.json file
    :return: xml.etree of attributes
    """
    with open(input_file) as input_file:
        input_content = json.load(input_file)

    attributes = Element('kom:attributes')

    for key in input_content:
        xml_attribute = SubElement(attributes, "kom:attribute")
        xml_property = SubElement(xml_attribute, "kom:property")
        xml_value = SubElement(xml_attribute, "kom:value")
        xml_property.text = key
        xml_value.text = str(input_content[key])

    return attributes


def adios_config_parser(input_file):
    # todo: implement this
    return None