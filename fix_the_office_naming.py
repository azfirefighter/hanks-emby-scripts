import re
import os

for filename in os.listdir("to_process/"):
    print(filename)
    if 'The Office' in filename and '[' in filename:
        startname = filename
        season = re.search('\[\d', startname)[0]
        episode = re.search('\d\d]', startname)[0]
        season = season[1:]
        episode = episode[:2]
        os.rename("to_process/" + startname, "to_process/" + "The Office S0{0}E{1}".format(season, episode) + ".avi")
