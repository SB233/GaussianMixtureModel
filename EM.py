import csv
import argparse
from os import path

import numpy as np
import matplotlib.pyplot as plt


def main():
    parser = argparse.ArgumentParser(
        description='Implement EM algorithm for GMM.'
    )
    parser.add_argument(
        'training',
        help='file containing the training data'
    )
    parser.add_argument(
        'file',
        help='file containing the data to be classified'
    )
    parser.add_argument(
        '--dimension',
        help='number of dimentional feature',
        required=False,
        default=2
    )

    args = parser.parse_args()

    if not path.isfile(args.training) or not path.isfile(args.file):
        parser.error('Invalid file path')

    data, labels = read_file(args.training, args.dimension, True)
    dataStore = createDataStore(data, labels)
    printDataStore(dataStore)


def createDataStore(data, labels):
    dataStore = dict()
    for pos, val in enumerate(data):
        dataLabel = labels[pos]
        if(dataLabel in dataStore.keys()):
            dataStore[dataLabel].append(val)
        else:
            dataStore[dataLabel] = [val]
    for label in dataStore:
        dataStore[label] = np.array(dataStore[label])
    return dataStore


def read_file(filepath, dimension, withlabel=False):
    with open(filepath) as f:
        csv_reader = csv.reader(f, delimiter=' ', skipinitialspace=True)
        labels = []
        data = []
        for sample in csv_reader:
            features = [float(i) for i in sample[:dimension]]
            data.append(features)
            if withlabel:
                labels.append(sample[-1])
    return data, labels


def printDataStore(dataStore):
    colors = ['blue', 'green', 'magenta', 'cyan']
    for k in dataStore:
        values = dataStore[k]
        x = values[:, 0]
        y = values[:, 1]
        plt.scatter(x, y, color=colors[0])
        colors.pop(0)
    plt.show()


if __name__ == '__main__':
    main()