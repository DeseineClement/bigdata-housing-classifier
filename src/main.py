from system_io import input, output
from classifier import dataset


def main():
    try:
        dataset_file, dataset_columns, dataset_visus, dataset_range = input.arguments()
    except RuntimeError as err:
        output.error(err)
        return
    data = dataset.from_csv(dataset_file)
    dataset.analyse(data[dataset_range[0]:dataset_range[1]], dataset_columns, dataset_visus)


if __name__ == "__main__":
    main()
