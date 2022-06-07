import os
import re
import random
import pandas as pd
import numpy as np
import math

# path to 'Images' subdirectory, in directory resulting from unzipping
# CB Database zip file
IMG_DIR = 'PATH/TO/CBD/IMAGES/DIRECTORY'
# path to 'CBDatabase_Size_Eccentricity_RT.xlsx' file, also from CB Database
# zip file
CBD_SPECIFICATIONS_XLSX_PATH = 'PATH/TO/CBD/SPECS/CBDatabase_Size_Eccentricity_RT.xlsx'

# get the file names 
os.chdir(IMG_DIR)
file_names = os.listdir() 

# get a set containing all the image file numbers, FOR NON-MIRROR/-WINDOW STIMULI ONLY
# (the mirror/window stimuli are special and it's not entirely clear how selection
# from them should be done)
all_nos = set(range(1, 85)) 

# get a set of randomly picked image file numbers, that will be used for selecting 
# images with the change on the left side
left_nos = set(random.sample(all_nos, 24)) 

# get a set of randomly picked image file numbers, that will be used for selecting the
# images with the change on the right side (making sure not to use any of the numbers already 
# reserved for images with changes on the left side)
right_nos = set(random.sample(all_nos - left_nos, 24))  

# converting to str, and adding a 0 at the start of each number, 
# since that's used in the file names 
left_nos = ["0" + str(no) for no in left_nos]
right_nos = ["0" + str(no) for no in right_nos]

# create regex that will match all file names for images with changes on the left side
left_regex = "^(" + "|".join(left_nos) + ")_L"
right_regex = "^(" + "|".join(right_nos) + ")_R"

# filter using the above regexes
left_file_names = list(filter(lambda file_name: re.search(left_regex, file_name), file_names))
right_file_names = list(filter(lambda file_name: re.search(right_regex, file_name), file_names))

# separate the file names for images with the target present/absent
left_present_file_names = list(filter(lambda file_name: re.search("present", file_name), left_file_names))
left_absent_file_names = list(filter(lambda file_name: re.search("absent", file_name), left_file_names))

right_present_file_names = list(filter(lambda file_name: re.search("present", file_name), right_file_names))
right_absent_file_names = list(filter(lambda file_name: re.search("absent", file_name), right_file_names))

# now that we're certain that there are 24 left/right images each, we can merge the lists
present_file_names = left_present_file_names + right_present_file_names
absent_file_names = left_absent_file_names + right_absent_file_names

# make sure that the file name lists are sorted in the same way
for file_name_ls in (present_file_names, absent_file_names):
    file_name_ls.sort()

file_name_dict = {
    "target_present": present_file_names,
    "target_absent": absent_file_names
}

# create a pandas data frame (for exporting to .csv)
img_path_df = pd.DataFrame(file_name_dict)

# get data about target location and size
size_loc_df = pd.read_excel("", dtype=str)

# add columns and fill with empty values, for target radius and location (location in number of pixels from centre)
img_path_df['target_radius_px'] = np.nan
img_path_df['target_xcoord_px'] = np.nan
img_path_df['target_ycoord_px'] = np.nan

for row_no in range(len(img_path_df)):
    left_or_right = re.search("(R|L)", img_path_df['target_present'][row_no])[0]
    img_no = re.search("0(\d+)_", img_path_df['target_present'][row_no])[1]
    # convert from area to radius (have to convert object types here)
    img_path_df['target_radius_px'][row_no] = (float(size_loc_df['Pixel area'][int(img_no)]) / math.pi) ** (1/2)
    # selecting columns for x/ycoords in the size_loc_df based on if it's an image 
    # with the change on the left or the right hand side (because these data are in
    # different columns)
    if left_or_right == 'L':
        xcol = 7
        ycol = 8
    elif left_or_right == 'R':
        xcol = 9
        ycol = 10
    # need to shift the xcoords/ycoords by width/2 and height/2, respectively, to centre them
    img_path_df['target_xcoord_px'][row_no] = (float(size_loc_df.iloc[int(img_no), xcol]) - 1024/2)
    img_path_df['target_ycoord_px'][row_no] = -(float(size_loc_df.iloc[int(img_no), ycol]) - 768/2)


img_path_df.to_csv('change_blindness_flicker_stimuli_data.csv', index=False)
