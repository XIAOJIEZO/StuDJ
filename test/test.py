import os
from os import listdir
my_path = '/sale_data/153/20220817/18/out'
for file_name in listdir(my_path):

    if file_name.endswith('.ok'):
        print(file_name)
        os.remove(file_name)