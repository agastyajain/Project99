import os
import shutil


def main():
    path = input("Enter a directory that needs to be sorted : ")
    list = os.listdir(path)
    for file in list:
        name, extension = os.path.splitext(file)
        extension = extension[1:]
        print(extension)
        if extension == "":
            continue
        if not os.path.exists(path+'/'+extension):
            os.makedirs(path+'/'+extension)
        shutil.move(path+'/'+file, path+'/'+extension)

main()
