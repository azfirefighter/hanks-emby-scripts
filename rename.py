import os
import re

for filename in os.listdir("to_process/"):
    startname = filename
    m = re.search('S\d\dE\d\d', filename)
    if m is not None:
        filename = filename[:filename.index(m.group(0))+6]
    filename = filename.replace(' ', '.')
    filename = filename.replace('-', '')
    os.rename("./to_process/" + startname, "./to_process/" + filename + startname[len(startname)-4:])

