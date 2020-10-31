import os
import shutil

directory = "D:\CAT 2020\ElitesGrid\LRDI\hgvyv\Logical Reasoning and Data Interpretation for CAT - Series 2"
directory2 = "D:\CAT 2020\ElitesGrid\LRDI\hgvyv\The jpgs"
files_in_directory = os.listdir(directory)
filtered_files = [file for file in files_in_directory if file.endswith(".jpg")]

print("original list of jpg files:", filtered_files)
for file in filtered_files:
    path_to_file = os.path.join(directory, file)
    shutil.copy(path_to_file, directory2)
    os.remove(path_to_file)

# filtered_files = [file for file in files_in_directory if file.endswith(".jpg")]
