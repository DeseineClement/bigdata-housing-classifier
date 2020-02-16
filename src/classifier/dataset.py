from pandas import read_csv


def from_csv(dataset_file_path):
    return read_csv(dataset_file_path)


def analyse(dataset, columns):
    print(dataset, columns)  # TODO analyse dataset here
