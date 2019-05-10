__author__ = 'Михайловский Василий Владимирович'

import os
import shutil

print(os.getcwd())

script_name=os.path.basename(__file__)
shutil.copyfile(fr"{os.getcwd()}\{script_name}", fr"{os.getcwd()}\new_{script_name}",)
print(os.listdir(os.getcwd()))
