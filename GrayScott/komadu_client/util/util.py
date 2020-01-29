import os
from komadu_client.models.ingest_models import attributesType, attributeType
from komadu_client.util.constants import GRAYSCOTT_WORKFLOW, BRUSSELATOR_WORKFLOW_NAME, GRAYSCOTT_WORKFLOW_VERSION,\
    BRUSSELATOR_WORKFLOW_VERSION, WORKFLOW_VERSION_DEFAULT
import json


def get_experiment_info(file_path):
    """
    Returns the extracted campaign info based on the filepath
    :param file_path: path of the individual fobs.json file
    :return:
    """
    dirname = os.path.dirname(file_path)
    dirs = dirname.split(os.sep)

    # extracting meta data from the directory structure
    campaign_name = dirs[-4]
    # todo: change this
    codesign_name = campaign_name
    username = dirs[-3]
    sweepGroup = dirs[-2]
    sweep = dirs[-1]

    run_name = dirs[-1]
    if run_name.startswith("run"):
        experiment_name = username + "-" +codesign_name + "-" + campaign_name + "-" + dirs[-2] + "-" + run_name
    else:
        experiment_name = run_name

    return experiment_name, codesign_name, campaign_name, username, sweepGroup, sweep


def get_cascaded_id(ids):
    """
    Creating the cascaded ids from a given list
    ex: get_cascaded_id([user, camp23]) would return user-camp23
    :param ids:
    :return:
    """
    for i in range(len(ids) - 1):
        cascaded_id = ids[i] + "-"
    return cascaded_id + ids[len(ids) - 1]


def get_attributes(dict_values):
    attributes = attributesType()
    for key in dict_values:
        attribute = attributeType()
        attribute.property_ = key
        attribute.value_ = (str(dict_values[key]))
        attributes.append(attribute)
    return attributes


def get_workflow_name(filename):
    if GRAYSCOTT_WORKFLOW in filename:
        return GRAYSCOTT_WORKFLOW
    elif BRUSSELATOR_WORKFLOW_NAME in filename:
        return BRUSSELATOR_WORKFLOW_NAME
    else:
        return None


def get_workflow_version(workflow_name):
    if workflow_name == GRAYSCOTT_WORKFLOW:
        return GRAYSCOTT_WORKFLOW_VERSION
    elif workflow_name == BRUSSELATOR_WORKFLOW_NAME:
        return BRUSSELATOR_WORKFLOW_VERSION
    else:
        return WORKFLOW_VERSION_DEFAULT


def get_node_id(workflow_id, node_id):
    return workflow_id + "-" + node_id


def parse_json_file(file):
    with open(file) as f:
        data = json.load(f)
    return data


def flatten_dict(data, prefix=""):
    fmap = {}
    for key in data:
        if isinstance(data[key], dict):
            values = flatten_dict(data[key], key + "_")
            fmap.update(values)
        else:
            fmap[prefix + key] = data[key]
    return fmap
