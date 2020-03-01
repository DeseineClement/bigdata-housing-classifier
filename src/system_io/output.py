from string import Template
from sys import argv


def helper():
    print(Template("python $entry_point --dataset-file={dataset-file} --columns={column1},{column2},... --visus={visu1},{visu2} --range={index0, index1}").
          substitute(entry_point=argv[0]))
    print("  --dataset-file\t--d\t| the path to the dataset file")
    print("  --columns\t\t--c\t| the list of columns to be analysed separated by comas")
    print("  --visus\t\t--v\t| the list of visus to be used separated by comas")
    print("  --range\t\t--r\t| the range in data to be considered for visualization")

def error(message):
    print(message)
    helper()
