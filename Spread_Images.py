from random import random
import os
from PIL import Image
from shutil import copyfile

if __name__ == "__main__":
    print(random())

    inpath = input("Input Path: ")
    out1 = input("Train directory: ") # e.g. 80%
    out2 = input("Test directory: ") # e.g. 20%

    ratio = float(int(input("How much percent should be in Train ? insert int:"))) / 100

    for filename in os.listdir(inpath):
        if(filename.endswith(".png")): # check if .jpg

            src1 = os.path.join(inpath, filename)
            if random() <= ratio:
                out_dir = out1
            else:
                out_dir = out2
            dst1 = os.path.join(out_dir, filename)
            copyfile(src1, dst1) #jpg

