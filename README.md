# bigdata-housing-classifier

## Setup

Both rules can be called using <code>make</code>

#### Build virtual environments

    make virtualenv

#### Generate dataset

    make dataset


## Visualize dataset

    ./classifier-venv/bin/python3 src/main.py

Arguments are:

    --d | ----dataset-file {path_to_dataset} // Default is: dataset/data.csv\n
    --c | --columns {column1}, {column2}, ...
    --v | --visus {visu1}, {visu2} // Default is: scatter_plot, histogram
    --r | --range {index1}, {index2} // Defauls is: 0, 1000
