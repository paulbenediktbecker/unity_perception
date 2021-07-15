from PIL import Image, ImageDraw, ImageFont
import os
import numpy as np
import cv2
import argparse
import csv
import matplotlib.pyplot as plt



if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Convert Ouput of Unity to .csv File for Tensorflow')
    parser.add_argument('-dir', '--imagedir', type=str, required=True, help='Path to Folder with images')
    parser.add_argument('-csv', '--csv', type=str, required=True, help='Path to Anno csv.')
    args = parser.parse_args()

    dir = args.imagedir
    csv_path = args.csv
    print("HIIER")
    print(dir, csv_path)


    with open(csv_path, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')


        for filename in os.listdir(dir):
            img = cv2.imread(os.path.join(dir, filename), 1)
            for row in spamreader:
                if(str(row[0]) == str(filename)):
                    xmin = int(row[4])
                    ymin = int(row[5])
                    xmax = int(row[6])
                    ymax = int(row[7])


                    img = cv2.rectangle(img, (xmin, ymin), (xmax, ymax), (0, 255, 0), 6)
                    img= cv2.putText(img, row[3], (xmin, ymax+20), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 0), 1)
            cv2.imwrite(os.path.join(dir,"anno_" + str(filename) ),img)
