import shutil
import os

srcPath = "file1.txt"
destinationPath = "trial/"

#shutil.copy(srcPath,destinationPath) #copies a file
shutil.move(srcPath,destinationPath) #moves a file