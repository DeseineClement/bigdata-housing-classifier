from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB
from sklearn import preprocessing

import pandas as pb
import numpy as np

import string
import math

def parse_training_file(path='../../dataset/data.csv', label_row='housing_type'):
    parsed_data = pb.read_csv(path)

    label_values = parsed_data.pop(label_row).values
    feature_names = parsed_data.keys()
    feature_values = parsed_data.values

    # This is a slight modification for the "NA" (Namibia) country code
    # it results in "NaN" value when reading the csv file, we therefore
    # replace it by its original value
    for row in feature_values:
        if not isinstance(row[3], str) and math.isnan(row[3]):
            row[3] = "NA"

    le = preprocessing.LabelEncoder()
    conv_label_values = le.fit_transform(label_values)

    ohe = preprocessing.OneHotEncoder()
    feature_values = ohe.fit_transform(feature_values).toarray()

    return conv_label_values, feature_names, feature_values


def main():
    label_values, feature_names, feature_values = parse_training_file()

    test_size = 0.33

    print_parameters(feature_names, feature_values, test_size)

    train_values, test_values, train_labels, test_labels = train_test_split(feature_values,
                                                                            label_values,
                                                                            test_size=test_size,
                                                                            random_state=42)

    gnb = GaussianNB()
    gnb.fit(train_values, train_labels)
    predictions = gnb.predict(test_values)

    label_counts = np.unique(test_labels, return_counts=True)
    pred_counts = np.unique(predictions, return_counts=True)

    print_output(label_counts, pred_counts, predictions, test_labels)


def print_parameters(feature_names, feature_values, test_size):
    print("\n-----------------------------------------------------------\nParameters:\n")
    print(">> Number of buildings: ", len(feature_values))
    print("\t| Used for testing\t\t: ", round(test_size * len(feature_values)))
    print("\t| Used for training\t: ", len(feature_values) - round(test_size * len(feature_values)), '\n')
    print(">> Features tested: ")
    for feature_name in feature_names:
        print("\t| ", feature_name)


def print_output(label_counts, pred_counts, predictions, test_labels):
    print("\n-----------------------------------------------------------\nResults:\n")
    print(">> the accuracy score is:", str(round(accuracy_score(test_labels, predictions) * 100, 2)) + '%\n')

if __name__ == "__main__":
    main()