from system_io import input, output


def main():
    try:
        dataset_file, dataset_columns = input.arguments()
    except RuntimeError as err:
        output.error(err)
        return
    print(dataset_file, dataset_columns)


if __name__ == "__main__":
    main()
