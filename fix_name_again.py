import os

for filename in os.listdir("to_process/"):
    if 'The Office S01' in filename or 'The Office S02':
        os.rename("to_process/" + filename, "to_process/" + filename + ".avi")