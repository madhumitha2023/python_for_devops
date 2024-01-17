import os

folders_path = input("Please rovide the folder names with spaces inbetween: ").split()

for folder in folders_path:
    files = os.listdir(folder)
    print(f"=====Below are the list of files for the folder {folder}=======")
    for file in files:
        print(file)