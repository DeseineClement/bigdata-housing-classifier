import os
from typing import List
from pandas import read_csv, DataFrame, value_counts, Series
import matplotlib.pyplot as plt

from system_io.input import DEFAULT_DATASET_COLUMNS

RESULT_DIR = "visu-result"
BUILDINGS_NUM_COL = "Number of buildings"
HISTO_FILE_NAME_PART = "_histo.png"
PLOT_FILE_NAME = "scatter-plot.png"

def from_csv(dataset_file_path: str):
    return read_csv(dataset_file_path)

def analyse(dataset: DataFrame, columns: List[str], visus: List[str]):
    print(dataset)
    if not os.path.exists(RESULT_DIR):
        os.mkdir(RESULT_DIR)
    if "histogram" in visus:
        histogram(dataset, columns)
    if "scatter_plot" in visus:
        scatter_plot(dataset, columns)

def histogram(dataset: DataFrame, columns: List[str]):
    # create histogram for each column selected
    for i in range(0, len(columns)):
        # test if column is of type string or int
        if dataset.dtypes[columns[i]] == "object":
            # create histogram for string column and compare number of buildings for each value
            witness_column = None
            if (i - 1) < 0:
                witness_column =  DEFAULT_DATASET_COLUMNS[i + 1]
            else:
                witness_column = DEFAULT_DATASET_COLUMNS[i - 1]
            final_dataset = dataset.groupby(columns[i])[[witness_column]].count()
            final_dataset.sort_values(witness_column).reset_index()
            final_dataset.columns = [BUILDINGS_NUM_COL]
            final_dataset = final_dataset.sort_values(by=BUILDINGS_NUM_COL, ascending=False)
            if len(final_dataset.index) > 20:
                final_dataset = final_dataset.head(20)
            print(final_dataset)
            hist = final_dataset.plot(y=BUILDINGS_NUM_COL, kind="bar", figsize=(15, 15))
            hist.get_figure().savefig(os.path.join(RESULT_DIR, columns[i] + HISTO_FILE_NAME_PART))
        else:
            # create histogram for int column and compare number of buildings
            print(dataset[columns[i]])
            dataset.hist(column=columns[i])
            plt.savefig(os.path.join(RESULT_DIR, columns[i] + HISTO_FILE_NAME_PART))

def scatter_plot(dataset: DataFrame, columns: List[str]):
    if len(columns) < 2:
        print("Need minimum 2 columns to create scatter plot")
        return
    scatter = None
    if len(columns) >= 3 and dataset.dtypes[columns[2]] != "object":
       scatter = dataset.plot.scatter(x=columns[0], y=columns[1], c=columns[2], colormap='viridis')
    else:
        scatter = dataset.plot.scatter(x=columns[0], y=columns[1])
    figure = scatter.get_figure()
    figure.savefig(os.path.join(RESULT_DIR, PLOT_FILE_NAME))
