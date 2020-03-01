from sys import argv
from getopt import getopt
from os import R_OK, access
from string import Template

DEFAULT_DATASET_FILE_PATH = "dataset/data.csv"
DEFAULT_DATASET_COLUMNS = ['surface (m2)', 'height (m)', 'latitude', 'housing_type', 'longitude', 'country_code',
                           'city']
DEFAULT_VISU = ["scatter_plot", "histogram"]
DEFAULT_RANGE = [0, 1000]

def arguments():
    options, *_ = getopt(argv[1:], 'dc', ['dataset-file=', 'columns=', 'visus=', 'range='])
    dataset_file = DEFAULT_DATASET_FILE_PATH
    dataset_columns = DEFAULT_DATASET_COLUMNS
    dataset_visus = DEFAULT_VISU
    dataset_range = DEFAULT_RANGE
    for opt, arg in options:
        if opt in ('-d', '--dataset-file'):
            dataset_file = arg
        elif opt in ('-c', '--columns'):
            dataset_columns = arg.split(',')
        elif opt in ('-v', '--visus'):
            dataset_visus = arg.split(',')
        elif opt in ('-r', '--range'):
            dataset_range = arg.split(',')

    dataset_range = list(map(lambda x: int(x), dataset_range))
    if len(dataset_range) == 1 :
        dataset_range.append(DEFAULT_RANGE[1])

    if not access(dataset_file, R_OK):
        raise RuntimeError(Template("the file $file does not exists or is not readable.").substitute(file=dataset_file))

    for column in dataset_columns:
        if column not in DEFAULT_DATASET_COLUMNS:
            raise RuntimeError(Template("Invalid column $column must be one of $columns.").
                               substitute(column=column, columns=','.join(DEFAULT_DATASET_COLUMNS)))

    for visu in dataset_visus:
        if visu not in DEFAULT_VISU:
            raise RuntimeError(Template("Invalid visu $column must be one of $columns.").
                               substitute(column=visu, columns=','.join(DEFAULT_VISU)))

    for range_num in dataset_range:
        if range_num not in range(0, 1001):
            raise RuntimeError(Template("Invalid range $column must be between 0 and 999.").
                               substitute(column=range_num))

    return dataset_file, dataset_columns, dataset_visus, dataset_range
