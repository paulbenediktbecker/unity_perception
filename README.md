## unity_perception
scripts and ressources for project thesis on generating synthetic image data in a logistics environment.


# Show_Annotations.py
Script to display annotations.
Arguments:
  -dir/--imagedir : Path to Folder with images
  -csv/--csv : Path to CSV containing annotation in TF format
  
 # UnityAnnotations_toCSV
Script for converting the Annotations .json of [Unity Perception](https://github.com/Unity-Technologies/com.unity.perception) to a .csv that can be used with Tensorflow. The output looks like this: 

filename,width,height,class,xmin,ymin,xmax,ymax
rgb_13.png,101,128,SLC,792,0,893,128
rgb_13.png,253,159,Pallet,15,0,268,159
rgb_13.png,130,123,SLC,380,65,510,188
rgb_13.png,147,125,SLC,625,329,772,454
rgb_13.png,225,222,Pallet,140,315,365,537
rgb_13.png,151,154,SLC,931,489,1082,643
  
# Spread_Images.py
Script to split images of one Folder into two folders in a special proportion.

#Spread_CSV.py
Script for creating a new .csv for all images in a folder.
Use case: after using Spread_Images.py, the images are split up into two folder, e.g. a "train" and "test" folder. 
The corresponding .csv file is not split up yet. The script takes all rows of the entries in the given folder and creates a new .csv with these. 
Arguments:
  -in/--input : Path to .csv input file (incl ".csv")
  -dir/--directory : Path to folder of images
  -name/--filename : name of output CSV (incl. ".csv")
  


