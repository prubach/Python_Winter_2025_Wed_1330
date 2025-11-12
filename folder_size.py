# compute the size occupied by a given folder including the content
# - do not use os.walk
import os

my_folder = 'data'

def compute_folder_size(my_folder):
    folder_size = 0
    os.listdir(my_folder) # list of files and folders in a given folder
    os.path.getsize(my_folder) # get the size
    os.path.isdir(my_folder) # if is folder
    os.path.isfile(my_folder) # if is a regular file
    #TODO
    return folder_size