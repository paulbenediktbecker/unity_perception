import json
import csv
import argparse
import os

if __name__ == "__main__":


    #ARGPARSER
    parser = argparse.ArgumentParser(description='Convert Ouput of Unity to .csv File for Tensorflow')
    parser.add_argument('-f', '--file', type=str, required=True, help='Path to Folder Json File (incl. ".json")')
    parser.add_argument('-out', '--output', type=str, required=True, help='name of output CSV (incl. ".csv")')
    args = parser.parse_args()
    with open(args.output, 'w', newline='') as csv_file:  # open/create CSV
        writer = csv.writer(csv_file)  # initiate CSV
        writer.writerow(["filename", "width", "height", "class", "xmin", "ymin", "xmax", "ymax"])  # write header to csv
        for filename in os.listdir(args.file):
            if(filename.endswith(".json")): # check if .jpg
                with open(os.path.join(args.file,filename)) as f: #open JSON

                    data = json.load(f) #load Data


                    captures = data["captures"]

                    for capture in captures: #iterate trough pictures
                        full_filename = capture["filename"]
                        filename = str(full_filename).split("/")[1] #get only filename
                        annos = capture["annotations"][0]["values"] #filter values
                        for entry in annos: #iterate trough all annotations of a single picture

                            #Values
                            x_val = int(entry["x"])
                            y_val = int(entry["y"])
                            width_val = int(entry["width"])
                            height_val = int(entry["height"])
                            class_val = entry["label_name"]
                            xmax_val = str(x_val + width_val)
                            ymax_val = str(y_val + height_val)

                            #write to CSV
                            toWrite = [filename,width_val ,height_val ,class_val ,x_val,y_val,xmax_val,ymax_val ]
                            writer.writerow(toWrite)

                        #print(json.dumps(annos, sort_keys=True, indent=4)) #DEBUG