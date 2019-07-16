#!/usr/bin/env python
"""
Input file parser which parses the inputs required and creates the attributes list for Komadu.
ex:
settings.json -> Komadu attributes
"""
import json
from komadu_client.models.ingest_models import attributeType, attributesType
from komadu_client.util.constants import GRAYSCOTT_WORKFLOW_NAME

class InputParser:

    def parse(self, file, file_type):
        """
        Parses a given input file and returns attributes
        :param file: input file
        :param file_type: name of the input file (ex: grayscott)
        :return: list of attributeType
        """
        if file_type.lower() == GRAYSCOTT_WORKFLOW_NAME:
            return self.gray_scott_input_parser(file)
        else:
            return None

    def gray_scott_input_parser(self, input_file):
        """
        Parses the gray scott input json file into Komadu attributes
        :param input_file: settings.json file
        :return: list of attributeType
        """
        with open(input_file) as in_file:
            input_content = json.load(in_file)

        attributes = attributesType()
        for key in input_content:
            attribute = attributeType()
            attribute.property_ = key
            attribute.value_ = (str(input_content[key]))
            attributes.append(attribute)

        # adding the location
        attribute = attributeType()
        attribute.property_ = "location"
        attribute.value_ = str(input_file)
        attributes.append(attribute)

        return attributes
