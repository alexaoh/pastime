#Prints out all filenames in your root path
import os

#Solution #1
def list_all_files_recursively(root):
    paths = os.listdir(root)
    for path_name in paths:
        if os.path.isfile(root+path_name):
            print(path_name)
        elif os.path.isdir(root+path_name):
            list_all_files(root+path_name+"/")

#Solution #2
def list_all_files(root):
    i = 0
    paths = [root + path_name for path_name in os.listdir(root)]
    while len(paths):
        if os.path.isfile(paths[0]):
            print(paths[0].split("/")[-1])
            paths.pop(0)
        elif os.path.isdir(paths[0]):
            new_paths = [paths[0] + "/" + path_name for path_name in os.listdir(paths[0] + "/")]
            paths += new_paths
            paths.pop(0)
