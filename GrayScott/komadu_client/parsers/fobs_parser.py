import json
from komadu_client.util.util import get_experiment_name, get_workflow_name, get_attributes, get_node_id, \
    get_workflow_version
from komadu_client.util.constants import GRAYSCOTT_WORKFLOW_VERSION
from komadu_client.models.model_creator import create_workflow_activity
from datetime import datetime
from komadu_client.models.ingest_models import activityActivityType, communicationType


def parse_fobs_json(filename):
    """
    This function passes the fobs.json file and creates the workflow in Komadu.
    :param filename:
    :return:
    """
    with open(filename) as file:
        fobs = json.load(file)

    experiment_id = get_experiment_name(filename)
    machine = fobs["machine_name"]
    workflow_name = get_workflow_name(filename)
    runs = fobs["runs"]
    workflow_node_ids = list(range(len(runs)))

    for i in workflow_node_ids:
        if runs[i]["name"] == "simulation":
            simulation_index = i
            workflow_node_ids.remove(i)
            break

    simulation = runs[simulation_index]
    workflow_attributes = {
        "node_layout": flatten_node_layout(fobs["node_layout"]),
        "nprocs": simulation["nprocs"],
        "total_nodes": fobs["total_nodes"],
        "launch_mode": fobs["launch_mode"]
    }
    simulation_name = simulation["name"]
    workflow_version = get_workflow_version(workflow_name)
    simulation_node = create_workflow_activity(experiment_id, get_node_id(experiment_id, simulation_name),
                                               get_node_id(experiment_id, simulation_name),
                                               workflow_name, workflow_version, datetime.now(),
                                               machine, attributes=get_attributes(workflow_attributes))
    # todo: support more than two nodes
    analysis = runs[workflow_node_ids[0]]
    analysis_name = analysis["name"]
    analysis_node = create_workflow_activity(experiment_id, get_node_id(experiment_id, analysis_name),
                                             get_node_id(experiment_id, analysis_name), workflow_name,
                                             workflow_version, datetime.now(), machine)

    return get_activity_activity_type(simulation_node, analysis_node)


def flatten_node_layout(node_layout):
    final_map = {}
    for i in node_layout:
        final_map.update(i)
    return ', '.join("{!s}={!r}".format(key, val) for (key, val) in final_map.items())


def get_activity_activity_type(node1, node2):
    model = activityActivityType()
    model.activity1 = node1
    model.activity2 = node2
    comm = communicationType()
    comm.informantActivityID = node1.serviceInformation.serviceID
    comm.informedActivityID = node2.serviceInformation.serviceID
    model.communication = comm
    return model
