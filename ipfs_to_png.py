import os
import shutil

path = "./apebase/ipfs"
new = "./apebase/data/ipfs_png2"

os.mkdir(new)

for i in os.listdir(path):
    f = os.path.join(path,i)
    c = os.path.join(new,i + ".png")
    shutil.copy(f,c)

