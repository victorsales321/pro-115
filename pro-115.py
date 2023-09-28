import os

from_dir = "C:/Users/Paulosae/OneDrive - Unisys/Desktop/teste1"
to_dir = "C:/Users/Paulosae/OneDrive - Unisys/Desktop/teste2"



file_oldname = os.path.join(from_dir, "liz.txt")
file_newname_newfile = os.path.join(to_dir, "lizauau.txt")

os.rename(file_oldname, file_newname_newfile)