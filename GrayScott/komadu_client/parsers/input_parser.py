#!/usr/bin/env python
"""
Input file parser which parses the inputs required and creates the attributes list for Komadu.
ex:
settings.json -> Komadu attributes
"""
import json
from komadu_client.models.ingest_models import attributeType, attributesType


class InputParser:

    def parse(self, file, file_type):
        """
        Parses a given input file and returns attributes
        :param file: input file
        :param file_type: name of the input file (ex: grayscott)
        :return: list of attributeType
        """
        if file_type.lower() == "grayscott":
            return self.gray_scott_input_parser(file)
        elif file_type.lower() == "adiosConfig":
            return self.adios_config_parser(file)
        else:
            return None

    def gray_scott_input_parser(self, input_file):
        """
        Parses the gray scott input json file into Komadu attributes
        :param input_file: settings.json file
        :return: list of attributeType
        """
        with open(input_file) as input_file:
            input_content = json.load(input_file)

        attributes = attributesType()
        for key in input_content:
            attribute = attributeType()
            attribute.property_ = key
            attribute.value_ = (str(input_content[key]))
            attributes.append(attribute)

        return attributes

    def adios_config_parser(self, input_file):
        # todo: implement this
        return None
