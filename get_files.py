import glob
import os

where = "C:/Users/Gerrid/Documents/test/" # Where folders is created

os.chdir(where)

e = glob.glob("*")
print(f"Total Folders: {e.__len__()}")
with open("existing_files.txt", "w") as write_:
     write_.write("\n".join(e)) 

    