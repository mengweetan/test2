
import os
from os import listdir
from os.path import isfile, join
import re

current_directory = os.getcwd()
path_list = [x[0] for x in os.walk(current_directory)]

def get_todos(path,onlyfiles):
    temp = []
    for file in onlyfiles:
        if file[-3:] == '.js':
            #print (file)
            with open(path+"/"+file) as f:
                txt = f.read()
                x = re.search("TODO", txt)
                if x:
                    print (path+"/"+file)
                    temp.append(path+"/"+file)
    return temp

def check_todos():
    todo_list = []
    for path in path_list:
        onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
        todo_list += get_todos(path,onlyfiles)

    return todo_list

check_todos()
