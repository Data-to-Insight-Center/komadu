from mpi4py import MPI
import adios2
from komadu_client.util.constants import TAU_EXTRACT_STRING
from komadu_client.util.util import get_attributes


def parse_tau_file(file):
    """
    Parses the tau file in the current location and returns a set of attributes.
    :param file:
    :return:
    """
    attributes = {}
    tau_string_attrs = TAU_EXTRACT_STRING.split(",")
    tau_string_attrs = map(str.strip, tau_string_attrs)

    with adios2.open(file, "r", MPI.COMM_SELF) as tauf:
        for fstep in tauf:
            for key in tau_string_attrs:
                # removing the "Metadata" from the key name
                refactored_key = key if "MetaData" not in key else key.split(':')[-1].lower()
                refactored_key = refactored_key.replace(' ', '_')
                attributes[refactored_key] = fstep.read_attribute_string(key)[0]
            # inspect variables in current step
            step_vars = fstep.available_variables()

            # # print variables information
            # for name, info in step_vars.items():
            #     print("variable_name: " + name)
            #     for key, value in info.items():
            #         print("\t" + key + ": " + value)
            #     print("\n")
            #
            # # print(fstep.read("comm_rank_count"))
            #print(fstep.read_attribute_string("MetaData:0:0:Hostname"))
    return get_attributes(attributes)
