import json
from komadu_client.util.util import get_experiment_name, get_workflow_name, get_attributes
from komadu_client.util.constants import GRAYSCOTT_WORKFLOW_VERSION
from komadu_client.models.model_creator import create_workflow_activity
from datetime import datetime


def parse_fobs_json(filename):
    """
    This function passes the fobs.json file and creates the workflow in Komadu.
    :param filename:
    :return:
    """
    with open(filename) as file:
        fobs = json.load(file)

    experiment_name = get_experiment_name(filename)
    machine = fobs["machine_name"]
    workflow_name = get_workflow_name(filename)
    runs = fobs["runs"]
    workflow_node_ids = range(len(runs))

    for i in workflow_node_ids:
        if runs[i]["name"] == "simulation":
            simulation_index = i
            other_node_ids = workflow_node_ids - i
            break

    simulation = runs[simulation_index]
    workflow_attributes = {
        "node_layout": flatten_node_layout(fobs["node_layout"]),
        "nprocs": simulation["nprocs"],
        "total_nodes": fobs["total_nodes"],
        "launch_mode": fobs["launch_mode"]
    }
    simulation_name = simulation["name"]
    sumulation_node = create_workflow_activity(experiment_name, experiment_name + "-" + simulation_name,
                                               experiment_name + "-" + simulation_name,
                                               workflow_name, GRAYSCOTT_WORKFLOW_VERSION, datetime.now(),
                                               machine, attributes=get_attributes(workflow_attributes))

    return sumulation_node


def flatten_node_layout(node_layout):
    final_map = {}
    for i in node_layout:
        final_map.update(i)
    ', '.join("{!s}={!r}".format(key, val) for (key, val) in final_map.items())
