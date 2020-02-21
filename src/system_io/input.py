from sys import argv
from getopt import getopt
from os import R_OK, access
from string import Template

DEFAULT_DATASET_FILE_PATH = "dataset/data.csv"
DEFAULT_DATASET_COLUMNS = ['housing_type', 'latitude', 'longitude', 'country_code', 'surface (m2)', 'height (m)',
                           'city']


def arguments():
    options, *_ = getopt(argv[1:], 'dc', ['dataset-file=', 'columns='])
    dataset_file = DEFAULT_DATASET_FILE_PATH
    dataset_columns = DEFAULT_DATASET_COLUMNS
    for opt, arg in options:
        if opt in ('-d', '--dataset-file'):
            dataset_file = arg
        elif opt in ('-c', '--columns'):
            dataset_columns = arg.split(',')

    if not access(dataset_file, R_OK):
        raise RuntimeError(Template("the file $file does not exists or is not readable.").substitute(file=dataset_file))

    for column in dataset_columns:
        if column not in DEFAULT_DATASET_COLUMNS:
            raise RuntimeError(Template("Invalid column $column must be one of $columns.").
                               substitute(column=column, columns=','.join(DEFAULT_DATASET_COLUMNS)))

    return dataset_file, dataset_columns
