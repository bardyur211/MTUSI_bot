import pandas as pd
import os
import pathlib
import sys
import glob
import xlrd


#for search_file in script_path.glob('*.xls'):
#    print(search_file)

class SearchFile:
    def __init__(self):
        self.path = pathlib.Path(sys.argv[0]).parent
        self.xls_files = []
        self.search_files()

    def search_files(self):
        for search_file in self.path.glob('*.xls'):
            self.xls_files.append(search_file)

    def __str__(self):
        return '\n'.join(str(file) for file in self.xls_files)


path_to_file = SearchFile()

file = pd.read_excel(path_to_file.xls_files[0], sheet_name=0, header=15)
for i in file:
    print(i.replace('NaN', ' '))
