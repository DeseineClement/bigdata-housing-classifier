from system_io import input, output
from classifier import dataset


def main():
    try:
        dataset_file, dataset_columns = input.arguments()
    except RuntimeError as err:
        output.error(err)
        return
    data = dataset.from_csv(dataset_file)
    dataset.analyse(data, dataset_columns)


if __name__ == "__main__":
    main()
