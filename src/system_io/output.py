from string import Template
from sys import argv


def helper():
    print(Template("python $entry_point --dataset-file={dataset-file} --columns={column1},{column2},...").
          substitute(entry_point=argv[0]))
    print("  --dataset-file\t--d\t| the path to the dataset file")
    print("  --columns\t\t--c\t| the list of columns to be analysed separated by comas")


def error(message):
    print(message)
    helper()
