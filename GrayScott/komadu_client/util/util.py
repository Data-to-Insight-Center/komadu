import os


def get_experiment_name(file_path):
    dirname = os.path.dirname(file_path)
    dirs = dirname.split(os.sep)
    run_name = dirs[-1]
    if run_name.startswith("run"):
        experiment_name = dirs[-2] + "-" + run_name
    else:
        experiment_name = run_name

    return experiment_name
