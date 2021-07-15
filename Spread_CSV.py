from random import random
import os
import argparse
import csv
from PIL import Image
from shutil import copyfile

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Convert Ouput of Unity to .csv File for Tensorflow')
    parser.add_argument('-in', '--input', type=str, required=True,help='Path to .csv input file (incl ".csv")')
    parser.add_argument('-dir', '--directory', type=str, required=True, help='Path to folder of images')
    parser.add_argument('-name', '--filename', type=str, required=True, help='name of output CSV (incl. ".csv")')
    args = parser.parse_args()

    csv_path = args.input
    img_path = args.directory
    new_file = args.filename

    filenames = []

    for filename in os.listdir(img_path):
        filenames.append(str(filename))

    with open(csv_path, newline='') as csvfile:
        with open(new_file, 'w', newline='') as csv_file:  # open/create CSV

            spamreader = csv.reader(csvfile, delimiter=',')
            writer = csv.writer(csv_file)  # initiate CSV
            for index, row in enumerate(spamreader):
                if(index==0):
                    writer.writerow(row)
                if(row[0] in filenames):
                    writer.writerow(row)


