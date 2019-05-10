__author__ = 'Михайловский Василий Владимирович'
import os

print(os.getcwd())

for i in range(1,10):
    os.mkdir(fr"{os.getcwd()}\dir_{i}")
print(os.listdir(os.getcwd()))
for i in range(1,10):
    os.rmdir(fr"{os.getcwd()}\dir_{i}")
print(os.listdir(os.getcwd()))

